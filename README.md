# UdacityDataVisualization

SUMMARY

This visualization shows the on-time performance of arrival flights at the San 
Diego (SAN) airport between January 2003 and February 2017. The data is grouped
by airline. The source is the Bureau of Transportation statistics website 
(https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp)


DESIGN

My goal was to compared the performance of each airline in terms of delayed 
flights for each year. Stacked bars allowed me to both show the overall number 
of arriving flights for each airline and the proportion of these that was 
delayed. Also, I was able to compare the year over year performance by 
animating through each year in the data in order to show a time trend.

After receiving the first feedback, I decided to fix the x axis so it wouldn't
rescaled after each animation. This allowed the viewer to better compare the 
number of flights between two years.


FEEDBACK

1 - "I like the way your use of the graph, but the x axis moving around is kind
of distracting. I think if it stayed the same it would be easier for me to 
compare between two years. Right now I cannot really get a precise idea of the
difference in the number of flights between two years unless I pay very close
attention to the value of the axis"


RESOURCES:
- http://stackoverflow.com/questions/25559658/dimple-js-how-to-customize-range-of-values-on-y-axis-from-0-to-100
- https://discussions.udacity.com/t/uncaught-typeerror-a-scaletime-is-not-a-function/244966/4
- http://dimplejs.org/examples_viewer.html?id=bars_vertical_stacked
- http://dimplejs.org/advanced_examples_viewer.


