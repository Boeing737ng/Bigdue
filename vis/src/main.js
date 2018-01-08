var nodes = null;
var edges = null;
var network = null;

var LENGTH_MAIN = 100,
    LENGTH_SERVER = 100,
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
function draw() {
  nodes = []; // Create a data table with nodes.
  edges = [];// Create a data table with links.

  // Create main server
  nodes.push({id: 1, label: '192.168.0.1', group: 'switch', value: 20});
  nodes.push({id: 2, label: '192.168.0.2', group: 'switch', value: 18});
  nodes.push({id: 3, label: '192.168.0.3', group: 'switch', value: 26});
  nodes.push({id: 4, label: '192.168.0.4', group: 'switch', value: 50});
  edges.push({from: 1, to: 2, length: LENGTH_MAIN, color: GRAY, width: WIDTH_SCALE * 3, label: '0.71 mbps'});
  edges.push({from: 1, to: 3, length: LENGTH_MAIN, color: GRAY, width: WIDTH_SCALE * 3, label: '0.55 mbps'});
  edges.push({from: 1, to: 4, length: LENGTH_MAIN, color: GRAY, width: WIDTH_SCALE * 3, label: '0.65 mbps'});
  
  // group around 1
  for (var i = 10; i <= 15; i++ ) {
    nodes.push({id: i, label: '192.168.0.' + i, group: 'mobile', value: 2});
    edges.push({from: 1, to: i, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});
  }
  nodes.push({id: 16, label: '192.168.0.' + 16, group: 'mobile', value: 2});
  edges.push({from: 10, to: 16, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});
  nodes.push({id: 17, label: '192.168.0.' + 17, group: 'mobile', value: 2});
  edges.push({from: 13, to: 17, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});
  nodes.push({id: 18, label: '192.168.0.' + 18, group: 'mobile', value: 2});
  edges.push({from: 14, to: 18, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});

  nodes.push({id: 204, label: 'Internet', group: 'server', value: 10});
  edges.push({from: 1, to: 204, length: 200, width: WIDTH_SCALE * 1, label: '0.63 mbps'});

  // group around 2
  for (var i = 100; i <= 104; i++) {
    var width = WIDTH_SCALE * 2;
    nodes.push({id: i, label: '192.168.0.' + i, group: 'internet', value: 1});
    edges.push({from: 2, to: i, length: LENGTH_SUB, color: GRAY, width: width, label: null});
  }
  nodes.push({id: 201, label: '192.168.0.201', group: 'internet', value: 1});
  edges.push({from: 2, to: 201, length: LENGTH_SUB, color: GRAY, width: WIDTH_SCALE});

  // group around 3
  for (var i = 227; i <= 231; i++ ) {
    nodes.push({id: i, label: '192.168.0.' + i, group: 'mobile', value: 2});
    edges.push({from: 3, to: i, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});
  }

  // group around 4
  for (var i = 30; i <= 49; i++ ) {
    nodes.push({id: i, label: '192.168.0.' + i, group: 'mobile', value: 2});
    edges.push({from: 4, to: i, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});
  }
  nodes.push({id: 50, label: '192.168.0.' + i, group: 'internet', value: 2});
  edges.push({from: 41, to: 50, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});
  nodes.push({id: 51, label: '192.168.0.' + i, group: 'internet', value: 2});
  edges.push({from: 34, to: 51, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});
  nodes.push({id: 52, label: '192.168.0.' + i, group: 'internet', value: 2});
  edges.push({from: 38, to: 52, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});
  nodes.push({id: 53, label: '192.168.0.' + i, group: 'internet', value: 2});
  edges.push({from: 49, to: 53, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});

  // legend
  // var mynetwork = document.getElementById('mynetwork');
  // var x = - mynetwork.clientWidth / 2 + 50;
  // var y = - mynetwork.clientHeight / 2 + 50;
  // var step = 70;
  // nodes.push({id: 1000, x: x, y: y, label: 'Internet', group: 'internet', value: 1, fixed: true, physics:false});
  // nodes.push({id: 1001, x: x, y: y + step, label: 'Switch', group: 'switch', value: 1, fixed: true,  physics:false});
  // nodes.push({id: 1002, x: x, y: y + 2 * step, label: 'Server', group: 'server', value: 1, fixed: true,  physics:false});
  // nodes.push({id: 1003, x: x, y: y + 3 * step, label: 'Computer', group: 'desktop', value: 1, fixed: true,  physics:false});
  // nodes.push({id: 1004, x: x, y: y + 4 * step, label: 'Smartphone', group: 'mobile', value: 1, fixed: true,  physics:false});

  // create a network
  var container = document.getElementById('mynetwork');
  var data = {
    nodes: nodes,
    edges: edges
  };
  network = new vis.Network(container, data, options);
}