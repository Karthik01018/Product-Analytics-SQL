# Data Dictionary

This document describes the datasets used in the InsightFlow Analytics project.

---

## users

Stores information about users who signed up for the platform.

| Column Name         | Description                                          |
| ------------------- | ---------------------------------------------------- |
| user_id             | Unique identifier for each user                      |
| user_name           | User name                                            |
| age                 | Age of the user                                      |
| signup_date         | Date the user registered                             |
| country             | User's country                                       |
| industry            | Industry the user belongs to                         |
| company_size        | Company size category                                |
| acquisition_channel | Source through which the user discovered InsightFlow |

---

## subscriptions

Stores subscription information for paying and non-paying users.

| Column Name             | Description                    |
| ----------------------- | ------------------------------ |
| subscription_id         | Unique subscription identifier |
| user_id                 | Reference to the user          |
| plan_type               | Subscription plan              |
| subscription_start_date | Subscription start date        |
| subscription_end_date   | Subscription end date          |
| monthly_revenue         | Monthly recurring revenue      |
| subscription_status     | Current subscription status    |
| billing_cycle           | Monthly or annual billing      |

---

## events

Stores user activity and product engagement events.

| Column Name              | Description                           |
| ------------------------ | ------------------------------------- |
| event_id                 | Unique event identifier               |
| user_id                  | Reference to the user                 |
| event_date               | Date of the event                     |
| event_type               | Type of user action                   |
| feature_name             | Product feature involved in the event |
| session_duration_minutes | Session duration in minutes           |
| device_type              | Desktop, mobile, or tablet            |
| event_source             | Platform used for the event           |

---

## trials

Stores information about free trials and trial conversions.

| Column Name       | Description                           |
| ----------------- | ------------------------------------- |
| trial_id          | Unique trial identifier               |
| user_id           | Reference to the user                 |
| trial_start_date  | Trial start date                      |
| trial_end_date    | Trial end date                        |
| trial_status      | Active, completed, or expired         |
| converted_to_paid | Indicates whether the trial converted |
| days_to_convert   | Number of days taken to convert       |
