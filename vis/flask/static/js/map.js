// svg path for target icon
var targetSVG = "M9,0C4.029,0,0,4.029,0,9s4.029,9,9,9s9-4.029,9-9S13.971,0,9,0z M9,15.93 c-3.83,0-6.93-3.1-6.93-6.93S5.17,2.07,9,2.07s6.93,3.1,6.93,6.93S12.83,15.93,9,15.93 M12.5,9c0,1.933-1.567,3.5-3.5,3.5S5.5,10.933,5.5,9S7.067,5.5,9,5.5 S12.5,7.067,12.5,9z";
// svg path for plane icon
var planeSVG = "M19.671,8.11l-2.777,2.777l-3.837-0.861c0.362-0.505,0.916-1.683,0.464-2.135c-0.518-0.517-1.979,0.278-2.305,0.604l-0.913,0.913L7.614,8.804l-2.021,2.021l2.232,1.061l-0.082,0.082l1.701,1.701l0.688-0.687l3.164,1.504L9.571,18.21H6.413l-1.137,1.138l3.6,0.948l1.83,1.83l0.947,3.598l1.137-1.137V21.43l3.725-3.725l1.504,3.164l-0.687,0.687l1.702,1.701l0.081-0.081l1.062,2.231l2.02-2.02l-0.604-2.689l0.912-0.912c0.326-0.326,1.121-1.789,0.604-2.306c-0.452-0.452-1.63,0.101-2.135,0.464l-0.861-3.838l2.777-2.777c0.947-0.947,3.599-4.862,2.62-5.839C24.533,4.512,20.618,7.163,19.671,8.11z";

window.onload = function () {
  var isMap = document.getElementById('chartdiv');
  if(isMap){
    this.setReloadTime();
    setInterval(function () {
      this.setReloadTime();
    }, 60000);
  }
}

$(document).ready(function() {
  if (window.location.pathname == '/map') {
    readMapNodeCSV();
    readMapEdgeCSV();
  }
});

// get node
function readMapNodeCSV() {
    $.ajax({
        type:'GET',
        url: 'static/data/1517900990/map/node.csv',
        dataType: 'text',
        success: function (response) {
          console.log("Nodes extracted")
        },
        error: function (error) {
          console.log(error)
        }
      }).done(addCountry);
}

// get edge
function readMapEdgeCSV() {
  $.ajax({
      type:'GET',
      url: 'static/data/1517900990/map/edge.csv',
      //async: false,
      dataType: 'text',
      success: function (response) {
        console.log("Edges extracted")
      },
      error: function (error) {
        console.log(error)
      }
    }).done(addLine);
}

function getCurrentTime() {
  var date = new Date();
  var hours = date.getHours() > 12 ? date.getHours() - 12 : date.getHours();
  var am_pm = date.getHours() >= 12 ? "pm" : "am";
  hours = hours < 10 ? "0" + hours : hours;
  var minutes = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
  time = hours + ":" + minutes + am_pm;
  return time;
}

function getCurrentDate() {
  var current_Date = new Date();
  var year = current_Date.getFullYear();
  var month = current_Date.getMonth() + 1; // getMonth() starts from 0
  var date = current_Date.getDate();
  date = date < 10 ? "0" + date: date;
  month = month < 10 ? "0" + month: month;
  var today = year + "/ " + month + "/ " + date;
  return today;
}

function setReloadTime() {
  var time = document.getElementById('time');
  time.innerHTML = this.getCurrentDate() + "/ - " + this.getCurrentTime();
}

// PARAMETER REQUIRED: latitude, longitude, country name, scale
function addCountry(data) {
  var reg= /\r?\n|\r/;
  var csv = data.split(reg);
  for(var row = 1; row < csv.length - 1; row++){
    var parsed = csv[row].split(',');
    var latitude = parsed[0];
    var longitude = parsed[1];
    var country = parsed[2];
    var city = new AmCharts.MapImage();

    city.title = country;
    city.latitude = latitude;
    city.longitude = longitude;
    city.type = "circle";
    city.chart = map;
    city.scale = 0.5;
    map.dataProvider.images.push(city);
    city.validate();

  }
}

// PARAMETER REQUIRED: src[lattitude,longitude], dst[lattitude,longitude], weight
function addLine(data) {
  var reg= /\r?\n|\r/;
  var csv = data.split(reg);
  for(var row = 1; row < csv.length; row++){
    var parsed = csv[row].split(',');
    var src_lat = parsed[0];
    var src_lng = parsed[1];
    var dst_lat = parsed[2];
    var dst_lng = parsed[3];
    var line_size = parseInt(parsed[4]);
    var log_value = parseInt(Math.log10(line_size));
    var line = new AmCharts.MapLine();

    line.latitudes = [ src_lat, dst_lat ];
    line.longitudes = [ src_lng, dst_lng ];
    line.thickness = log_value; // Maximum value: 10
    line.arrowSize = (line.thickness * 1.7);
    line.chart = map;
    map.dataProvider.lines.push(line);
    line.validate();
  }
}

var map = AmCharts.makeChart( "chartdiv", {
  "type": "map",
  "theme": "light",
  "dataProvider": {
    "map": "worldLow",
    "zoomLevel": 2.5,
    "zoomLongitude": -86.9571,
    "zoomLatitude": 40.4763,

    "lines": [],
    "images": []
  },

  "areasSettings": {
    "unlistedAreasColor": "#FFCC00",
    "unlistedAreasAlpha": 0.9
  },

  "imagesSettings": {
    "color": "#CC0000",
    "rollOverColor": "#CC0000",
    "selectedColor": "#000000"
  },

  "linesSettings": {
    "arc": -0.7, // this makes lines curved. Use value from -1 to 1
    "arrow": "middle",
    "color": "#CC0000",
    "alpha": 0.4,
    "arrowAlpha": 1,
    "arrowSize": 4,
    "bringForwardOnHover": true
  },
  "zoomControl": {
    "gridHeight": 100,
    "draggerAlpha": 1,
    "gridAlpha": 0.2
  },

  "backgroundZoomsToTop": true,
  "linesAboveImages": true,
  
  "export": {
    "enabled": true
  }
});