
### About this project
This project is part of my Udacity Data Scientist Nanodegree. It is about customer profiles and customer actions made in Starbucks reward app. The goal of the project is to analyze customer behavior by combining various data sets from the Starbucks reward app, and to predict whether customers will accept offers received through this app.

Find my blog post about this project here: https://medium.com/@jpeltaso/the-starbucks-challenge-who-will-accept-the-offer-c809cdc6731e

### Files in this Repository

In this repository:
* Starbucks_Chhallenge.ipynb - the notebook file containing the data analysis
* /data/portfolio.zip - zip file with portfolio.json, listing the offer portfolio
*/data/profile.zip - zip file with profile.json, listing the customer profiles
*/data/transcript.zip - zip file with transcript.json, listing the app events

### Libraries

* Jupyter Notebooks
* Pandas/Numpy
* Plotly
*Scikit

### Problem Statement

This data set contains simulated data that mimics customer behavior on the Starbucks rewards mobile app. Once every few days, Starbucks sends out an offer to users of the mobile app. An offer can be merely an advertisement for a drink or an actual offer such as a discount or BOGO (buy one get one free). Some users might not receive any offer during certain weeks.

Not all users receive the same offer, and that is the challenge to solve with this data set.

The task in this project is to combine transaction, demographic and offer data to determine which demographic groups respond best to which offer type. This data set is a simplified version of the real Starbucks app because the underlying simulator only has one product whereas Starbucks actually sells dozens of products.

Every offer has a validity period before the offer expires. As an example, a BOGO offer might be valid for only 5 days. Informational offers have a validity period even though these ads are merely providing information about a product; for example, if an informational offer has 7 days of validity, you can assume the customer is feeling the influence of the offer for 7 days after receiving the advertisement.

Transactional data show user purchases made on the app including the timestamp of purchase and the amount of money spent on a purchase. This transactional data also has a record for each offer that a user receives as well as a record for when a user actually views the offer. There are also records for when a user completes an offer.

Also, someone using the app might make a purchase through the app without having received an offer or seen an offer.

### Datas Sets and Data Dictionary

The data is contained in three files:

portfolio.json - containing offer ids and meta data about each offer (duration, type, etc.)
profile.json - demographic data for each customer
transcript.json - records for transactions, offers received, offers viewed, and offers completed
Here is the schema and explanation of each variable in the files:

portfolio.json

id (string) - offer id
offer_type (string) - type of offer ie BOGO, discount, informational
difficulty (int) - minimum required spend to complete an offer
reward (int) - reward given for completing an offer
duration (int) - time for offer to be open, in days
channels (list of strings)
profile.json

age (int) - age of the customer
became_member_on (int) - date when customer created an app account
gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
id (str) - customer id
income (float) - customer's income
transcript.json

event (str) - record description (ie transaction, offer received, offer viewed, etc.)
person (str) - customer id
time (int) - time in hours since start of test. The data begins at time t=0

### Summary 

In this notebook we will focus on two questions:

* Conducting an extensive data analysis, including the demographic composition of the customer base, their purchasing behavior, and which customer group is likely to respond best to discount offers.
* Developing a machine learning model predicting whether or not a customer will accept a specific offer.

This work can serve as a starting point to come up with a profitable offering strategy.
