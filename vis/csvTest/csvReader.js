var nodes = null;
var edges = null;
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

function readCSV() {
    $.ajax({
        type:'GET',
        url: 'save_1.csv',
        dataType: 'text',
      }).done(parseCSV);
}

function parseCSV(data) {
    nodes = []; // Create a data table with nodes.
    edges = []; // Create a data table with links.
    var tempSrcIP = [],
        tempDestIP = [];
    var duplicateSrcFromSrc = false,
        duplicateSrcFromDes = false,
        duplicateDesFromSrc = false,
        duplicateDesFromDes = false;
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);
    
    // Draw nodes
    for(var row = 1; row < csv.length; row++) {
        var parsed = csv[row].split(',');
        var sip = parsed[1];
        var dip = parsed[3];
        // Check duplicate IP address
        for(var i = 0; i < tempSrcIP.length; i++) {
          if(sip === tempSrcIP[i]) {
            duplicateSrcFromSrc = true;
            //break;
          }
          if(sip === tempDestIP[i]) {
            duplicateSrcFromDes = true;
            //break;
          }
          if(dip === tempSrcIP[i]) {
            duplicateDesFromSrc = true;
            //break;
          }
          if(dip === tempDestIP[i]) {
            duplicateDesFromDes = true;
            //break;
          }
        }
        tempSrcIP.push(sip);
        tempDestIP.push(dip);
        
        if(!duplicateSrcFromSrc && !duplicateSrcFromDes) {
          nodes.push({id: sip, label: sip, group: 'internet', value: 20});
        }
        if(!duplicateDesFromSrc && !duplicateDesFromDes) {
          if(sip !== dip) {
            nodes.push({id: dip, label: dip, group: 'internet', value: 20});
          }
        }
        edges.push({from: sip, to: dip, length: LENGTH_SUB, color: GRAY, 
                    fontColor: GRAY, width: WIDTH_SCALE});
        duplicateSrcFromSrc = false;
        duplicateSrcFromDes = false;
        duplicateDesFromSrc = false;
        duplicateDesFromDes = false;
    }
    var container = document.getElementById('mynetwork');
    var data = {
      nodes: nodes,
      edges: edges
    };
    network = new vis.Network(container, data, options);
    network.on("stabilizationIterationsDone", function () {
      network.setOptions({
          nodes: {physics: false},
          edges: {physics: false},
      });
  });
}