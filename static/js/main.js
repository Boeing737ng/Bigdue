
$(document).ready(function() {
    var menu = document.getElementsByClassName('menu')[0];
    if (window.location.pathname == '/') {
        menu.style.display = 'none';
    }else{
        menu.style.display = 'block';
    }
});

function sendDataToServer(first_value, last_value ,timestamp) {
    if(first_value < 0){
        first_value = 0;
    }
    localStorage.setItem("current_timestamp",timestamp);
    var script_root = getScriptRoot();
    $.getJSON(script_root + '/', {
        first: first_value,
        last: last_value,
        current_timestamp: timestamp,
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
    slider.style.width = '75%';
    slider.style.margin = 'auto';
    noUiSlider.create(slider, {
        start: [parseInt(timestamp[0]), parseInt(timestamp[timestamp.length-1])],
        connect: true,
        tooltips: true,
        range: {
            'min': parseInt(min)-1,
            'max': parseInt(max)+1
        }
    });
    convertToolTipText();
    slider.noUiSlider.on('set', function( values, handle ) {
        var timestamp = document.getElementsByClassName('noUi-tooltip');
        value_arr = String(values).split(',');
        if(handle === 0){
            timestamp[0].innerHTML = convertTimestamp(parseFloat(value_arr[0]));
        }
        if(handle === 1){
            timestamp[1].innerHTML = convertTimestamp(parseFloat(value_arr[1]));
        }
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
    // var hours = "0" + date.getHours();
    // var minutes = "0" + date.getMinutes();
    // // Display time in 10:30:23 format
    // var formattedTime = hours.substr(-2) + ':' + minutes.substr(-2);
    var formattedTime = date.toLocaleString()
    return formattedTime;
}

function getSelectedData() {
    var timeStampInS = getCurrentTimestamp();
    var timestamp = getTimestamp();
    var selected_time =  slider.noUiSlider.get();
    var first_file = findClosestValue(parseInt(selected_time[0]), timestamp);
    var second_file = findClosestValue(parseInt(selected_time[1]), timestamp);
    console.log(first_file + '|'+ second_file);
    sendDataToServer(getIndexOfElement(first_file), getIndexOfElement(second_file) + 1,timeStampInS);
}

function getCurrentTimestamp() {
    var timeStampInMs = window.performance 
        && window.performance.now 
        && window.performance.timing 
        && window.performance.timing.navigationStart 
        ? window.performance.now()  
        + window.performance.timing.navigationStart : Date.now();
    var timeStampInS = Math.ceil(timeStampInMs);
    return timeStampInS;
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
    var timeStampInS = getCurrentTimestamp();
    var timestamp = getTimestamp();
    setLoadingText('Analysing all data...');
    displayGuideText('All data selected. Choose your desired visualized item on top. <b>IT MAY TAKE SOME TIME!</b>');
    sendDataToServer(0,timestamp.length,timeStampInS);
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
    setLoadingText('Analysing the selected data...');
    displayGuideText('Select the time range of your desired section and submit');
    displayOrHideOption();
    createDragOption(timestamp[0], timestamp[timestamp.length - 1]);
}

function showLoading(){
    document.getElementsByClassName("animationload")[0].style.display = "block";
}

function hideLoading(){
    document.getElementsByClassName("animationload")[0].style.display = "none";
}

function displayGuideText(text) {
    var guide_text = document.getElementById('guide_text');
    guide_text.innerHTML = text;
}

function setLoadingText(text) {
    var loading_text = document.getElementsByClassName('loading_text')[0];
    loading_text.innerHTML = text;
}

function displayOrHideOption() {
    var extendable_box = document.getElementsByClassName('jumbo')[0];
    if(extendable_box.style.height === '450px'){
        displayGuideText('');
        extendable_box.style.animationName = 'slide_up'; 
        extendable_box.style.animationDuration = '800ms';
        extendable_box.style.height = '250px';
        $('#slider_container').fadeOut('fast');
    }
    else{
        extendable_box.style.animationName = 'slide_down'; 
        extendable_box.style.animationDuration = '600ms';
        extendable_box.style.height = '450px';
        $('#slider_container').fadeIn('slow');
    }
}