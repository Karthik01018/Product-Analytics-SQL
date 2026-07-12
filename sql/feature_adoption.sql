-- ============================================
-- FEATURE ADOPTION ANALYSIS
-- ============================================

SELECT
    feature_name,

    COUNT(*) AS total_events,

    COUNT(DISTINCT user_id) AS unique_users,

    ROUND(
        COUNT(*) * 1.0 /
        COUNT(DISTINCT user_id),
        2
    ) AS avg_events_per_user

FROM events

GROUP BY feature_name

ORDER BY total_events DESC;