
### Analyzing Airbnb data for Munich and Berlin

#### Motivation
This project is part of my [Udacity Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025).
Udacity Data Scientist Nanodegree. We will analyze and compare the usage of Airbnb (https://www.airbnb.com/) in two German cities (Munich and Berlin), and build a model for predicting price per night for accomodations in Munich and Berlin.

#### Summary of the results of the analysis
The Medium post related to this Jupyter Notebook can be found here: https://medium.com/@jpeltaso/munich-vs-berlin-an-analysis-of-airbnb-usage-148135ef9768

Based on Inside Airbnb Data for the two cities, we conduct a general explorative analysis, as well as a geospatial and temporal analysis. Also, we use Linear Regression and Random Forest Regression to predict the price per night of accommodations in both cities. The main questions and findngs are:

<ul>
  <li>Q1. What are the main differences in the price structure and in the range of accommodations between Berlin in Munich?</li>
  A1: The main diffference is that the price level is higher in Munich than in Berlin
  <li>Q2. How is the price trend over the year, and are there any notable differences between the two cities?</li>
  A2: In Berlin we can see we can observe a pronounced weekly seasonality (price peaks at the weekends) while in Munich there is a strong yearly price peak during Oktoberfest season.
  <li>Q3. What factors influence the price, and to what extent can we predict the price for the two cities, given the information from Inside Airbnb?</li>
  A3: We identify a number of factors that influence the price in the two cities. We also can state that the goodness of our prediction is lower for Munich than for Berlin. We discuss possible reasons for this, and point out how the prediction could be improved in future work.
</ul>

#### Files in the repository
This projects contains two notebooks:
<ul>
 <li> download_airbnb_data_munich_berlin: downloads the required data sets</li>
 <li>explore_airbnb_data_munich_vs_berlin: reads data from the 'data' folder', performs data cleaning and analysis and fitting the predictive models</li>
</ul>

#### Libraries used
Besides [Pandas](https://pandas.pydata.org/) and [NumPy](https://numpy.org/), the following libraries for visualization and machine learning are used:
 
 * Seaborn: https://seaborn.pydata.org/
 * Plotly: https://plotly.com/
 * Folium: https://python-visualization.github.io/folium/quickstart.html
 * Calplot: https://calplot.readthedocs.io/en/latest/
 * scikit-learn: https://scikit-learn.org/stable/ 

#### Acknowledgments
General:
 * https://www.udacity.com/
 * https://stackoverflow.com/
 
Visualization:
 * https://stackoverflow.com/questions/26463714/pandas-get-combination-of-columns-where-correlation-is-high
 * https://seaborn.pydata.org/examples/many_pairwise_correlations.html
 
Linear regression
* https://statisticsbyjim.com/regression/multicollinearity-in-regression-analysis/
* https://statisticsbyjim.com/regression/check-residual-plots-regression-analysis/

Feature selection
 * https://towardsdatascience.com/how-to-use-variance-thresholding-for-robust-feature-selection-a4503f2b5c3f
 * https://towardsdatascience.com/predicting-airbnb-prices-with-machine-learning-and-deep-learning-f46d44afb8a6
   Rezazadeh, Pouya & Nikolenko, Liubov & Rezaei, Hoormazd. (2019). Airbnb Price Prediction Using Machine Learning and Sentiment Analysis.
 * https://machinelearningmastery.com/rfe-feature-selection-in-python/
 
SHAP:
 * https://towardsdatascience.com/explain-your-model-with-the-shap-values-bc36aac4de3d
 * https://christophm.github.io/interpretable-ml-book/shap.html
 * https://shap.readthedocs.io/en/latest/index.html

