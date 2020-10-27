# Dollar-Rupee-Predictor

## Introduction

This project focuses on one of many applications of time series “Predicting Prices of Dollar-Rupee based on previous trend”. The problem can also be compared to “stock market analysis” or “company financial trend analysis”. This project emphasizes on providing accurate predictions for future trend and there by help the investors to know the market condition.<br><br>

## Tools and Technology

The main language used for programming is python and anaconda navigator is used as an IDE. Google Colab is used for fast training of the model and experimenting with model structure. 

List of python libraries

<b>-</b> Numpy - matrix operation<br>
<b>-</b> Pandas - dataset operations<br>
<b>-</b> Matplotlib - visualization<br>
<b>-</b> Sklearn - Preprocessing<br>
<b>-</b> Tensorflow/Keras - model building and training<br>
<b>-</b> BeautifulSoup - Data scrapping<br><br>

## Proposed Methodology

<b>Step 1:</b> Collection of raw data. In this step, we collected the raw data (historical data for USD/INR) from the following source<br> https://www.poundsterlinglive.com/bank-of-england-spot/historical-spot-exchange-rates/usd/USD-to-INR.<br>

<b>Step 2:</b> Data Pre-processing In this step, we did data transformation by scaling the data between 0 and 1. We didn’t have any missing values which made us skip the process of data cleaning. Then, we merged all the raw data and prepared a dataset. In this step, we also split the data into training and test sets. We used 30 percent of the total data as testing data and 70 percent as training data.<br>

<b>Step 3:</b> Construction of LSTM model In this step, we constructed an LSTM model based on the description presented below.<br> 

<b>Step 4:</b> Forecasting future values In the final step, we forecast the future values based on the previous values of USD/INR.<br><br>

## Model Description

The model consists of a single layered LSTMs with 100 neurons followed by dropouts for regularization and the dense layer for desired out was used. The model summary for the project is as follows.<br><br>
![image](https://user-images.githubusercontent.com/54568147/97261690-5acb1200-1845-11eb-85cf-14abb5e54fad.png)<br><br>

## Results

### <b>1.</b> Srapping Rupee price for Dollar from 2015 onwards<br>
![image](https://user-images.githubusercontent.com/54568147/97261339-a16c3c80-1844-11eb-8e94-ea98d5499369.png)<br>

### <b>2.</b> Training Loss Vs Validation Loss comparison<br>
![image](https://user-images.githubusercontent.com/54568147/97261437-d8425280-1844-11eb-917f-00786af72820.png)<br>
![image](https://user-images.githubusercontent.com/54568147/97261445-de383380-1844-11eb-98c4-951aa2839338.png)<br>

### <b>3.</b> Predicted Prices for training and test set<br>
![image](https://user-images.githubusercontent.com/54568147/97261538-0cb60e80-1845-11eb-938b-59941db84100.png)<br>
    Training performance<br>
![image](https://user-images.githubusercontent.com/54568147/97261548-0fb0ff00-1845-11eb-9249-a0ff32bb296b.png)<br>
    Testing Performance<br>


