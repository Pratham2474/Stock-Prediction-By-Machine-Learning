



# 💾Stock-Prediction-By-Machine-Learning

Overview This project aims to predict stock prices using machine learning techniques. We’ll focus on forecasting stock prices for a publicly listed company based on historical data. In this example, we’ll use APPLE (AAPL) as our case study.


## 💾Table Of Content

- Introduction 
- Data 
- Methodology 
- Implementation 
- Results 
- Conclusion
## 💾Features
- Introduction:- The stock market is a dynamic environment where stocks and other securities are bought and sold by investors. Predicting stock prices is a challenging task, but machine learning algorithms can help us analyze historical data and make informed predictions.

- Data:- We’ll work with historical stock price data for AAPL, which is publicly traded on NASDAQ. The data will be provided by the Yahoo Finance as yfinance module.

- Methodology:- We’ll use a Long Short-Term Memory (LSTM) model, a deep learning technique, for time series forecasting. LSTM is well-suited for capturing temporal dependencies in sequential data, making it suitable for stock price prediction.

- Implementation:- Data Preparation: Load the historical stock price data and preprocess it.
- Feature Engineering: Create relevant features (e.g., moving averages, volatility, volume ) from the data.
- Model Building: Train an LSTM model using the preprocessed data.
- Evaluation: Evaluate the model’s performance using appropriate metrics.
- Prediction: Use the trained model to predict future stock prices.
- Results:- Share the performance metrics, visualizations, and insights obtained from your model. You can include graphs showing actual vs. predicted stock prices over time.
- Conclusion:- Stock market prediction is a fascinating field, and this project demonstrates how machine learning can be applied to forecast stock prices. Remember that stock markets are influenced by various factors, so predictions may not always be accurate. Continuously refine your model and stay informed about market trends.

## 📈Original Close Price and MA for 250 days

![App Screenshot](https://drive.google.com/file/d/1I4DMRjexeoarTlGCAfALadgt0m9pqbRo/view?usp=drive_link)

## 📈Original Close Price and MA for 200 days

![App Screenshot](http://localhost:8501/media/c3baccf631234b1b46ab716784fc32eea4df843fc197f4c6c33cccd3.png)

## 📈Original Close Price and MA for 100 days

![App Screenshot](http://localhost:8501/media/c8dd51c9c460bdff0d6ae63a216007314457c3959be3e613b958d449.png)

## 📈Original Close Price and MA for 100 days and MA for 250 days

![App Screenshot](http://localhost:8501/media/5d1924c4711b541a2b51e2532f5f2cd5d94edbbf39db53ccb0114b06.png)

## 📖Original Close Price vs Predicted Close price

![App Screenshot](http://localhost:8501/media/cf1da00e7fb9c38712a695e48b1ee0bcc1270a928b161b1b6859c8bd.png)
