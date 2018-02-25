var nodes = [];
var edges = [];

var check_node = [];
var check_edge = [];
var network = null;

var LENGTH_MAIN = 1000,
    LENGTH_SERVER = 100,
    LENGTH_SUB = 100,
    WIDTH_SCALE = 1,
    GREEN = 'green',
    RED = '#C5000B',
    ORANGE = 'orange',
    GRAY = '#6E6E6E',
    BLACK = '#2B1B17';

var options = {
    layout: {
      improvedLayout: true
    },
    nodes: {
      scaling: {
        min: 16,
        max: 50
      }
    },
    edges: {
      arrows: {
        to:     {enabled: true, scaleFactor:1, type:'arrow'},
        middle: {enabled: false, scaleFactor:3, type:'arrow'},
        from:   {enabled: false, scaleFactor:3, type:'arrow'}
      },
      color: GRAY,
      smooth: true
    },
    physics:{
      barnesHut:{gravitationalConstant:-30000},
      stabilization: {iterations:2500},
      enabled: false
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

$(document).ready(function() {
  if (window.location.pathname == '/graph') {
    hideLoading();
    var timeStamp = localStorage.getItem('current_timestamp');
    console.log("graph:" + timeStamp);
    readNodeCSV(timeStamp);
    readEdgeCSV(timeStamp);
    showGraphOptions();
  }
});

// get node
function readNodeCSV(timeStamp) {
    $.ajax({
        type:'GET',
        url: 'static/data/graph/' + timeStamp + '_node.csv',
        dataType: 'text',
        success: function (response) {
          console.log("Nodes extracted")
        },
        error: function (error) {
          console.log(error)
        }
      }).done(addNode);
}

// get edge
function readEdgeCSV(timeStamp) {
  $.ajax({
      type:'GET',
      url: 'static/data/graph/' + timeStamp + '_edge.csv',
      //async: false,
      dataType: 'text',
      success: function (response) {
        console.log("Edges extracted")
      },
      error: function (error) {
        console.log(error)
      }
    }).done(addEdge);
}

function addNode(data){
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);
    // Push all the nodes.
    for(var row = 1; row < csv.length - 1; row++){
        var parsed = csv[row].split(',');
        var srcIp = parsed[0];
        var weight = parseInt(parsed[1]) / 1000;
        check_node.push(srcIp);
        nodes.push({id: srcIp, label: srcIp, group: 'internet', value: weight});
    }
}
/**
 * Append nodes and edges after parsing the CSV files.
 * @author ryan
 * @param {*} data
 */
function addEdge(data) {
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);
    // Create edges
    for(var row = 1; row < csv.length - 1; row++) {
        var parsed = csv[row].split(',');
        var sip = parsed[0];
        var dip = parsed[1];
        var wid = parsed[2];
        edges.push({from: sip, to: dip, length: LENGTH_SUB, color: GRAY,
                    fontColor: GRAY, width: wid});
    }
    var container = document.getElementById('mynetwork');
    var data = {
      nodes: nodes,
      edges: edges
    };
    // Pushes all created data to Chart Library
    if(container){
      network = new vis.Network(container, data, options);
      network.on("stabilizationIterationsDone", function () {
        network.setOptions({
            nodes: {physics: false},
            edges: {physics: false},
        });
      });
    }
}