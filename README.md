#About the Project

Artificial Intelligence and deep learning has revolutionized data modelling and prediction. 

Our hack revolves around the use of Artificial intelligence in the geospatio-temporal prediction of the spread of diseases.

We intend to build a data modelling toolkit that takes a hybrid approach to train the model that uses both data from previous years and non-conventional data sources such as social media, newspapers. Additional parameters can be considered while building the model.

Multiple inferences can be derived from the model. 

Some of the potential use cases for the general population include:
    
- Risk factor of contracting a disease at the user's location
- Travel guidlines based on the risk factor

Mylan can also leverage this technology to 

- Find the best time to procure raw materials for manufacturing drugs
- Estimate the demand for a particular drug at a particular location


#Technologies Used

- Artifical intelligence using Recurrent Neural Networks
- Scraping newspapers using Python - Scrapy
- Scraping social media using Tweepy (twitter) and Facebook-SDK
- Data storage - MongoDB
- Application Server - NodeJS
- Frontend - HTML5, CSS3, JavaScript

#How it works

- For Each disease, the system scrapes newspapers, twitter, Facebook and existing previous years data to build a data model using Recurrent Neural Networks which learns/predicts sequences. 
- Multiple views can access the data model in order to derive conclusions and visualize various aspects.