
function convertTimestamp(){
    var timestamp = getTimestamp();
    for(var i = 0 ; i < timestamp.length; i++){
        var integer_time = parseInt(timestamp[i]);
        var date = new Date(integer_time*1000);
        var hours = date.getHours();
        var minutes = "0" + date.getMinutes();
        var seconds = "0" + date.getSeconds();
        // Display time in 10:30:23 format
        var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
        console.log(timestamp[i] + " : " + formattedTime);
    }
}
//convertTimestamp();

$(function() {
    $('#show_data').bind('click', function() {
        //var timestamp = getTimestamp();
        var timestamp = ["1","2","3"];
        var script_root = getScriptRoot();
        $.getJSON(script_root + '/', {
            data: JSON.stringify(timestamp),
        }, function(data) {
            $("#result").text(data.result);
        });
        return false;
    });
});

// $(function() {
//     $('#show_data').click(function() {
//         //var timestamp = getTimestamp();
//         
//         $.ajax({
//             url: '/sendValue',
//             data: {"data": JSON.stringify(timestamp)},
//             type: 'POST',
//             contentType: 'application/json;charset=UTF-8',
//             dataType: "json",
//             success: function(response) {
//                 console.log(response);
//             },
//             error: function(error) {
//                 console.log(error);
//             }
//         });
//     });
// });