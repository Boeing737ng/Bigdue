var svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var format = d3.format(",d");

var color = d3.scaleOrdinal(d3.schemeCategory20c);

var file_root = 'static/data/graph/';
var pack = d3.pack()
    .size([width, height])
    .padding(1.5);


$(document).ready(function() {
  if (window.location.pathname == '/bubble') {
    hideLoading();
    document.body.style.overflow = 'auto';
    var timeStamp = localStorage.getItem('current_timestamp');
    console.log("bubble:" + timeStamp);
    file_root = file_root + timeStamp;

    d3.csv(file_root + '_node.csv', function(d) {
      d.weight =+Math.sqrt(d.weight);

      if (d.weight) return d;
    }, function(error, classes) {
      if (error) throw error;
      var root = d3.hierarchy({children: classes})
          .sum(function(d) { return d.weight; })
          .each(function(d) {
            if (node = d.data.node) {
              var node, i = node.lastIndexOf(".");
              d.node = node;
              d.package = node.slice(0, i);
              d.class = node.slice(i + 1);
            }
          });
    
      var circle_node = svg.selectAll(".node")
        .data(pack(root).leaves())
        .enter().append("g")
          .attr("class", "node")
          .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
    
          circle_node.append("circle")
          .attr("node", function(d) { return d.node; })
          .attr("r", function(d) { return d.r; })
          .style("fill", function(d) { return color(d.package); });
    
          circle_node.append("clipPath")
          .attr("node", function(d) { return "clip-" + d.node; })
        .append("use")
          .attr("xlink:href", function(d) { return "#" + d.node; });
    
          circle_node.append("text")
          .attr("clip-path", function(d) { return "url(#clip-" + d.node + ")"; })
        .selectAll("tspan")
        .data(function(d) {
          return d.node.split(/(?=[A-Z][^A-Z])/g);
           //return format(Math.pow(d.weight,2)).split(/(?=[A-Z][^A-Z])/g); 
          })
        .enter().append("tspan")
          .attr("x", 0)
          .attr("y", function(d, i, circle_nodes) { return 13 + (i - circle_nodes.length / 2 - 0.5) * 10; })
          .text(function(d) { 
            return d; 
          });
    
          circle_node.append("title")
          .text(function(d) { 
            console.log(d)
            return d.node + "\n" + Math.trunc(d.data.weight); });
    });

  }
});