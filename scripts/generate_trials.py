import pandas as pd
import numpy as np
from datetime import timedelta
import os

# Reproducible results
np.random.seed(42)

# Load users dataset
users_df = pd.read_csv("data/raw/users.csv")

# 65% of users start a trial
trial_users = users_df.sample(
    frac=0.65,
    random_state=42
).copy()

# Conversion rates by acquisition channel
conversion_rates = {
    "Referral": 0.30,
    "LinkedIn": 0.25,
    "Google Search": 0.18,
    "Direct": 0.15,
    "Product Hunt": 0.12,
    "YouTube": 0.08
}

trials = []

for index, row in trial_users.iterrows():

    user_id = row["user_id"]

    trial_id = f"T{len(trials)+1:05d}"

    signup_date = pd.to_datetime(row["signup_date"])

    # Trial starts 0-7 days after signup
    trial_start_date = signup_date + timedelta(
        days=np.random.randint(0, 8)
    )

    # Fixed 14-day trial
    trial_end_date = trial_start_date + timedelta(days=14)

    acquisition_channel = row["acquisition_channel"]

    conversion_probability = conversion_rates[
        acquisition_channel
    ]

    converted = np.random.rand() < conversion_probability

    if converted:

        trial_status = "Completed"

        days_to_convert = np.random.randint(
            1,
            15
        )

        converted_to_paid = "Yes"

    else:

        trial_status = np.random.choice(
            ["Expired", "Completed"],
            p=[0.8, 0.2]
        )

        days_to_convert = None

        converted_to_paid = "No"

    trials.append([
        trial_id,
        user_id,
        trial_start_date.date(),
        trial_end_date.date(),
        trial_status,
        converted_to_paid,
        days_to_convert
    ])

# Create dataframe
trials_df = pd.DataFrame(
    trials,
    columns=[
        "trial_id",
        "user_id",
        "trial_start_date",
        "trial_end_date",
        "trial_status",
        "converted_to_paid",
        "days_to_convert"
    ]
)

# Ensure folder exists
os.makedirs("data/raw", exist_ok=True)

# Save
output_file = "data/raw/trials.csv"

trials_df.to_csv(
    output_file,
    index=False
)

print("=" * 50)
print("Trials dataset generated successfully")
print(f"Total Trial Records: {len(trials_df):,}")
print(f"Output File: {output_file}")
print("=" * 50)

print("\nSample Records:")
print(trials_df.head())