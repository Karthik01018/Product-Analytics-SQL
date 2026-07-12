# Product Analytics using SQL & PostgreSQL

## Project Overview

InsightFlow is an end-to-end Product Analytics project designed to simulate real-world business scenarios faced by Product Analysts, Data Analysts, and Growth Analysts.

The project models the customer lifecycle from user acquisition to trial conversion, subscription revenue, feature adoption, and customer churn. A synthetic SaaS dataset was generated and stored in PostgreSQL to perform business-focused SQL analysis and derive actionable insights.

Unlike traditional SQL portfolio projects that focus only on queries, this project follows a complete analytics workflow including data generation, validation, database modeling, KPI analysis, and business recommendations.

---

## Business Problem

A SaaS company wants to understand:

* How users are acquired
* Which acquisition channels perform best
* How effectively users convert from trial to paid subscriptions
* Which product features drive engagement
* How much recurring revenue is generated
* What percentage of customers churn
* Whether AI-powered features improve customer conversion

The goal is to support product, marketing, and revenue teams with data-driven decision making.

---

## Business Questions

### User Growth

* How many users sign up each month?
* What is the month-over-month growth rate?

### Acquisition Analysis

* Which acquisition channels generate the most users?
* Which channels produce the highest paid conversion rate?

### Conversion Funnel

* How many users start a trial?
* How many become paying customers?

### Revenue Analytics

* What is the Monthly Recurring Revenue (MRR)?
* Which subscription plans contribute most revenue?

### Product Analytics

* Which features are most frequently used?
* How many users adopt AI-powered functionality?

### Customer Retention

* What is the churn rate?
* How many subscriptions remain active?

---

## Dataset Overview

### Users

Contains customer demographics and acquisition information.

| Column              |
| ------------------- |
| user_id             |
| user_name           |
| age                 |
| signup_date         |
| country             |
| industry            |
| company_size        |
| acquisition_channel |

### Trials

Contains free trial activity.

| Column            |
| ----------------- |
| trial_id          |
| user_id           |
| trial_start_date  |
| trial_end_date    |
| trial_status      |
| converted_to_paid |
| days_to_convert   |

### Subscriptions

Contains customer subscription and revenue data.

| Column                  |
| ----------------------- |
| subscription_id         |
| user_id                 |
| plan_type               |
| subscription_start_date |
| subscription_end_date   |
| monthly_revenue         |
| subscription_status     |
| billing_cycle           |

### Events

Contains user activity and product engagement events.

| Column                   |
| ------------------------ |
| event_id                 |
| user_id                  |
| event_date               |
| event_type               |
| feature_name             |
| session_duration_minutes |
| device_type              |
| event_source             |

---

## Dataset Statistics

| Metric               | Value  |
| -------------------- | ------ |
| Users                | 5,000  |
| Trial Users          | 3,250  |
| Paid Subscribers     | 620    |
| Events               | 75,000 |
| Countries            | 6      |
| Acquisition Channels | 6      |
| Subscription Plans   | 3      |

---

## Technology Stack

* PostgreSQL
* SQL
* Python
* Pandas
* Faker
* Git
* GitHub

---

## Project Structure

```text
SQL-Analytics-Playground

├── README.md

├── data
│   └── raw

├── docs
│   ├── business_overview.md
│   ├── business_assumptions.md
│   ├── data_dictionary.md
│   └── kpi_definitions.md

├── scripts
│   ├── generate_users.py
│   ├── generate_trials.py
│   ├── generate_subscriptions.py
│   ├── generate_events.py
│   ├── validate_data.py
│   └── fix_trials.py

├── database
│   └── schema
│       └── schema.sql

└── sql
    ├── monthly_growth_rate.sql
    ├── acquisition_analysis.sql
    ├── channel_conversion_analysis.sql
    ├── conversion_funnel.sql
    ├── mrr_analysis.sql
    ├── feature_adoption.sql
    ├── ai_adoption_impact.sql
    └── churn_analysis.sql
```

---

## Key Insights

### Acquisition

Google Search generated the largest share of users (30.76%), while LinkedIn and Referral channels produced the highest paid conversion rates.

### Conversion Funnel

65% of users started a trial and 19.08% of trial users converted into paid subscribers.

### Revenue

Enterprise customers contributed the highest Monthly Recurring Revenue despite representing a smaller portion of the customer base.

### Product Usage

Task Manager was the most adopted feature, while AI Assistant achieved strong adoption across the user base.

### Churn

85.81% of subscriptions remained active, resulting in a churn rate of 14.19%.

---

## Future Enhancements

* Power BI Executive Dashboard
* Cohort Retention Analysis
* Customer Lifetime Value (CLV)
* Revenue Forecasting
* A/B Testing Simulation
* Product Usage Segmentation

---

## Author

**Kartik Beelagi**
Data Analytics | Product Analytics | SQL | PostgreSQL | Python
GitHub: https://github.com/Karthik01018
