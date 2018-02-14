
//var timestamp = ["1518585580", "1518585582", "1518585584", "1518585585", "1518585586", "1518585587", "1518585589", "1518585590", "1518585591", "1518585592", "1518585594", "1518585622", "1518585628", "1518585629", "1518585645", "1518585705", "1518585740", "1518585761", "1518585762", "1518585765", "1518585766"];

$(document).ready(function() {
    var menu = document.getElementsByClassName('menu')[0];
    if (window.location.pathname == '/') {
        menu.style.display = 'none';
    }else{
        menu.style.display = 'block';
    }
});

function sendDataToServer(first_value, last_value) {
    var script_root = getScriptRoot();
    $.getJSON(script_root + '/', {
        first: first_value,
        last: last_value,
        success: function(){
            showGraphOptions();
        }
    });
    return false;
}

function createDragOption(min, max) {
    var timestamp = getTimestamp();
    var slider = document.getElementById('slider');
    var updateSliderValue = document.getElementById('value');
    slider.style.width = '60%';
    slider.style.margin = 'auto';
    noUiSlider.create(slider, {
        start: [parseInt(timestamp[0]), parseInt(timestamp[timestamp.length-1])],
        connect: true,
        tooltips: true,
        range: {
            'min': parseInt(min),
            'max': parseInt(max)
        }
    });
    convertToolTipText();
    slider.noUiSlider.on('set', function( values, handle ) {
        var timestamp = document.getElementsByClassName('noUi-tooltip');
        console.log(values + ',' + handle);
        if(handle === 0){
            timestamp[0].innerHTML = convertTimestamp(timestamp[0].innerHTML);
        }
        if(handle === 1){
            timestamp[1].innerHTML = convertTimestamp(timestamp[1].innerHTML);
        }
        //updateSliderValue.innerHTML = convertTimestamp(values[handle]);
        //convertToolTipText();
    });
}

function convertToolTipText() {
    var timestamp = document.getElementsByClassName('noUi-tooltip');
    for(var i = 0; i < timestamp.length; i++){
        timestamp[i].innerHTML = convertTimestamp(timestamp[i].innerHTML);
    }
}

function convertTimestamp(timestamp){
    Math.trunc(timestamp);
    var integer_time = parseInt(timestamp);
    var date = new Date(integer_time*1000);
    var hours = "0" + date.getHours();
    var minutes = "0" + date.getMinutes();
    // Display time in 10:30:23 format
    var formattedTime = hours.substr(-2) + ':' + minutes.substr(-2);
    return formattedTime;
}

function onSelectAllData() {
    var timestamp = getTimestamp();
    console.log(timestamp);
    sendDataToServer(0,timestamp.length);
}

function getIndexOfElement(element) {
    var index =  timestamp.indexOf(element);
    return index;
}

function showGraphOptions() {
    var menu = document.getElementsByClassName('menu')[0];
    menu.style.display = 'block';
}

function openSelectMenu() {
    var timestamp = getTimestamp();
    createDragOption(timestamp[0], timestamp[timestamp.length - 1]);
    var option = document.getElementById('slider_container');
    option.style.display = 'block';
}