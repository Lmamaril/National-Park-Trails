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

// Test add data
var trailData = 
[["Harding Ice Field Trail", "Kenai Fjords National Park", 1161.8976],
["Grandview Point to Horseshoe Mesa Trail","Grand Canyon National Park", 726.948],
["Clouds Rest Trail via Tenaya Lake", "Yosemite National Park", 948.8424]]

// adding the elevation gain header
d3.select("body").append("h4").text("Elevation Gain")

d3.select("body").selectAll("p")
       .data(trailData)
       .enter()
       .append("p")
       .text(function(trail) {return trail[0] + " " + trail[2]})

