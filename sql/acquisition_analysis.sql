-- ============================================
-- ACQUISITION CHANNEL PERFORMANCE
-- ============================================

SELECT
    acquisition_channel,
    COUNT(*) AS total_users,

    ROUND(
        COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER (),
        2
    ) AS user_percentage

FROM users

GROUP BY acquisition_channel

ORDER BY total_users DESC;