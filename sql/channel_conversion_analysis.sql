-- ============================================
-- CHANNEL CONVERSION ANALYSIS
-- ============================================

SELECT
    u.acquisition_channel,

    COUNT(DISTINCT u.user_id) AS total_users,

    COUNT(DISTINCT t.user_id) AS trial_users,

    COUNT(DISTINCT s.user_id) AS paid_users,

    ROUND(
        COUNT(DISTINCT t.user_id) * 100.0
        / COUNT(DISTINCT u.user_id),
        2
    ) AS trial_conversion_pct,

    ROUND(
        COUNT(DISTINCT s.user_id) * 100.0
        / COUNT(DISTINCT u.user_id),
        2
    ) AS paid_conversion_pct

FROM users u

LEFT JOIN trials t
ON u.user_id = t.user_id

LEFT JOIN subscriptions s
ON u.user_id = s.user_id

GROUP BY u.acquisition_channel

ORDER BY paid_conversion_pct DESC;