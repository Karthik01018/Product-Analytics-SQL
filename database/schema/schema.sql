-- USERS TABLE

CREATE TABLE users (
    user_id VARCHAR(10) PRIMARY KEY,
    user_name VARCHAR(100),
    age INT,
    signup_date DATE,
    country VARCHAR(50),
    industry VARCHAR(50),
    company_size VARCHAR(20),
    acquisition_channel VARCHAR(50)
);

-- TRIALS TABLE

CREATE TABLE trials (
    trial_id VARCHAR(10) PRIMARY KEY,
    user_id VARCHAR(10),
    trial_start_date DATE,
    trial_end_date DATE,
    trial_status VARCHAR(20),
    converted_to_paid VARCHAR(5),
    days_to_convert INT,

    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);

-- SUBSCRIPTIONS TABLE

CREATE TABLE subscriptions (
    subscription_id VARCHAR(10) PRIMARY KEY,
    user_id VARCHAR(10),
    plan_type VARCHAR(20),
    subscription_start_date DATE,
    subscription_end_date DATE,
    monthly_revenue NUMERIC(10,2),
    subscription_status VARCHAR(20),
    billing_cycle VARCHAR(20),

    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);

-- EVENTS TABLE

CREATE TABLE events (
    event_id VARCHAR(10) PRIMARY KEY,
    user_id VARCHAR(10),
    event_date DATE,
    event_type VARCHAR(50),
    feature_name VARCHAR(50),
    session_duration_minutes INT,
    device_type VARCHAR(20),
    event_source VARCHAR(20),

    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);