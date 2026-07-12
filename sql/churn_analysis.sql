-- ============================================
-- CHURN ANALYSIS
-- ============================================

SELECT

    subscription_status,

    COUNT(*) AS customers,

    ROUND(
        COUNT(*) * 100.0
        /
        SUM(COUNT(*)) OVER (),
        2
    ) AS percentage

FROM subscriptions

GROUP BY subscription_status;