$("form").submit(function(event) {
    var fields = ["#inputTopic", "#inputMemeLevel"];
    var formData = {};

    for (let field of fields) {
        formData[field.replace("#input", "")] = $(field).val();
    }

    console.log(formData);

    /* stop form from submitting normally */
    event.preventDefault();

    /* get some values from elements on the page: */
    var url = "http://localhost:8080/settings";

    /* Send the data using post */
    var posting = $.post(url, formData);

    /* Put the results in a div */
    posting.done(function(data) {
        alert("data saved");
    });

    // $.ajax({
    //     url: "http://localhost:8080/settings",
    //     type: "POST",
    //     data: formData,
    //     dataType: 'json',
    //     success: function(responseData, textStatus, jqXHR) {
    //         alert("data saved")
    //     },
    //     error: function(jqXHR, textStatus, errorThrown) {
    //         console.log(errorThrown);
    //     }
    // });
});
