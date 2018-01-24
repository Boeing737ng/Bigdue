window.onload = function () {
    $.ajax({
        type: 'GET',
        url: "static/data/file.txt",
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        }
    });
};