
function convertTimestamp(){
    var timestamp = getTimestamp();
    for(var i = 0 ; i < timestamp.length; i++){
        var integer_time = parseInt(timestamp[i]);
        var date = new Date(integer_time*1000);
        // Hours part from the timestamp
        var hours = date.getHours();
        // Minutes part from the timestamp
        var minutes = "0" + date.getMinutes();
        // Seconds part from the timestamp
        var seconds = "0" + date.getSeconds();

        // Will display time in 10:30:23 format
        var formattedTime = hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
        console.log(timestamp[i] + " : " + formattedTime);
    }
}
convertTimestamp();

$(function() {
    $('#show_data').bind('click', function() {
        var timestamp = getTimestamp();
        var script_root = getScriptRoot();
        $.getJSON(script_root + '/sendValue', {
            data: JSON.stringify(timestamp),
        }, function(data) {
            $("#result").text(data.result);
        });
        return false;
    });
});