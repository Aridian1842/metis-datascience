var width = 960,
    height = 500;

var currentyear = 2002;

////// SETUP THE MAP
var color = d3.scale.threshold()
    .domain([0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22])
    .range(['#fff7ec','#fee8c8','#fdd49e','#ffffcc','#ffeda0','#fed976','#feb24c','#fd8d3c','#fc4e2a','#e31a1c','#bd0026','#800026']);

var path = d3.geo.path();

var svg = d3.select("#map").append("svg")
    .attr("width", width)
    .attr("height", height);

d3.select('#year').text(currentyear);


queue()
    .defer(d3.json, "js/us.json")
    .defer(d3.tsv, "js/finaldata.tsv")
    .await(ready)

function ready(error, us, rates) {
    if (error) throw error;

    var us_data = d3.map(rates, function(d) { return d.id; });

    console.log(us_data);

///// BUILD THE MAP
    svg.append("g")
          .attr("class", "counties")
        .selectAll("path")
          .data(topojson.feature(us, us.objects.counties).features)
        .enter().append("path")
          .attr("d", path)
          .style("fill", function(d) {
          try { return color(us_data.get(d.id)[currentyear]); }
          catch(err) { return 0; }
                });

      svg.append("path")
          .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a.id !== b.id; }))
          .attr("class", "states")
          .attr("d", path);

          d3.select('#slider')
                .call(
                d3.slider()
                .value(currentyear)
                .min(2002)
                .max(2014)
                .step(1)
                .axis(true)
                .on("slide", function(evt,value) {
                d3.select('#year').text(value);
                currentyear = value;

                  svg.append("g")
                        .attr("class", "counties")
                      .selectAll("path")
                        .data(topojson.feature(us, us.objects.counties).features)
                      .enter().append("path")
                        .attr("d", path)
                        .style("fill", function(d) {
                        try { return color(us_data.get(d.id)[currentyear]); }
                        catch(err) { return 0; }
                              });

                })
          );


}
