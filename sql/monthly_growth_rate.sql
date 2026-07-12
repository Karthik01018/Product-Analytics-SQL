-- ============================================
-- MONTHLY USER GROWTH RATE
-- ============================================

WITH monthly_users AS (

    SELECT
        DATE_TRUNC('month', signup_date) AS signup_month,
        COUNT(*) AS new_users
    FROM users
    GROUP BY 1

)

SELECT
    signup_month,
    new_users,

    LAG(new_users) OVER (
        ORDER BY signup_month
    ) AS previous_month,

    ROUND(
        (
            (new_users - LAG(new_users) OVER (
                ORDER BY signup_month
            ))::numeric
            /
            NULLIF(
                LAG(new_users) OVER (
                    ORDER BY signup_month
                ),
                0
            )
        ) * 100,
        2
    ) AS growth_rate_pct

FROM monthly_users
ORDER BY signup_month;