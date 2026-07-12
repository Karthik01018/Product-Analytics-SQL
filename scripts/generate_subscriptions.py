import pandas as pd
import numpy as np
from datetime import timedelta
import os

# Reproducible results
np.random.seed(42)

# Load datasets
users_df = pd.read_csv("data/raw/users.csv")
trials_df = pd.read_csv("data/raw/trials.csv")

# Keep only converted users
converted_users = trials_df[
    trials_df["converted_to_paid"] == "Yes"
].copy()

# Plan distribution
plans = {
    "Pro": 0.60,
    "Team": 0.30,
    "Enterprise": 0.10
}

# Monthly revenue
plan_revenue = {
    "Pro": 499,
    "Team": 1999,
    "Enterprise": 9999
}

subscriptions = []

for i, row in enumerate(converted_users.itertuples(), start=1):

    user_id = row.user_id

    plan_type = np.random.choice(
        list(plans.keys()),
        p=list(plans.values())
    )

    trial_start = pd.to_datetime(row.trial_start_date)

    days_to_convert = row.days_to_convert

    if pd.isna(days_to_convert):
        days_to_convert = 7

    subscription_start_date = (
        trial_start + timedelta(days=int(days_to_convert))
    )

    # Churn probability by plan
    churn_rates = {
        "Pro": 0.20,
        "Team": 0.12,
        "Enterprise": 0.05
    }

    churned = np.random.rand() < churn_rates[plan_type]

    if churned:

        subscription_status = "Cancelled"

        active_days = np.random.randint(30, 365)

        subscription_end_date = (
            subscription_start_date +
            timedelta(days=int(active_days))
        )

    else:

        subscription_status = "Active"

        subscription_end_date = ""

    billing_cycle = np.random.choice(
        ["Monthly", "Annual"],
        p=[0.80, 0.20]
    )

    subscriptions.append([
        f"S{i:05d}",
        user_id,
        plan_type,
        subscription_start_date.date(),
        subscription_end_date,
        plan_revenue[plan_type],
        subscription_status,
        billing_cycle
    ])

subscriptions_df = pd.DataFrame(
    subscriptions,
    columns=[
        "subscription_id",
        "user_id",
        "plan_type",
        "subscription_start_date",
        "subscription_end_date",
        "monthly_revenue",
        "subscription_status",
        "billing_cycle"
    ]
)

# Ensure output directory exists
os.makedirs("data/raw", exist_ok=True)

output_file = "data/raw/subscriptions.csv"

subscriptions_df.to_csv(
    output_file,
    index=False
)

print("=" * 50)
print("Subscriptions dataset generated successfully")
print(f"Total Subscriptions: {len(subscriptions_df):,}")
print(f"Output File: {output_file}")
print("=" * 50)

print("\nSample Records:")
print(subscriptions_df.head())