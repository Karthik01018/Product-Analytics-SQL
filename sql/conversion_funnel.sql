-- ============================================
-- CONVERSION FUNNEL
-- ============================================

SELECT
    'Users' AS stage,
    COUNT(DISTINCT user_id) AS users
FROM users

UNION ALL

SELECT
    'Trials',
    COUNT(DISTINCT user_id)
FROM trials

UNION ALL

SELECT
    'Paid Subscribers',
    COUNT(DISTINCT user_id)
FROM subscriptions;