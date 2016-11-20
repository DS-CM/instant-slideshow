var prevURL = "";

(function updateImage() {
    $.ajax({
        url: "http://localhost:8080/imagelink",
        type: "GET",
        dataType: 'text',
        success: function(data) {
            if (data !== prevURL) {
                prevURL = data;
                var slide = $( "<section class='present'><img></section>" );
                $( slide ).find("img").attr("src", data);
                $( '.present' ).removeClass( "present" ).addClass( "past" );
                $( '#slides' ).append( slide );
                $( '.navigate-right' ).prop('enabled', true); //just enable it, even if it is
            }
        },
        // fail: function() {
        //     alert("error");
        // },
        complete: function() {
            setTimeout(updateImage, 2000);
        }
    });
})();
