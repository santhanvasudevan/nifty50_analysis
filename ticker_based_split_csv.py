import pandas as pd

# Load the CSV file
df = pd.read_csv(r"AI ML\Stock Market Analysis\output\merged_data.csv")  # Replace with your actual file path

# Get unique tickers
unique_tickers = df["Ticker"].unique()

output_dir = r"AI ML\Stock Market Analysis\output\individual_output_csv"
os.makedirs(output_dir, exist_ok=True)  # Create directory if it does not exist

for ticker in unique_tickers:
    filtered_df = df[df["Ticker"] == ticker]  # Filter data for the ticker
    filtered_df.to_csv(os.path.join(output_dir, f"{ticker}.csv"), index=False)  # Save to CSV

print("CSV files created successfully!")