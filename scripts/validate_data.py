import pandas as pd

print("=" * 60)
print("INSIGHTFLOW DATA VALIDATION REPORT")
print("=" * 60)

# Load datasets
users = pd.read_csv("data/raw/users.csv")
trials = pd.read_csv("data/raw/trials.csv")
subscriptions = pd.read_csv("data/raw/subscriptions.csv")
events = pd.read_csv("data/raw/events.csv")

# --------------------------------------------------
# USERS
# --------------------------------------------------

print("\n[USERS]")

print(f"Total Users: {len(users):,}")

print("\nCountry Distribution (%)")
print(
    round(
        users["country"]
        .value_counts(normalize=True)
        .mul(100),
        2
    )
)

print("\nAcquisition Channel Distribution (%)")
print(
    round(
        users["acquisition_channel"]
        .value_counts(normalize=True)
        .mul(100),
        2
    )
)

# --------------------------------------------------
# TRIALS
# --------------------------------------------------

print("\n[TRIALS]")

total_trials = len(trials)

converted_trials = len(
    trials[
        trials["converted_to_paid"] == "Yes"
    ]
)

conversion_rate = (
    converted_trials / total_trials
) * 100

print(f"Total Trials: {total_trials:,}")
print(f"Converted Trials: {converted_trials:,}")
print(f"Conversion Rate: {conversion_rate:.2f}%")

# --------------------------------------------------
# SUBSCRIPTIONS
# --------------------------------------------------

print("\n[SUBSCRIPTIONS]")

print(f"Total Subscriptions: {len(subscriptions):,}")

print("\nPlan Distribution (%)")
print(
    round(
        subscriptions["plan_type"]
        .value_counts(normalize=True)
        .mul(100),
        2
    )
)

print("\nSubscription Status (%)")
print(
    round(
        subscriptions["subscription_status"]
        .value_counts(normalize=True)
        .mul(100),
        2
    )
)

print("\nEstimated Monthly Revenue")

revenue = subscriptions["monthly_revenue"].sum()

print(f"MRR: ₹{revenue:,.0f}")

# --------------------------------------------------
# EVENTS
# --------------------------------------------------

print("\n[EVENTS]")

print(f"Total Events: {len(events):,}")

print("\nEvent Type Distribution (%)")
print(
    round(
        events["event_type"]
        .value_counts(normalize=True)
        .mul(100),
        2
    )
)

events["event_date"] = pd.to_datetime(
    events["event_date"]
)

print("\nEvent Date Range")

print(
    f"Start: {events['event_date'].min().date()}"
)

print(
    f"End  : {events['event_date'].max().date()}"
)

# --------------------------------------------------
# DATA QUALITY CHECKS
# --------------------------------------------------

print("\n[DATA QUALITY CHECKS]")

future_events = len(
    events[
        events["event_date"] >
        pd.Timestamp("2025-12-31")
    ]
)

print(
    f"Events beyond project timeline: {future_events:,}"
)

if future_events > 0:
    print(
        "WARNING: Events found beyond Dec-2025"
    )

print("\nValidation Complete")
print("=" * 60)