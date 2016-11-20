$(function() {
    $.ajax({
        url: "http://127.0.0.1:5000/imagelink/",
        type: "GET",
        dataType: 'text'
    })
    .done(function(data) {
        $('#slide').attr("src", data);
    })
    .fail(function() {
        alert("error");
    });
});
