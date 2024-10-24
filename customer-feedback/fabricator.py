import pandas as pd
import random

# Function to generate random feedback data
def generate_random_feedback(total_rows=1000, positive_percentage=50):
    """
    Simulates customer feedback data by randomly selecting rows from
    positive and negative feedback datasets.

    Parameters:
    - total_rows: Total number of feedback rows to generate.
    - positive_percentage: Percentage of positive feedback rows (the rest will be negative).

    Returns:
    - None: Saves the combined feedback data to a CSV file.
    """

    # Load the positive and negative feedback data
    positive_df = pd.read_csv(POSITIVE_FILE_PATH)
    negative_df = pd.read_csv(NEGATIVE_FILE_PATH)

    # Calculate the number of positive and negative rows based on the percentage
    positive_count = int((positive_percentage / 100) * total_rows)
    negative_count = total_rows - positive_count

    # Randomly select rows from the positive and negative datasets
    random_positive_df = positive_df.sample(n=positive_count, replace=True, random_state=None)
    random_negative_df = negative_df.sample(n=negative_count, replace=True, random_state=None)

    # Add the 'source' column to label positive and negative data
    random_positive_df['Source'] = 'POSITIVE'
    random_negative_df['Source'] = 'NEGATIVE'

    # Combine the positive and negative data into one DataFrame
    combined_df = pd.concat([random_positive_df, random_negative_df], ignore_index=True)

    # Shuffle the combined data for randomness
    combined_df = combined_df.sample(frac=1, random_state=None).reset_index(drop=True)

    combined_df.to_csv(FINAL_FILE_PATH, index=False)


# Paths to the base CSV files
POSITIVE_FILE_PATH = "customer-feedback/data/positive.csv"
NEGATIVE_FILE_PATH = "customer-feedback/data/negative.csv"
FINAL_FILE_PATH = "customer-feedback/data/fabricated_feedback.csv"

# Example usage
fabricated_data = generate_random_feedback(total_rows=1000, positive_percentage=60)

print(f"Done simulating customer feedback!")
