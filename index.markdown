
<style>


body {
    color: #000000; /* Black color */
}

.container1 {
  display: flex; /* This enables flexbox layout, making its children (the two divs) lay out horizontally */
  #border: 2px solid blue; /* If you want the container itself to also have a border */
  width: 1050px; /* Explicitly set the container's width */
  margin: auto; /* This centers the container horizontally in its parent */
  /* Adjust the top and bottom margin as needed, keeping the left and right margins as auto */
  #background-color: #1c1d1f;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  background-color: #262626; 
}

.container2 {
  display: flex; /* This enables flexbox layout, making its children (the two divs) lay out horizontally */
  #border: 2px solid blue; /* If you want the container itself to also have a border */
  width: 1050px; /* Explicitly set the container's width */
  margin: auto; /* This centers the container horizontally in its parent */
  /* Adjust the top and bottom margin as needed, keeping the left and right margins as auto */
  #background-color: #1c1d1f;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  margin-bottom: 40px;
  background-color: #262626; 
}

.container3 {
  display: flex; /* This enables flexbox layout, making its children (the two divs) lay out horizontally */
  #border: 2px solid blue; /* If you want the container itself to also have a border */
  width: 1010px; /* Explicitly set the container's width */
  margin: auto; /* This centers the container horizontally in its parent */
  /* Adjust the top and bottom margin as needed, keeping the left and right margins as auto */
  background-color: #ffffff;
  padding: 5px; 
}

    
div {
  border: 1px solid blue;  Sets a blue border for all divs 
    margin: 0px;
    margin: 0px;
  padding: 0px;
}

.wrapper {
margin: 0px;
}

 
.top-left-box {
  overflow: hidden; /* This hides any overflow the scaling might cause */
  width: 610px;
  height: 430px;
  transform: scale(0.5);
  transform-origin: top left;
  margin-right: -305px; /* Adjust this value as needed to bring the divs closer */

}

.top-left-box iframe, .center-box iframe {
  width: 100%; /* Makes the iframe fill the container */
  height: 100%; /* Adjust the height to match the div's scaling */
  border: 0; /* Removes the iframe border */
  margin-right: 20px;
}

