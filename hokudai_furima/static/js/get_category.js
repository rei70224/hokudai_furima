function getcategory(){
  var val = $('[name=category]').val();
  if(val=="digitalitem"){
    $('#digitalitemupload').removeAttr('style');
    $('#digitalitemupload').attr('required', 'required');
    $('.digital_iran_form-group').attr('style', 'display:none;');
    $('.digital_iran_form-group select').removeAttr('required');
  }else {
    $('#digitalitemupload').attr('style', 'display:none;');
    $('#digitalitemupload').removeAttr('required');
    $('.digital_iran_form-group').removeAttr('style');
    $('.digital_iran_form-group select').attr('required', 'required');
  }
  $('.incategory').attr('style', 'display:none;');
  $('.incategory').removeAttr('required');

  $('#'+val).removeAttr('style');
  $('#'+val).attr('required');
}
