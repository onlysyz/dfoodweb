var divid='#chart'
var w = 190,
	h = 190;

var colorscale = d3.scale.category10();

var LegendOptions = ['中石油','神华','中航信','中山'];

var d = [
		  [
			{axis:"安全漏洞扫描",value:5},
			{axis:"网页木马检测",value:7},
			{axis:"被黑网站检测",value:4},
			{axis:"仿冒网站监测",value:3},
			{axis:"内容违规检测",value:4},
		  ],[
			{axis:"安全漏洞扫描",value:4},
			{axis:"网页木马检测",value:4},
			{axis:"被黑网站检测",value:2},
			{axis:"仿冒网站监测",value:2},
			{axis:"内容违规检测",value:4},
		  ],[
			{axis:"安全漏洞扫描",value:3},
			{axis:"网页木马检测",value:5},
			{axis:"被黑网站检测",value:1},
			{axis:"仿冒网站监测",value:4},
			{axis:"内容违规检测",value:1},
		  ],[
			{axis:"安全漏洞扫描",value:6},
			{axis:"网页木马检测",value:1},
			{axis:"被黑网站检测",value:6},
			{axis:"仿冒网站监测",value:3},
			{axis:"内容违规检测",value:0},
		  ]
		];

	
		
//Options for the Radar chart, other than default
var mycfg = {
  w: w,
  h: h,
  maxValue: 10,
  levels: 5,
  ExtraWidthX: 200
}

//Call function to draw the Radar chart
//Will expect that data is in %'s
RadarChart.draw(divid, d, mycfg);

////////////////////////////////////////////
/////////// Initiate legend ////////////////
////////////////////////////////////////////

var svg = d3.select(divid)
	.selectAll('svg')
	.append('svg:g')
	.attr("width", w+100)
	.attr("height", h)

//Create the title for the legend
var text = svg.append("text")
	.attr("class", "title")
	.attr('transform', 'translate(90,0)') 
	.attr("x", w - 70)
	.attr("y", 10)
	.attr("font-size", "12px")
	.attr("fill", "#ddd")
	.text("Web扫描结果");
		
//Initiate Legend	
var legend = svg.append("g")
	.attr("class", "legend")
	.attr("height", 100)
	.attr("width", 200)
	.attr('transform', 'translate(90,20)') 
	;
	//Create colour squares
	legend.selectAll('rect')
	  .data(LegendOptions)
	  .enter()
	  .append("rect")
	  .attr("x", w - 65)
	  .attr("y", function(d, i){ return i * 20;})
	  .attr("width", 10)
	  .attr("height", 10)
	  .style("fill", function(d, i){ return colorscale(i);})
	  ;
	//Create text next to squares
	legend.selectAll('text')
	  .data(LegendOptions)
	  .enter()
	  .append("text")
	  .attr("x", w - 52)
	  .attr("y", function(d, i){ return i * 20 + 9;})
	  .attr("font-size", "11px")
	  .attr("fill", "#aaa")
	  .text(function(d) { return d; })
	  ;	