.bottom-left-box {
  width: 610px;

.center-box {
  overflow: hidden;
  width: 680px;
  height: 645px;
  transform: scale(1);
  transform-origin: top left;
}

.bottom-box {
  overflow: hidden;
  width: 1050px;
  height: 345px;
  transform: scale(1);
  transform-origin: top left;
}

.bottom-box iframe, .center-box iframe {
  width: 100%; /* Makes the iframe fill the container */
  height: 100%; /* Adjust the height to match the div's scaling */
  border: 0; /* Removes the iframe border */
}

</style>


  <div class="container3">
     <section class="home">
        <h1>Crime in San Francisco: A data story3</h1>
        <p>Looking at the crime in San Francisco, there can be shown many interesting aspects of the historical development, trends, and popular locations of the crimes in this region. In this story of the crime that has occurred in San Francisco, we start by giving a brief introduction to the dataset that has been used to make visualizations and to gain insights.</p>
     </section>
  </div>


  <div class="container1" >
    <div class="left-column">
      <div class="top-left-box">
        <iframe src="interactive_crime_hours.html"></iframe> 
      </div>
      <div class="bottom-left-box">
        <p style="color: white;">The barchart shows a 24-hour cycle of a crime category. The map shows specific incidents reported, visualizing where cimr have happened. The timeline chart shows crime development through out the years for the different districts.</p>
      </div>
    </div>
    <div class="center-box">
          <select id="crimeSelection">
        <option value="map_WEAPON LAWS.html">Weapon Laws</option>
        <option value="Map/map_PROSTITUTION.html">Prostitution</option>
        <option value="Map/map_DRIVING UNDER THE INFLUENCE.html">Driving Under The Influence</option>
        <option value="Map/map_ROBBERY.html">Robbery</option>
        <option value="Map/map_BURGLARY.html">Burglary</option>
        <option value="Map/map_ASSAULT.html">Assault</option>
        <option value="Map/map_DRUNKENNESS.html">Drunkenness</option>
        <option value="Map/map_DRUG_NARCOTIC.html">Drug/Narcotic</option>
        <option value="Map/map_TRESPASS.html">Trespass</option>
        <option value="Map/map_LARCENY_THEFT.html">Larceny/Theft</option>
        <option value="Map/map_VANDALISM.html">Vandalism</option>
        <option value="Map/map_VEHICLE THEFT.html">Vehicle Theft</option>
        <option value="Map/map_STOLEN PROPERTY.html">Stolen Property</option>
        <option value="Map/map_DISORDERLY CONDUCT.html">Disorderly Conduct</option>
</select>

<iframe id="crimeFrame" src="map_WEAPON LAWS.html"></iframe>

<script>
    document.getElementById('crimeSelection').addEventListener('change', function() {
        var selectedCrime = this.value;
        document.getElementById('crimeFrame').src = selectedCrime;
    });
</script>

</div>
  </div>

  <div class="container2">
    <div class="bottom-box" >
      <iframe src="bokeh_timeline_plot.html"></iframe>
    </div>
  </div>



  <div class="container3">
      <section class="home">
        <h2>Introduction to the SF Crime Dataset</h2>
        <p>The data that has been used, comes from the dataset Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240130.csv, that can be accessed and downloaded on San Francisco´s police department website. The data spans from 2003 to May of 2018, and consists of occurrences of different crimes, such as assault, burglary, vehicle theft and so on, as well as where and when these crimes have occurred.<p/>
     

  <div class="container3">
     <section class="home">
        <h2>Visualizing crime & finding insights</h2>
        <p>Looking at the data visualizations, there are a total of 3 different visuals. There is a bar-chart, showcasing the trend on a 24-hour cycle of a specific type of crime, this can give an insight into when a crime is more likely to occur. There is also a map, which shows the specific coordinates (latitude and longitude) of where crime has occurred, the crime can be sorted based on what types of crime, as well as which year and month the crime happened. The last visual is a time series, that shows the development through time of the number of incidents of crime in different districts within San Francisco, this graph enables the comparison of different districts regarding the development of crime over a specific period. </p>
        <p>In the following sections, we will take a closer look on each of these visualizations, and what insights can be made from them.                    </p>
     </section>
  </div>

  <div class="container3">
     <section class="home">
        <h3>24-hour crime cycle</h3>
        <p>Looking at the data presented in the bar-chart, some interesting patterns emerge. Choosing for example the crime category Drunkenness you see a clear patterns of behaviour, almost linearly, the probability of drunkenness being reported rises from 05:00 and tops at around midnight, whereafter it drastically declines after 02:00, perhaps the drunk people tend to go to sleep here. Interestingly, the category Weapon laws follow the somewhat the same pattern as the Drunkenness, perhaps they could even be correlated. The same goes for Driving under the influence, though the tendency is more towards the later hours. </p>
     </section>
  </div>

  <div class="container3">
     <section class="home">
        <h3>Geospatial data</h3>
            <p>The map shows where the different crimes in each crime group have occurred, this can give valuable information about crime hotspots, which is indeed what we see for some of the crime categories. The data has been filtered to show data for the year 2017. If all data was plotted, it would remove any notable trends, as there is so much data that it would be hard to find any patterns. Though, a heatmap would solve this problem, as it shows densities of data much better. </p>
            <p>Focusing on the Prostitution category, we see a clear hot spot for sex work in the Mission district of San Francisco. A quick internet search of “San Francisco prostitution hot spot” also quickly leads to an article [1], that describes this district as a hub for prostitution. </p>
            <p>From looking at most of the other crime categories, it becomes clear that the hotspot for crime in general is around the Southern district. But there are also crimes that are more evenly distributed throughout different districts, such as assault and vandalism. </p>
     </section>
  </div>

  <div class="container3">
     <section class="home">
        <h3>Timeline</h3>
            <p>The last graph to showcase is the timeline graph, here the total number of crime incidents throughout the years are displayed. This graph also makes it clear that it is indeed the Southern district that has the biggest incidents of crimes and has had that throughout the years. There also appears to be a sudden increase in crime for the Southern district, around the end of 2010, which persists throughout the following years. </p>
     </section>
  </div>

  <div class="container3">
     <section class="home">
        <h2>Conclusion</h2>
            <p>This report investigates crime in San Francisco, using data to show where, when, and what types of crimes have occurred. By analyzing the SF Crime Dataset, we've learned about the patterns of crime across different parts of the city and at different times.</p>
            <p>The data shows us when certain crimes, like drunkenness, are most likely to happen, mostly at night. This information can help the police to be more alert for this crime.</p>
            <p>We also looked at where crimes happen in the city. For example, we found that a lot of prostitution happens in the Mission district, and the Southern district has a high number of crimes in general. This kind of information can help focus efforts to make these areas safer.</p>
            <p>Overall, this report shows that looking at crime data can help in the understanding of where and when crimes happen, which can help make the city safer. </p>
            <p>Some limitations and notes for improvement: It could have been quite interesting exploring the data if the geospatial data could be sorted into different periods of time, for a more precise exploration of data. This did become too challenging with the use of Plotly, but I do believe it could work if Bokeh had been utilized, though Bokeh did have some problems with the X and Y data in the dataset for some time periods, which is why Plotly was ultimately used. </p>
     </section>
  </div>

  <div class="container3">
     <section class="home">
        <h2>References</h2>
            <p>[1] <a href="https://www.latimes.com/california/story/2023-02-09/san-francisco-sex-workers-red-light-district-capp-street-closure">https://www.latimes.com/california/story/2023-02-09/san-francisco-sex-workers-red-light-district-capp-street-closure</a></p>
     </section>
  </div>


  </main>
</body>

