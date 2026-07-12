import pandas as pd
import numpy as np
from faker import Faker
from datetime import date
import os

# Initialize Faker
fake = Faker()

# Reproducible results
np.random.seed(42)

# Number of users
NUM_USERS = 5000

# Country distribution
countries = {
    "India": 0.45,
    "United States": 0.20,
    "United Kingdom": 0.10,
    "Germany": 0.10,
    "Australia": 0.08,
    "Singapore": 0.07
}

# Industries
industries = [
    "Technology",
    "Healthcare",
    "Finance",
    "Education",
    "Retail",
    "Marketing"
]

# Company sizes
company_sizes = [
    "1-10",
    "11-50",
    "51-200",
    "201-500",
    "500+"
]

# Acquisition channels
acquisition_channels = {
    "Google Search": 0.30,
    "LinkedIn": 0.20,
    "YouTube": 0.15,
    "Referral": 0.15,
    "Direct": 0.10,
    "Product Hunt": 0.10
}

# Create users list
users = []

for i in range(1, NUM_USERS + 1):

    user_id = f"U{i:05d}"

    user_name = fake.name()

    age = np.random.choice(
        [22, 25, 28, 31, 35, 40, 45, 52],
        p=[0.10, 0.20, 0.20, 0.20, 0.15, 0.08, 0.05, 0.02]
    )

    signup_date = fake.date_between(
        start_date=date(2024, 1, 1),
        end_date=date(2025, 12, 31)
    )

    country = np.random.choice(
        list(countries.keys()),
        p=list(countries.values())
    )

    industry = np.random.choice(industries)

    company_size = np.random.choice(company_sizes)

    acquisition_channel = np.random.choice(
        list(acquisition_channels.keys()),
        p=list(acquisition_channels.values())
    )

    users.append([
        user_id,
        user_name,
        age,
        signup_date,
        country,
        industry,
        company_size,
        acquisition_channel
    ])

# Create DataFrame
users_df = pd.DataFrame(
    users,
    columns=[
        "user_id",
        "user_name",
        "age",
        "signup_date",
        "country",
        "industry",
        "company_size",
        "acquisition_channel"
    ]
)

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# Save CSV
output_file = "data/raw/users.csv"

users_df.to_csv(
    output_file,
    index=False
)

print("=" * 50)
print("Users dataset generated successfully")
print(f"Total Users: {len(users_df):,}")
print(f"Output File: {output_file}")
print("=" * 50)

print("\nSample Records:")
print(users_df.head())