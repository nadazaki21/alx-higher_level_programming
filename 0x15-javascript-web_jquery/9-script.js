
$(document).ready(function() {
    $.ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        method: "GET",
        success: function(data) {
        //data: "json"
        $('DIV#hello').text("Hello " + data.hello);
        },
        error: function() {
        alert("Failed to fetch movie titles.");
        }
    });
});
    