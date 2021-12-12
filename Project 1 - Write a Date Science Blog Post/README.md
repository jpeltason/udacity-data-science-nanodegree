
### Analyzing Airbnb data for Munich and Berlin

This project is part of my [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).
Udacity Data Scientist Nanodegree. We will analyze and compare the usage of Airbnb (https://www.airbnb.com/) in two German cities (Munich and Berlin), and build a model for predicting price per night for accomodations in Munich and Berlin.

The Medium post related to this Jupyter Notebook can be found here: https://medium.com/@jpeltaso/munich-vs-berlin-an-analysis-of-airbnb-usage-148135ef9768

Based on Inside Airbnb Data for the two cities, we conduct a general explorative analysis, as well as a geospatial and temporal analysis. Also, we use Linear Regression and Random Forest Regression to predict the price per night of accommodations in both cities. We focus on the following questions:

<ul>
  <li>Q1. What are the main differences in the price structure and in the range of accommodations between Berlin in Munich?</li>
  <li>Q2. How is the price trend over the year, and are there any notable differences between the two cities?</li>
  <li>Q3. What factors influence the price, and to what extent can we predict the price for the two cities, given the information from Inside Airbnb?</li>
</ul>

This projects contains two notebooks:
<ul>
 <li> download_airbnb_data_munich_berlin: downloads the required data sets</li>
 <li>explore_airbnb_data_munich_vs_berlin: reads data from the 'data' folder', performs data cleaning and analysis and fitting the predictive models</li>
</ul>

#### Acknowledgments
The following libraries for visualization and machine learning are used by these notebooks:
 
 * Seaborn: https://seaborn.pydata.org/
 * Plotly: https://plotly.com/
 * Folium: https://python-visualization.github.io/folium/quickstart.html
 * Calplot: https://calplot.readthedocs.io/en/latest/
 * scikit-learn: https://scikit-learn.org/stable/ 
