import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# Function to get correct model filename for a company
def get_model_filename(ticker):
    return f"{ticker}_stock_model.keras"

# Function to fetch stock data
def get_stock_data(ticker="AAPL"):
    data = yf.download(ticker, start="2020-01-01", end="2025-01-01")
    return data

# Function to prepare test data
def prepare_data(prices, lookback=50):
    scaler = MinMaxScaler(feature_range=(0, 1))
    prices_scaled = scaler.fit_transform(prices)

    X_test = []
    for i in range(lookback, len(prices_scaled)):
        X_test.append(prices_scaled[i-lookback:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    return X_test, scaler

# Function to forecast next 7 days
def forecast_next_days(model, prices, scaler, lookback=50, days=7):
    last_sequence = prices[-lookback:]
    last_sequence_scaled = scaler.transform(last_sequence)

    forecast = []
    current_seq = last_sequence_scaled.reshape(1, lookback, 1)

    for _ in range(days):
        next_pred = model.predict(current_seq)[0][0]
        forecast.append(next_pred)

        current_seq = np.append(current_seq[:, 1:, :], [[[next_pred]]], axis=1)

    forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1))
    return forecast

# Main loop for multiple companies
companies = ["AAPL", "AMZN", "MSFT", "TSLA", "GOOGL"]
all_forecasts = {}

for ticker in companies:
    print(f"\n🔹 Processing {ticker}...")

    model_filename = get_model_filename(ticker)
    model = load_model(model_filename)

    data = get_stock_data(ticker)
    prices = data["Close"].values.reshape(-1, 1)

    X_test, scaler = prepare_data(prices)
    predicted_prices = model.predict(X_test)
    predicted_prices = scaler.inverse_transform(predicted_prices)

    # Forecast next 7 days
    forecast = forecast_next_days(model, prices, scaler)
    print(f"{ticker} - Next 7 Days Forecast:")
    print(forecast.flatten())

    # Save forecast for CSV
    all_forecasts[ticker] = forecast.flatten()

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(prices, color="blue", label=f"Actual {ticker} Price")
    plt.plot(range(50, len(predicted_prices)+50), predicted_prices, color="red", label="Predicted Price")
    plt.plot(range(len(prices), len(prices)+7), forecast, color="green", marker="o", label="7-Day Forecast")
    plt.title(f"{ticker} Stock Price Prediction & Forecast")
    plt.xlabel("Time")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.show()

# Save all forecasts to CSV
df_forecasts = pd.DataFrame(all_forecasts).T
df_forecasts.columns = [f"Day {i+1}" for i in range(df_forecasts.shape[1])]
df_forecasts.to_csv("stock_forecasts.csv")

print("\n✅ All forecasts saved to stock_forecasts.csv")

