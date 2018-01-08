var nodes = null;
var edges = null;
var network = null;

var LENGTH_MAIN = 1000,
    LENGTH_SERVER = 100,
    LENGTH_SUB = 5000,
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
        max: 50
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

function readCSV() {
    $.ajax({
        type:'GET',
        url: 'test.csv',
        dataType: 'text',
      }).done(parseCSV);
}

function parseCSV(data) {
    nodes = []; // Create a data table with nodes.
    edges = []; // Create a data table with links.
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);
    
    // Draw nodes
    for(var row = 1; row < csv.length; row++) {
        var parsed = csv[row].split(',');
        var srcIP = parsed[1];
        nodes.push({id: srcIP, label: srcIP, group: 'switch', value: parsed[5]});
    }

    // Draw edges
    for(var i = 1; i < csv.length; i++) {
        var parsed = csv[i].split(',');
        var srcIP = parsed[1];
        var destinationIP = parsed[3];
        console.log(srcIP + " ---> " + destinationIP);
        edges.push({from: srcIP, to: destinationIP, length: LENGTH_MAIN, color: GRAY, width: WIDTH_SCALE * 3, label: '0.71 mbps'});
    }
    var container = document.getElementById('mynetwork');
    var data = {
      nodes: nodes,
      edges: edges
    };
    network = new vis.Network(container, data, options);
}