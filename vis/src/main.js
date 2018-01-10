var nodes = null;
var edges = null;
var network = null;

var LENGTH_MAIN = 500,
    LENGTH_SERVER = 500,
    LENGTH_SUB = 50,
    WIDTH_SCALE = 2,
    GREEN = 'green',
    RED = '#C5000B',
    ORANGE = 'orange',
    GRAY = '#6E6E6E',
    BLACK = '#2B1B17';
var options = {
  nodes: {
    scaling: {
      min: 16,
      max: 32
    }
  },
  edges: {
    color: GRAY,
    smooth: true
  },
  physics:{
    barnesHut:{gravitationalConstant:-30000},
    stabilization: {iterations:2500}
  },
  groups: {
    'switch': {
      shape: 'dot',
      color: '#2B7CE9' // blue
    },
    desktop: {
      shape: 'dot',
      color: "#2B7CE9" // blue
    },
    mobile: {
      shape: 'dot',
      color: "#5A1E5C" // purple
    },
    server: {
      shape: 'dot',
      color: "#C5000B" // red
    },
    internet: {
      shape: 'dot',
      color: "#109618" // green
    }
  }
};

// Called when the Visualization API is loaded.
// csv file read and parse
$(function() {

  nodes = []; // Create a data table with nodes.
  edges = [];// Create a data table with links.

  var tempSrcIP = []; // Array of inserted source IP
  var tempDestIP = []; // Array of inserted destinaion IP
  var duplicateDIP = false;
  var duplicateSIP = false;

  $("#upload").bind("click", function() {
    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
    if (regex.test($("#fileUpload").val().toLowerCase())) {
      if (typeof FileReader != "undefined") {
        var reader = new FileReader();
        reader.onload = function(e) {
          var rows = e.target.result.split("\n");
          // Draw nodes
          for(var row = 1; row < rows.length; row++) {
              var parsed = rows[row].split(',');
              var sip = parsed[1];
              var dip = parsed[3];
              tempSrcIP.push(sip);
              tempDestIP.push(dip);
              // Check duplicate IP address
              for(var i = 0; i < tempSrcIP.length; i++){
                if(sip === tempDestIP[i]){
                  duplicateDIP = true;
                  break;
                }
                if(dip === tempSrcIP[i]){
                  duplicateSIP = true;
                  break;
                }
              }
              if(!duplicateDIP){ // If there is no duplication
                nodes.push({id: sip, label: sip, group: 'internet', value: 20});
              }
              if(!duplicateSIP){
                nodes.push({id: dip, label: dip, group: 'internet', value: 40});
              }
              edges.push({from: sip, to: dip, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});

              duplicateDIP = false;
              duplicateSIP = false;
          }
          // create a network
          var container = document.getElementById('mynetwork');
          var data = {
            nodes: nodes,
            edges: edges
          };
          network = new vis.Network(container, data, options);
        }
        reader.readAsText($("#fileUpload")[0].files[0]);
      }else {
          alert("This browser does not support HTML5.");
        }
      } else {
        alert("Please upload a valid CSV file.");
      }
  });
});