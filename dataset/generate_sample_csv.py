import pandas as pd

# Path to the file
file_path = "/media/gina/DATA/cv_projects/azure-adf-etl-fao/dataset/faostat_crop_data.csv"


df = pd.read_csv(file_path, low_memory=False)

# Sampling 15 instances
sample_df = df.sample(n=15, random_state=42)

# Save the file
sample_path = "/media/gina/DATA/cv_projects/azure-adf-etl-fao/dataset/faostat_crop_data_sample.csv"
sample_df.to_csv(sample_path, index=False)

print("File at:", sample_path)
