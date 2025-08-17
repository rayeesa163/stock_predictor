📊 Stock Dashboard

A clean and interactive Stock Dashboard for analyzing historical stock data. Built for data scientists and analysts, it allows users to visualize trends, trading volumes, and export stock data as a CSV file for further analysis.

🚀 Features

Historical stock data – Fetch up to 1 year of data for any stock symbol.

Interactive charts – Open & Close prices and trading volume visualizations.

Company mapping – Symbol → company name for easy identification.

CSV export – Download the latest stock data for analysis.

User-friendly interface – Clean, modern layout for quick exploration.

🖼️ Demo Vedio

https://www.loom.com/share/1601230c418646dd93ed1e07adfc6d6d


⚡ Installation

Clone the repository

git clone https://github.com/rayeesa163/stock_predictor.git
cd stock_dashboard


Create a virtual environment (optional)

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt

🏃 How to Run

python -m streamlit run stock_dashboard.py



Enter a stock symbol (e.g., AAPL).

View historical Open/Close price chart and trading volume chart.

Click Download CSV to export stock data.

🛠️ Tech Stack

Python – Core programming language

Pandas & NumPy – Data manipulation and analysis

yfinance – Fetch historical stock data

Plotly – Interactive charts

Streamlit – Dashboard UI and CSV download

💡 Future Improvements

Add multi-stock comparison.

Include technical indicators like SMA, EMA, RSI.

Allow custom date range selection.

Enhance chart interactivity with hover details.

🤝 Contribution

Contributions are welcome! Submit issues, fork the repo, or create pull requests to improve features, design, or performance.

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
