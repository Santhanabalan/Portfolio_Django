$(document).ready(function () {
    $('form').hide();
    $('#5').show();
    $('#inputState').change(function () {
        $('form').hide();
        $('#'+$(this).val()).show();})
  });
  