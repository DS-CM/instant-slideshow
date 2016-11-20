(function updateImage() {
    $.ajax({
        url: "http://localhost:8080/imagelink",
        type: "GET",
        dataType: 'text',
        success: function(data) {
            $('#slide').attr("src", data);
        },
        // fail: function() {
        //     alert("error");
        // },
        complete: function() {
            setTimeout(updateImage, 2000);
        }
    });
})();
