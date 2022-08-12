$(document).ready(function () {
  $('form').hide();
  $('#theory').show();
  $('#inputState').change(function () {
      $('form').hide();
      $('#'+$(this).val()).show();})
});
