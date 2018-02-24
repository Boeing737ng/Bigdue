
$(document).ready(function() {
  if (window.location.pathname == '/timeGraph') {
    google.charts.load('current', {packages:["motionchart"]});
    hideLoading();
    document.body.style.overflow = 'auto';
    var timeStamp = localStorage.getItem('current_timestamp');
    console.log("map:" + timeStamp);
    readSrcCSV(timeStamp);
    readDstCSV(timeStamp);
    showGraphOptions();
  }
});

function readSrcCSV(timeStamp) {
  $.ajax({
      type:'GET',
      url: 'static/data/time/'+ timeStamp +'_src.csv',
      //async: false,
      dataType: 'text',
      success: function (response) {
        google.charts.setOnLoadCallback(function(){
          drawSrcChart(response);
        });
        console.log("Src extracted");
        //drawChart(response)
      },
      error: function (error) {
        console.log(error);
      }
    });
}

function readDstCSV(timeStamp) {
  $.ajax({
      type:'GET',
      url: 'static/data/time/'+ timeStamp +'_dst.csv',
      //async: false,
      dataType: 'text',
      success: function (response) {
        google.charts.setOnLoadCallback(function(){
          drawDstChart(response);
        });
        console.log("Src extracted");
        //drawChart(response)
      },
      error: function (error) {
        console.log(error);
      }
    });
}

function convertTime(timestamp){
  var date = new Date(timestamp*1000);
  var year = date.getFullYear();
  var month = date.getMonth();
  var hours = "0" + date.getHours();
  var minutes = "0" + date.getMinutes();
  var formattedTime = year + ',' + month + ',' + hours.substr(-2) + ',' + minutes.substr(-2);
  return formattedTime;
}

function drawSrcChart(src_data){
  var reg= /\r?\n|\r/;
  var csv = src_data.split(reg);
  var data = new google.visualization.DataTable();
  var row_array = [];
  data.addColumn('string', 'ipaddress');
  data.addColumn('date', 'date');
  data.addColumn('number', 'time');
  data.addColumn('number', 'data size');
  data.addColumn('number', 'count');
  for(var row = 1; row < csv.length - 1; row++){
    var parsed = csv[row].split(',');
    var ip = parsed[0];
    var date = new Date(parseInt(parsed[1]));
    var time = parseInt(parsed[2]);
    var size = parseInt(parsed[3]);
    var count = parseInt(parsed[4]);
    var array = [ip,date,time,size,count];
    row_array.push(array);
  }
  data.addRows(row_array);
  var chart = new google.visualization.MotionChart(document.getElementById('src_time_graph'));

  var options = {};
  options['state'] =
  '{"colorOption":"_UNIQUE_COLOR"}';

  options['width'] = 800;
  options['height'] = 400;
  chart.draw(data, options);
}

function drawDstChart(src_data){
  var reg= /\r?\n|\r/;
  var csv = src_data.split(reg);
  var data = new google.visualization.DataTable();
  var row_array = [];
  data.addColumn('string', 'ipaddress');
  data.addColumn('date', 'date');
  data.addColumn('number', 'time');
  data.addColumn('number', 'data size');
  data.addColumn('number', 'count');
  for(var row = 1; row < csv.length - 1; row++){
    var parsed = csv[row].split(',');
    var ip = parsed[0];
    var date = new Date(parseInt(parsed[1]));
    var time = parseInt(parsed[2]);
    var size = parseInt(parsed[3]);
    var count = parseInt(parsed[4]);
    var array = [ip,date,time,size,count];
    row_array.push(array);
  }
  data.addRows(row_array);
  var chart2 = new google.visualization.MotionChart(document.getElementById('dst_time_graph'));

  var options = {};
  options['state'] =
  '{"colorOption":"_UNIQUE_COLOR"}';

  options['width'] = 800;
  options['height'] = 400;
  chart2.draw(data, options);
}