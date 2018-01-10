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

    $("#upload").bind("click", function() {
      var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
      if (regex.test($("#fileUpload").val().toLowerCase())) {
        if (typeof FileReader != "undefined") {
          var reader = new FileReader();
          reader.onload = function(e) {
            var rows = e.target.result.split("\n");
            for (var i = 1; i < rows.length; i++) {
              var paresd = rows[i].split(",");
              var sip = paresd[1];
              var dip = paresd[3];
              nodes.push({id: "s" + i, label: sip, group: 'internet', value: 2});
              nodes.push({id: "d" + i, label: dip, group: 'internet', value: 2});
              edges.push({from: "s" + i, to: "d" + i, length: LENGTH_SUB, color: GRAY, fontColor: GRAY, width: WIDTH_SCALE})
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
