
$(document).ready(function() {
    var menu = document.getElementsByClassName('menu')[0];
    // if (getPreviousFile() == ''){ // Uncomment if needed
    //     document.getElementById('previous_data').style.display = 'none';
    // }
    if (window.location.pathname == '/') {
        //menu.style.display = 'none';
        displayPcapFile();
        displayCSVFile();
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

function sendPcapDataToServer(pcap_files) {
    var script_root = getScriptRoot();
    $.getJSON(script_root + '/', {
        pcap: JSON.stringify(pcap_files),
        async: false,
        success: function(){
            console.log('files sent');
        }
    });
    return false;
}

function sendCSVDataToServer(csv_files ,timestamp) {
    localStorage.setItem("current_timestamp",timestamp);
    var script_root = getScriptRoot();
    $.getJSON(script_root + '/', {
        selected_csv: JSON.stringify(csv_files),
        current_timestamp: timestamp,
        success: function(){
            showGraphOptions();
            console.log('files sent');
        }
    });
    return false;
}

function onLoadPreviosData() {
    filename = getPreviousFile();
    if (filename == ''){
        displayGuideText('<b>NOT FOUND PREVIOUS FILES!</b>');
    }else{
        setLoadingText('Analysing all data...');
        displayGuideText('Previous data selected. Choose your desired visualized item on top. <b>IT MAY TAKE SOME TIME!</b>');
        showGraphOptions();
        localStorage.setItem('current_timestamp', getPreviousFile());
    }
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
    var formattedTime = date.toLocaleString();
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

function displayPcapFile() {
    var pcap = getPcapFiles();
    if(pcap.length > 0) {
        createTableContent(pcap, 'pcap');
    }
}

function displayCSVFile() {
    var csv = getWiresharkFiles();
    if(csv.length > 0) {
        createTableContent(csv, 'csv');
    }
}

function createTableContent(array, type) {
    var newType = type + '_list';
    var container = document.getElementById(newType);
    for(var i = 0; i < array.length; i++){
        var row = document.createElement('tr');
        var col_input = document.createElement('td');
        var col_file = document.createElement('td');
        var select = document.createElement('input');
        select.setAttribute('type', 'checkbox');
        select.setAttribute('value', array[i]);
        select.className = 'select_file_' + type;

        col_file.innerHTML = array[i];
        col_input.appendChild(select);
        row.appendChild(col_input);
        row.appendChild(col_file);
        container.appendChild(row);
    }
}

function selectData() {
    //clearTableContent();
    //var checkedValue = document.querySelector('.select_file:checked').value;
    var checkedValue = []; 
    var inputElements = document.getElementsByClassName('select_file_pcap');
    for(var i=0; inputElements[i]; ++i){
        if(inputElements[i].checked){
            checkedValue.push(inputElements[i].value);
        }
    }
    if(checkedValue.length > 0){
        sendPcapDataToServer(checkedValue);
    }
    //displayCSVFile();
}

function selectCSVFile() {
    var checkedValue = []; 
    var inputElements = document.getElementsByClassName('select_file_csv');
    for(var i=0; inputElements[i]; ++i){
        if(inputElements[i].checked){
            checkedValue.push(inputElements[i].value);
        }
    }
    if(checkedValue.length > 0){
        var timestamp = getCurrentTimestamp();
        setLoadingText('Analysing the selected data...');
        displayGuideText('All data selected. Choose your desired visualized item on top. <b>IT MAY TAKE SOME TIME!</b>');
        sendCSVDataToServer(checkedValue, timestamp);
    }
}

function clearTableContent() {
    var table = document.getElementById("csv_list");
    // faster way to remove child elements
    while (table.firstChild) {
        table.removeChild(table.firstChild);
    }
}