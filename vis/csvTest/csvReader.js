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
      arrows: {
        to:     {enabled: true, scaleFactor:3, type:'arrow'},
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
    var tempSrcIP = [];
    var tempDestIP = [];
    var duplicateDIP = false;
    var duplicateSIP = false;
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);
    
    // Draw nodes
    for(var row = 1; row < csv.length; row++) {
        var parsed = csv[row].split(',');
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
        if(!duplicateDIP){
          nodes.push({id: sip, label: sip, group: 'internet', value: 20});
        }
        if(!duplicateSIP){
          nodes.push({id: dip, label: dip, group: 'internet', value: 40});
        }
        edges.push({from: sip, to: dip, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE});

        duplicateDIP = false;
        duplicateSIP = false;
    }
    var container = document.getElementById('mynetwork');
    var data = {
      nodes: nodes,
      edges: edges
    };
    network = new vis.Network(container, data, options);
}