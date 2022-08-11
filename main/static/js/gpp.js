$(document).ready(function() {
    $("form").hide();
  })
  
  $("#inputState").change(function() {
    stateChange($(this).val());
  });
  
  function stateChange(stateValue) {
    $("form").hide();
  
    switch (stateValue) {
      case '1':
        $("#theory").show();;
      case '2':
        $("#embed").show();;
    }
  }
