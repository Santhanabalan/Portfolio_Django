$(document).ready(function() {
    $("form").hide();
  })
  
  $("#state").change(function() {
    stateChange($(this).val());
  });
  
  function stateChange(stateValue) {
    $("form").hide();
  
    switch (stateValue) {
      case 'theory':
        $("#theory").show();;
      case 'embed':
        $("#embed").show();;    }
  }
