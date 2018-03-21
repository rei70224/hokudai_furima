
    $(document).ready(function() {
        $('#user_talk_form').submit(function() {  // ボタンクリックでAJAX
            //return falseしないと、ページ遷移が起こり、その時点でcsrf errorになる
            
            $.ajax({
            'url':$('form#user_talk_form').attr('action'),
                'type':'POST',
                'data':{
                    'product_id':$('p[name="product_id"]').text(),
                    'sentence':$('textarea[name="sentence"]').val(),
                },
                'dataType':'json',
                'success':function(response){  // 通信が成功したら動く処理で、引数には返ってきたレスポンスが入る
            $('#chat').append(
                '<div class="user_talk">'+
                    '<div>'+ response.talker + '</div>'+
                    '<div class="balloon">' + response.sentence + '</div>'+
                    '<div>' + response.created_date + '</div>'+
                '</div>');
                },
            });
            return false;
        });
    });
