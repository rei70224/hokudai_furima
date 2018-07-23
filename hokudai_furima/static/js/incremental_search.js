$(window).on('load', function(){
    $('#id_q').on('keyup', function(e){
    e.preventDefault();
    var input = $.trim($(this).val());
    $.ajax({
      url: '/search/product/ajax',
      type: 'GET',
      data: ('q=' + input),
      processData: false,
      contentType: false,
      dataType: 'json'
    })
    .done(function(data){ //データを受け取ることに成功したら、dataを引数に取って以下のことする(dataには@usersが入っている状態ですね)
        $('#incremental_search_option').empty()
        $('#incremental_search_option').append('<div class="dropdown"><div class="dropdown-menu show" style="width:100%; margin-top:-10px"></div></div>');
      $(data).each(function(i, product){ //dataをuserという変数に代入して、以下のことを繰り返し行う(単純なeach文ですね)
        $('.dropdown-menu').append('<span class="dropdown-item" onclick="clickDropdownItem(\''+ htmlEscape(product.title).replace('&#x27;', '&quot;') +'\')">' + htmlEscape(product.title) + '</span>') //resultというidの要素に対して、<li>ユーザーの名前</li>を追加する。
      });
    }).fail(function(){
        // エラーの場合処理
        $('#incremental_search_option').empty()
    });
  });
});

function clickDropdownItem(text){
    $('#incremental_search_option').empty();
    setInputText(text);
}

function setInputText(text){
    $('#id_q').val(text);
    console.log('setInputText');
}

function htmlEscape(rawText){
  if(typeof rawText !== 'string') {
    return rawText;
  }
  return rawText.replace(/[&'`"<>]/g, function(match) {
    return {
      '&': '&amp;',
      "'": '&#x27;',
      '`': '&#x60;',
      '"': '&quot;',
      '<': '&lt;',
      '>': '&gt;',
    }[match]
  });
}

