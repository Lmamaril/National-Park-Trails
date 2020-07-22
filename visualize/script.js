// Test addition of a circle
var bodySelection = d3.select("body");
 
var svgSelection = bodySelection.append("svg")
       .attr("width", 50)
       .attr("height", 50);
 
svgSelection.append("circle")
    .attr("cx", 25)
    .attr("cy", 25)
    .attr("r", 25)
    .style("fill", "#dc143c");

// Test edit header
d3.selectAll("h1")
       .style("color", "#22232a")
       .style("font-family", "verdana")