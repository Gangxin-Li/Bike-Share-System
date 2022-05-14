function submit_report() {
    $.ajax({
        type: "post",
        url: "/report/submit_defective",
        data: {
            bike_id: $("#bike_id").val(),
            defective_parts: $("#defective_parts").val(),
            description: $("#description").val()
        },
        statusCode: {
            404: function () {
                console.log("404");
                alert("No such bike id, try another one.");
            },
            200: function () {
                console.log("200");
                alert("Report Successfully");
                window.location.replace("/ume")
            },
            500: function () {
                console.log("500");
                alert("Report Fail, try again.");
            }
        }
    });
}