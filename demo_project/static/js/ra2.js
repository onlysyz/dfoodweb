function radar(divid,csv_type,csv_data){
//var divid='#chart'
var w = 190,
	h = 190;
var colorscale = d3.scale.category10();
var dd=[];
var LegendOptions =[];//['中石油','神华','中航信','中山'];
var type=[];
d3.csv(csv_type,function(ty){//'type.csv'

	ty.forEach(function(ty_d){
			type.push(ty_d.typename);
		});	

	d3.csv(csv_data,function(data){	//'data.csv'	
		data.forEach(function(d){
			LegendOptions.push(d.company);	
			var tmp=[
				{axis:type[0],value:d.type1},
				{axis:type[1],value:d.type2},
				{axis:type[2],value:d.type3},
				{axis:type[3],value:d.type4},
				{axis:type[4],value:d.type5},
			  ];
			dd.push(tmp);
		});
	
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
RadarChart.draw(divid, dd, mycfg);

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
	.text("公司名称");
		
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
	});
});
}