$("#addRow").click(function () {
    var html = '';
    html += '<div class="form-row">';
    html += '<div class="form-group col-md-5">';
    html += '<label for="inputZip">Course Credit</label>';
    html += '<input type="number" class="form-control" id="cat1" placeholder="Total Credit">';
    html += '</div>';
    html += '<div class="form-group col-md-5">';
    html += '<label for="inputZip">Course Grade</label>';
    html += '<input type="number" class="form-control" id="cat2" min="0" max="10" placeholder="Out of 10">';
    html += '</div>';
    html += '<div class="form-group col-md-2">';
    html += '<label for="inputZip">Remove</label>';
    html += '<button button id="removeRow" type="button" class="form-control btn btn-danger ">Remove</button>';
    html += '</div>';  
    html += '</div>';

    $('#newRow').append(html);
});

// remove row
$(document).on('click', '#removeRow', function () {
    $(this).closest('.form-row').remove();
});