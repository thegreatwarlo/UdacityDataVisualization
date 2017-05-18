# UdacityDataVisualization

SUMMARY

This visualization shows the volume on-time performance of arrival flights at 
the San Diego (SAN) airport between January 2003 and February 2017. The data is
grouped by airline. The source is the Bureau of Transportation statistics 
website (https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp). 

Main Takeaways:
- Southwest consolidated its presence at the San Diego Airport over time, with
  considerable growth in volume until 2009
- Volume of flights overall increase until 2007, then decrease to stabilize
  around 2011
- Delays (particularly the one not caused by the airline itself) seem 
  correlated to the volume of flights by carrier

DESIGN

My goal was to compared the volume and performance of each airline in terms of delayed flights for each year. Stacked bars allowed me to both show the overall number of arriving flights for each airline and the proportion of these that was delayed. Also, I was able to compare the year over year performance by animating through each year in the data in order to show a time trend.

After receiving the first feedback (Hanna's), I decided to fix the x axis so it wouldn't rescale after each animation. This allowed the viewer to better compare the number of flights between two years.

The second (Lea's) and third (Paolo's) feedback that I received motivated me to add more flavorto the data related to delays by airline by distinguishing between the ones that were airline specific and the ones that weren't. I also added a short paragraph to describe how the visualization is interactive and what the length of the bars on the right of the main graph represent


FEEDBACK


#1 - Hanna
"I like the way your use of the graph, but the x axis moving around is kind of distracting. I think if it stayed the same it would be easier for me to compare between two years. Right now I cannot really get a precise idea of the difference in the number of flights between two years unless I pay very close attention to the value of the axis"



#2 - Lea
What do you notice in the visualization?
"First, I noticed that Southwest supports the most flights by a much larger margin than expected. Second, I noticed that Southwest had rapid sustained growth through 2009, before decreasing in volume, but increasing in on-time flights through present. "

What questions do you have about the data?
"How did flight distance impact this data? How did price point?"

What relationships do you notice?
"The decrease in flight volume across non-Southwest airlines correlates with an increase in Southwest flight volume."

What do you think is the main takeaway from this visualization?
"Southwest is taking over the airline business in San Diego."

Is there something you don’t understand in the graphic?
"I paid most attention to the changes in flight volume and less attention to the changes in the ontime/delayed ratio." 



#3 - Paolo
What do you notice in the visualization?
"Southwest consolidating its presence over time in SAN"

What questions do you have about the data?
"How many delays are airline specific vs. airport specific?"

What relationships do you notice?
"Overall number of flights changes over the years in addition to the % change 
between airlines"

What do you think is the main takeaway from this visualization?
"SAN Is a hub for Southwest?"

Is there something you don’t understand in the graphic?
"The volume of flights by carrier over time?"


RESOURCES:
- http://stackoverflow.com/questions/25559658/dimple-js-how-to-customize-range-of-values-on-y-axis-from-0-to-100
- https://discussions.udacity.com/t/uncaught-typeerror-a-scaletime-is-not-a-function/244966/4
- http://dimplejs.org/examples_viewer.html?id=bars_vertical_stacked
- http://dimplejs.org/advanced_examples_viewer.
- http://annapawlicka.com/pretty-charts-with-dimple-js/ 
- http://stackoverflow.com/questions/35434829/get-correct-percent-in-dimplejs-vertical-100-bar-chart
- https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple#filterData


