/**
 * Created by jinhyeok on 2018. 1. 22..
 */
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

function readCSV() {
    $.ajax({
        type:'GET',
        url: 'save_2.csv',
        dataType: 'text',
      }).done(parseCSV);
}

function readSrcCSV() {
    $.ajax({
        type:'GET',
        url: 'srcNode.csv',
        dataType: 'text',
      }).done(srcNodeAdd());
}

function readDstCSV() {
    $.ajax({
        type:'GET',
        url: 'dstNode.csv',
        dataType: 'text',
      }).done(dstNodeAdd());
}

function srcNodeAdd(data){
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);
    for(var row = 1; row < csv.length; row++){
        var parsed = csv[row].split(',');
        var srcIp = parsed[0];
        var weight = parsed[1];

        nodes.push({id: srcIp, label: srcIp, group: 'internet', value: weight});
    }
}

function dstNodeAdd(data){
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);
    for(var row = 1; row < csv.length; row++){
        var parsed = csv[row].split(',');
        var dstIp = parsed[0];
        var weight = parsed[1];

        nodes.push({id: dstIp, label: dstIp, group: 'internet', value: weight});
    }
}


/**
 * CSV파일을 parsing하여 node와 edge를 push하는 함수입니다.
 * @author ryan
 * @param {*} data
 */
function parseCSV(data) {
        readSrcCSV()
        readDstCSV()
    var reg= /\r?\n|\r/;
    var csv = data.split(reg);

    // Draw nodes
    for(var row = 1; row < csv.length; row++) {
        var parsed = csv[row].split(',');
        var sip = parsed[1];
        var dip = parsed[3];

        edges.push({from: sip, to: dip, length: LENGTH_SUB, color: GRAY,
                    fontColor: GRAY, width: WIDTH_SCALE});
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