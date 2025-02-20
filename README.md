# 📊 Stock Market Analysis Dashboard

## Overview
This **Streamlit** dashboard provides an interactive visualization of stock market data, allowing users to analyze stock volatility, cumulative returns, sector-wise performance, correlation heatmaps, and monthly top gainers & losers.

## Features
- **Volatility Analysis**: Identifies the most volatile stocks.
- **Cumulative Returns**: Tracks the performance of top stocks over time.
- **Sector-wise Performance**: Analyzes the average yearly return by sector.
- **Stock Price Correlation Heatmap**: Displays stock correlations for trend analysis.
- **Monthly Top Gainers & Losers**: Identifies the best and worst performing stocks each month.

## Installation

### Prerequisites
Ensure you have Python installed. Install dependencies using:
```bash
pip install streamlit pandas numpy seaborn matplotlib
```

### Running the Application
1. Clone the repository & unzip Stock_Market_Analysis.zip file:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. Run the Streamlit app after changing your input folder path as per your requirements:
   ```bash
   streamlit run nifty_50_analysis.py
   ```

## Folder Structure
```
📂 Stock Market Analysis
 ├── 📂 input
 │   ├── sector_data.csv  # Sector classification data
 ├── 📂 output
 │   ├── 📂 individual_output_csv  # Contains stock data CSVs
 ├── nifty_50_analysis.py  # Main Streamlit application
 ├── 📂 screenshots  # Folder containing screenshots
```

## Screenshots
![Dashboard Overview](screenshots/Screenshot1.png)

![Volatility Analysis](screenshots/Screenshot2.png)

## Data Requirements
- **Stock Data Files**: CSVs containing columns like `date`, `close`, `Ticker`.
- **Sector Mapping File**: `sector_data.csv` containing `Symbol` and `Sector`.

## Usage
- The dashboard will visualize stock performance using data from the CSV files.
- Users can explore stock trends, volatility, and sector performance.

## Contributions
Feel free to submit issues or pull requests to improve the dashboard.

## License
This project is licensed under the [MIT License](LICENSE).

