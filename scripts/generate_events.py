import pandas as pd
import numpy as np
from datetime import timedelta
import os

# Reproducible results
np.random.seed(42)

# Load users
users_df = pd.read_csv("data/raw/users.csv")

# Convert signup date
users_df["signup_date"] = pd.to_datetime(
    users_df["signup_date"]
)

# Project timeline
PROJECT_START = pd.Timestamp("2024-01-01")
PROJECT_END = pd.Timestamp("2025-12-31")

# Number of events
NUM_EVENTS = 75000

# Event type distribution
event_types = {
    "login": 0.25,
    "task_created": 0.20,
    "task_completed": 0.15,
    "note_created": 0.10,
    "workspace_created": 0.08,
    "file_uploaded": 0.07,
    "ai_prompt_used": 0.10,
    "subscription_purchased": 0.05
}

# Feature mapping
feature_mapping = {
    "login": "Platform",
    "task_created": "Task Manager",
    "task_completed": "Task Manager",
    "note_created": "Notes",
    "workspace_created": "Team Workspace",
    "file_uploaded": "File Sharing",
    "ai_prompt_used": "AI Assistant",
    "subscription_purchased": "Billing"
}

# Device distribution
device_types = {
    "Desktop": 0.50,
    "Mobile": 0.40,
    "Tablet": 0.10
}

# Platform distribution
event_sources = {
    "Web": 0.60,
    "Android": 0.25,
    "iOS": 0.15
}

events = []

for i in range(1, NUM_EVENTS + 1):

    user = users_df.sample(1).iloc[0]

    user_id = user["user_id"]

    signup_date = user["signup_date"]

    # Ensure events stay within project timeline
    max_days = (PROJECT_END - signup_date).days

    if max_days <= 0:
        event_date = signup_date
    else:
        event_date = signup_date + timedelta(
            days=np.random.randint(
                0,
                max_days + 1
            )
        )

    event_type = np.random.choice(
        list(event_types.keys()),
        p=list(event_types.values())
    )

    feature_name = feature_mapping[event_type]

    # AI events have longer sessions
    if event_type == "ai_prompt_used":

        session_duration = np.random.randint(
            15,
            46
        )

    elif event_type in [
        "task_created",
        "task_completed"
    ]:

        session_duration = np.random.randint(
            5,
            26
        )

    else:

        session_duration = np.random.randint(
            2,
            21
        )

    device_type = np.random.choice(
        list(device_types.keys()),
        p=list(device_types.values())
    )

    event_source = np.random.choice(
        list(event_sources.keys()),
        p=list(event_sources.values())
    )

    events.append([
        f"E{i:06d}",
        user_id,
        event_date.date(),
        event_type,
        feature_name,
        session_duration,
        device_type,
        event_source
    ])

# Create dataframe
events_df = pd.DataFrame(
    events,
    columns=[
        "event_id",
        "user_id",
        "event_date",
        "event_type",
        "feature_name",
        "session_duration_minutes",
        "device_type",
        "event_source"
    ]
)

# Ensure output directory exists
os.makedirs(
    "data/raw",
    exist_ok=True
)

# Save file
output_file = "data/raw/events.csv"

events_df.to_csv(
    output_file,
    index=False
)

print("=" * 60)
print("EVENTS DATASET GENERATED SUCCESSFULLY")
print("=" * 60)

print(f"Total Events: {len(events_df):,}")

print(
    f"Event Start Date: "
    f"{events_df['event_date'].min()}"
)

print(
    f"Event End Date: "
    f"{events_df['event_date'].max()}"
)

print(
    f"Output File: {output_file}"
)

print("=" * 60)

print("\nSample Records:")
print(events_df.head())