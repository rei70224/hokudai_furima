from django.test import TestCase, Client
from django.urls import reverse
from .models import LectureCategory


def create_lecture_category(name, description, parent):
    lecture_category = LectureCategory.objects.create(name=name, description=description, parent=parent)
    return lecture_category


class LectureCategoryListViewTests(TestCase):
    def test_zero_lecture_category(self):
        client = Client()
        response = client.get(reverse('lecture:lecture_category_list'))
        self.assertQuerysetEqual(
            response.context['lecture_category_list'],
            []
        )

    def test_one_lecture_category(self):
        create_lecture_category("総合教育部", "主に１年生が受ける授業の科目区分", None)
        client = Client()
        response = client.get(reverse('lecture:lecture_category_list'))
        self.assertQuerysetEqual(
            response.context['lecture_category_list'],
            ['<LectureCategory: 総合教育部>']
        )

    def test_two_lecture_category(self):
        parent = create_lecture_category("総合教育部", "主に１年生が受ける授業の科目区分", None)
        create_lecture_category("一般教育演習(ﾌﾚｯｼｭﾏﾝｾﾐﾅｰ)", "フレッシュマンセミナー", parent=parent)
        client = Client()
        response = client.get(reverse('lecture:lecture_category_list'))
        self.assertQuerysetEqual(
            response.context['lecture_category_list'],
            ['<LectureCategory: 総合教育部>']
        )

    def test_three_lecture_category(self):
        parent = create_lecture_category("総合教育部", "主に１年生が受ける授業の科目区分", None)
        create_lecture_category("一般教育演習(ﾌﾚｯｼｭﾏﾝｾﾐﾅｰ)", "フレッシュマンセミナー", parent=parent)
        create_lecture_category("該当なし", "どの科目区分とも関連していないもの", None)
        client = Client()
        response = client.get(reverse('lecture:lecture_category_list'))
        #print(response.context['lecture_category_list'])
        self.assertQuerysetEqual(
            response.context['lecture_category_list'],
            ['<LectureCategory: 総合教育部>', '<LectureCategory: 該当なし>']
        )


class LectureCategoryDetailsViewTests(TestCase):
    def setUp(self):
        parent = create_lecture_category("総合教育部", "主に１年生が受ける授業の科目区分", None)
        create_lecture_category("一般教育演習(ﾌﾚｯｼｭﾏﾝｾﾐﾅｰ)", "フレッシュマンセミナー", parent=parent)
        create_lecture_category("共通科目", "環境と人間・健康と社会・人間と文化など", parent=parent)

    def test_one_lecture_category(self):
        client = Client()
        lecture_category = LectureCategory.objects.get(pk=1)
        response = client.get(reverse('lecture:lecture_category_details',
                                      kwargs={'pk': lecture_category.pk}))
        self.assertQuerysetEqual(
            [response.context['lecture_category']],
            ['<LectureCategory: 総合教育部>']
        )
        self.assertQuerysetEqual(
            response.context['lecture_category_parent_chain'],
            ['<LectureCategory: 総合教育部>']
        )
        self.assertQuerysetEqual(
            response.context['child_lecture_categories'],
            []
        )
        self.assertQuerysetEqual(
            response.context['lecture_category_products'],
            []
        )

    def test_two_lecture_category(self):

        client = Client()
        print(list(map(lambda x: x.__dict__, LectureCategory.all())))
        lecture_category = LectureCategory.objects.get(pk=1)
        response = client.get(reverse('lecture:lecture_category_details',
                                      kwargs={'pk': lecture_category.pk}))
        self.assertQuerysetEqual(
            [response.context['lecture_category']],
            ['<LectureCategory: 総合教育部>']
        )
        self.assertQuerysetEqual(
            response.context['lecture_category_parent_chain'],
            ['<LectureCategory: 総合教育部>']
        )
        self.assertQuerysetEqual(
            response.context['child_lecture_categories'],
            ['<LectureCategory: 一般教育演習(ﾌﾚｯｼｭﾏﾝｾﾐﾅｰ)>']
        )
        self.assertQuerysetEqual(
            response.context['lecture_category_products'],
            []
        )

    def test_three_lecture_category(self):

        client = Client()
        print(list(map(lambda x: x.__dict__, LectureCategory.all())))
        lecture_category = LectureCategory.objects.get(pk=1)
        response = client.get(reverse('lecture:lecture_category_details',
                                      kwargs={'pk': lecture_category.pk}))
        self.assertQuerysetEqual(
            [response.context['lecture_category']],
            ['<LectureCategory: 総合教育部>']
        )
        self.assertQuerysetEqual(
            response.context['lecture_category_parent_chain'],
            ['<LectureCategory: 総合教育部>']
        )
        self.assertQuerysetEqual(
            response.context['child_lecture_categories'],
            ['<LectureCategory: 一般教育演習(ﾌﾚｯｼｭﾏﾝｾﾐﾅｰ)>', '<LectureCategory: 共通科目>']
        )
        self.assertQuerysetEqual(
            response.context['lecture_category_products'],
            []
        )
