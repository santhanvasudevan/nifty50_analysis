import os
import yaml
import pandas as pd

# Define the root folder where YAML files are stored
yaml_root_folder = "AI ML\Stock Market Analysis\input\data"
output_folder = "AI ML\Stock Market Analysis\output"

# Initialize an empty DataFrame
merged_df = pd.DataFrame()

# Loop through all directories and subdirectories
for root, _, files in os.walk(yaml_root_folder):
    for filename in files:
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            file_path = os.path.join(root, filename)

            # Load YAML data
            with open(file_path, "r") as file:
                data = yaml.safe_load(file)  # Load as list of dictionaries

            # Convert to DataFrame and append to merged_df
            df = pd.DataFrame(data)
            merged_df = pd.concat([merged_df, df], ignore_index=True)

# Save the merged DataFrame as a CSV file
output_csv = os.path.join(output_folder, "merged_data.csv")
merged_df.to_csv(output_csv, index=False)

print(f"Merged CSV file saved as '{output_csv}'")
