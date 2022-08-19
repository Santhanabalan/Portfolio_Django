$(document).ready(function() {
    $("#sgpa").submit(function() {
        // Get all the forms elements and their values in one step
        var values = $(this).serialize();
        console.log(values);
    });
});