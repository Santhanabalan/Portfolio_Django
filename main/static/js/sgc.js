$(document).ready(function() {
    $( "#addRow").click(function(){
    var x = $(form).serializeArray();
    $.each(x, function(i, field) {
    alert(field.name + " : " + field.value + " ");
    });
    });
    });