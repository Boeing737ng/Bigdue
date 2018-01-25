var nodes = [];
var edges = [];
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

$(document).ready(function() {
  if (window.location.pathname == '/graph') {
      readNodeCSV();
  }
});
// get node
function readNodeCSV() {
    $.ajax({
        type:'GET',
        url: 'static/data/node.csv',
        dataType: 'text',
        success: function (response) {
          console.log("Nodes exptracted")
        },
        error: function (error) {
          console.log(error)
        }
      }).done(add_node);
}

// get edge
function readEdgeCSV() {
  $.ajax({
      type:'GET',
      url: 'static/data/edge.csv',
      //async: false,
      dataType: 'text',
      success: function (response) {
        console.log("Edges exptracted")
      },
      error: function (error) {
        console.log(error)
      }
    }).done(add_edge);
}

function add_node(data){
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);
    // Push all the nodes.
    for(var row = 1; row < csv.length - 1; row++){
        var parsed = csv[row].split(',');
        var srcIp = parsed[0];
        var weight = parsed[1];
        nodes.push({id: srcIp, label: srcIp, group: 'internet', value: weight});
    }
    readEdgeCSV();
}

/**
 * Append nodes and edges after parsing the CSV files.
 * @author ryan
 * @param {*} data
 */
function add_edge(data) {
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
    container.innerHTML="yessss";
    var data = {
      nodes: nodes,
      edges: edges
    };
    // Pushes all created data to Chart Library
    network = new vis.Network(container, data, options);
    network.on("stabilizationIterationsDone", function () {
      network.setOptions({
          nodes: {physics: false},
          edges: {physics: false},
      });
  });
}