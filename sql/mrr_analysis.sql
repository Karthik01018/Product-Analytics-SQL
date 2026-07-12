-- ============================================
-- MONTHLY RECURRING REVENUE (MRR)
-- ============================================

SELECT
    plan_type,

    COUNT(*) AS customers,

    SUM(monthly_revenue) AS total_mrr,

    ROUND(
        AVG(monthly_revenue),
        2
    ) AS avg_revenue_per_customer

FROM subscriptions

WHERE subscription_status = 'Active'

GROUP BY plan_type

ORDER BY total_mrr DESC;