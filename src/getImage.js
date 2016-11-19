a = [];
$(function() {
    var params = {
        // Request parameters
        "q": "code programming",
        "count": "1",
        "offset": "0",
        "mkt": "en-us",
        "safeSearch": "Strict",
    };
    
    $.ajax({
        url: "https://api.cognitive.microsoft.com/bing/v5.0/images/search?" + $.param(params),
        beforeSend: function(xhrObj){
            // Request headers
            xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key", keys.microsoftapi);
        },
        type: "GET",
        // Request body
        data: "{body}",
    })
    .done(function(data) {
        a = data;
        $('#slide').attr("src", data['value'][0]['contentUrl'])
        alert("success");
    })
    .fail(function() {
        alert("error");
    });
});
