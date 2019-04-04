from django.shortcuts import render, get_object_or_404
from .models import LectureCategory


def lecture_category_list(request):
    _lecture_category_list = LectureCategory.objects.all().order_by('created_date')
    return render(request, 'lecture/lecture_category_list.html', {'lecture_category_list': _lecture_category_list})


def lecture_category_details(request, pk):
    lecture_category = get_object_or_404(LectureCategory, pk=pk)
    lecture_category_parent_chain = [lecture_category]
    temp_parent_lecture_category = lecture_category.parent
    while temp_parent_lecture_category:
        lecture_category_parent_chain.append(temp_parent_lecture_category)
        temp_parent_lecture_category = temp_parent_lecture_category.parent
    lecture_category_parent_chain.reverse()
    lecture_category_products = lecture_category.lecture_category_products.all().order_by('created_date')

    child_lecture_categories = lecture_category.children.all().order_by('created_date')
    return render(request, 'lecture/lecture_category_details.html',
                  {'lecture_category': lecture_category, 'lecture_category_parent_chain': lecture_category_parent_chain,
                   'child_lecture_categories': child_lecture_categories,
                   'lecture_category_products': lecture_category_products})
