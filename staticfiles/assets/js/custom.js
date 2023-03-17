// Cgpa
$(document).ready(function () {
    //Gpp
    $('form').hide();
    $('#theory').show();
    $('#inputState').change(function () {
        $('form').hide();
        $('#'+$(this).val()).show();})
    //sgc
    $( "#addRow").click(function(){
        var x = $(form).serializeArray();
        $.each(x, function(i, field) {
        alert(field.name + " : " + field.value + " ");
        });
        });
    //sgpa
    $('form').hide();
    $('#5').show();
    $('#inputState').change(function () {
        $('form').hide();
        $('#'+$(this).val()).show();})
  });
  