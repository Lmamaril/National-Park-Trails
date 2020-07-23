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

// Horizontal bar graph attempt
var margin = {
    top: 20,
    right: 30,
    bottom: 30,
    left: 220
};

// define wideth and height
var width = 600 - margin.left - margin.right;
var height = 460 - margin.top - margin.bottom;

var svg = d3.select("#elevationGraph")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// create x axis
var x = d3.scaleLinear()
    .domain([0, 1600])
    .range([ 0, width]);
svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .selectAll("text")
        .attr("transform", "translate(-10,0)rotate(-45)")
        .style("text-anchor", "end");

// create y axis
var y = d3.scaleBand()
    .range([ 0, height ])
    .domain(trailData.map(function(d) { return d[0]; }))
    .padding(.1);
svg.append("g")
    .call(d3.axisLeft(y))

// add bars
svg.selectAll("trailRect")
    .data(trailData)
    .enter()
    .append("rect")
        .attr("x", x(0) )
        .attr("y", function(trail) { return y(trail[0]); })
        .attr("width", function(trail) { return x(trail[2]); })
        .attr("height", y.bandwidth() )
        .attr("fill", "#4c9a2a")
    .on("mouseover", function() {
       d3.select(this)
            .attr("fill", "#acdf87");
    })
    .on("mouseout", function(d, i) {
       d3.select(this).attr("fill", "#4c9a2a") 
    })

    // consider hovering to original color
    // function() {
    //     return "" + color(this.fill) + "";
    // }

