-- ============================================
-- USER GROWTH ANALYSIS
-- ============================================

SELECT
    DATE_TRUNC('month', signup_date) AS signup_month,
    COUNT(*) AS new_users
FROM users
GROUP BY 1
ORDER BY 1;