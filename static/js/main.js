
$(document).ready(function() {
    var menu = document.getElementsByClassName('menu')[0];
    if (window.location.pathname == '/') {
        menu.style.display = 'none';
    }else{
        menu.style.display = 'block';
    }
});

function sendDataToServer(first_value, last_value) {
    if(first_value < 0){
        first_value = 0;
    }
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

function getSelectedData() {
    var timestamp = getTimestamp();
    var selected_time =  slider.noUiSlider.get();
    var first_file = findClosestValue(parseInt(selected_time[0]), timestamp);
    var second_file = findClosestValue(parseInt(selected_time[1]), timestamp);
    sendDataToServer(getIndexOfElement(first_file), getIndexOfElement(second_file));
}

function findClosestValue (num, array) {
    var current = parseInt(array[0].replace('.csv',''));
    var diff = Math.abs(num - current);
    for (var i = 0; i < array.length; i++) {
        var new_diff = Math.abs(num - parseInt(array[i].replace('.csv','')));
        if (new_diff < diff) {
            diff = new_diff;
            current = array[i];
        }
    }
    return current;
}

function onSelectAllData() {
    var timestamp = getTimestamp();
    console.log(timestamp);
    sendDataToServer(0,timestamp.length);
}

function getIndexOfElement(element) {
    var timestamp = getTimestamp();
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