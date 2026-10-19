# Stock Market Analysis with Python

This project provides tools to analyze and visualize stock market data using Python. It focuses on price trends, Z-Score normalization, and Delta Volume analysis to assist in understanding market behaviors and patterns. 

## Features
- **Data Retrieval**: Fetches historical stock data (e.g., MSFT, AAPL, GOOG) using the `yfinance` library for a customizable period.
- **Price Charting**: Includes functions to visualize stock closing prices with overlays for Simple Moving Averages (SMA).
- ![image](https://github.com/user-attachments/assets/ed038829-1d4c-4e53-9f31-d1b0b0f4f0aa)
- 
- **Rolling Z-Score**: a causal rolling 20-bar Z-score of the close (each value uses only past bars) that shows how far price is from its recent mean.
![image](https://github.com/user-attachments/assets/77b1fa2f-caa0-4d16-8860-ad400227c99f)
![image](https://github.com/user-attachments/assets/f085a51a-6c70-4d6c-9ef6-2ac3fdc68947)

- **Estimated Delta Volume**: a close-location proxy for buy/sell volume (Yahoo has no real buy/sell split), shown as cumulative % of total volume so different stocks can be compared.
- ![image](https://github.com/user-attachments/assets/9ed683a1-ca8b-40a8-8adf-422e84fef8b8)


## Functionalities
1. **Draw Price Charts**:
   - Plots closing price trends for selected stocks over a specified timeframe.
   - Adds a 15-day Simple Moving Average (SMA) line for better trend identification.

2. **Rolling Z-Score**:
   - `(close − rolling mean) / rolling std` over the last 20 bars. It is causal: past values never change when new data arrives.
   - Shows Z over time and a bar chart of the latest Z per stock.

3. **Delta Volume Analysis**:
   - Estimated delta = volume × (2 × (close − low)/(high − low) − 1), shown cumulatively as a % of total volume.
   - It describes past volume pressure. It has not been tested as a predictor.

## Applications
- Analyzing stock price trends with SMA overlays.
- Seeing how stretched price is versus its recent mean (rolling Z).
- Comparing estimated volume pressure across stocks (normalised).
- Visualizing key metrics for data-driven trading decisions.

## Requirements
- Python (>= 3.7)
- Libraries: `yfinance`, `pandas`, `matplotlib` (tests: `nbclient`, `nbformat`, `ipykernel`, `pytest`)

## Usage
1. Clone the repository and install the required libraries.
2. Use the provided scripts to:
   - Fetch financial data for chosen stocks.
   - Generate price trend visualizations with SMA overlays.
   - Perform Z-score and Delta Volume analyses.

**This project is intended solely for educational purposes and should not be considered financial advice.**
