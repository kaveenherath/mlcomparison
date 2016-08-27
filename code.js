

  function getColor(x) {
    if(x == 1)
      return "#B81D18";
    return "#004687";
  }

  var w = window.innerWidth;
  var h = window.innerHeight;

  var real = d3.select("#real")
            .append("svg")
            .attr("width", h/3)
            .attr("height", h/3);


  var ll = d3.select("#ll")
            .append("svg")
            .attr("width", h/3)
            .attr("height", h/3);

  var knn = d3.select("#knn")
            .append("svg")
            .attr("width", h/3)
            .attr("height", h/3);

  var dt = d3.select("#dt")
            .append("svg")
            .attr("width", h/3)
            .attr("height", h/3);

  var nb = d3.select("#nb")
            .append("svg")
            .attr("width", h/3)
            .attr("height", h/3);


  var xScale = d3.scale.linear().domain([-1,10]).range([0,300]);
  var yScale = d3.scale.linear().domain([50,200]).range([0,300]);


  var myMouseoverFunction = function (){
    var circle = d3.select(this);
				circle.transition()
					.attr("r", circle.attr("r") * 1 + 10 );
  }

  var myMouseoutFunction = function (){
    var circle = d3.select(this);
				circle.transition().duration(200)
					.attr("r", 5 );
  }

  d3.csv("/algo_vis/data.csv", function(data) {

    real.selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", function(d) {
          return xScale(d["x"]);
      })
      .attr("cy", function(d) {
          return yScale(d["y"]);
      })
      .attr("r", 5)
      .on("mouseover", myMouseoverFunction)
      .on("mouseout", myMouseoutFunction)
      .style("fill", function(d) {
        return getColor(d["true"]);
      });



    ll.selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", function(d) {
          return xScale(d["x"]);
      })
      .attr("cy", function(d) {
          return yScale(d["y"]);
      })
      .attr("r", 5)
      .on("mouseover", myMouseoverFunction)
      .on("mouseout", myMouseoutFunction)
      .style("fill", function(d) {
        return getColor(d["ll"]);
      });

    knn.selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", function(d) {
          return xScale(d["x"]);
      })
      .attr("cy", function(d) {
          return yScale(d["y"]);
      })
      .attr("r", 5)
      .on("mouseover", myMouseoverFunction)
      .on("mouseout", myMouseoutFunction)
      .style("fill", function(d) {
        return getColor(d["knn"]);
      });

    dt.selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", function(d) {
          return xScale(d["x"]);
      })
      .attr("cy", function(d) {
          return yScale(d["y"]);
      })
      .attr("r", 5)
      .on("mouseover", myMouseoverFunction)
      .on("mouseout", myMouseoutFunction)
      .style("fill", function(d) {
        return getColor(d["dt"]);
      });


    nb.selectAll("circle")
      .data(data)
      .enter()
      .append("circle")
      .attr("cx", function(d) {
          return xScale(d["x"]);
      })
      .attr("cy", function(d) {
          return yScale(d["y"]);
      })
      .attr("r", 5)
      .on("mouseover", myMouseoverFunction)
      .on("mouseout", myMouseoutFunction)
      .style("fill", function(d) {
        return getColor(d["nb"]);
      });

});
