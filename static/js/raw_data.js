$(document).ready(function() {
    if (window.location.pathname == '/raw_data') {
        hideLoading();
        var container = document.getElementById('raw_packets');
        var timestamp = getTimestamp();
        readPackets(timestamp[0], container);
        showGraphOptions();
    }
});

function readPackets(timestamp, container) {
    $.ajax({
        type:'GET',
        url: 'static/data/packet/'+ timestamp,
        dataType: 'text',
        success: function (response) {
            container.innerHTML = response;
        },
        error: function (error) {
          console.log(error)
        }
      });
}