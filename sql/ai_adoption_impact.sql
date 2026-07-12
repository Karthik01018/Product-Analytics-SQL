-- ============================================
-- AI FEATURE IMPACT ON CONVERSION
-- ============================================

WITH ai_users AS (

    SELECT DISTINCT user_id

    FROM events

    WHERE feature_name = 'AI Assistant'

)

SELECT

    CASE
        WHEN a.user_id IS NOT NULL
        THEN 'AI Users'
        ELSE 'Non-AI Users'
    END AS user_segment,

    COUNT(DISTINCT u.user_id) AS total_users,

    COUNT(DISTINCT s.user_id) AS paid_users,

    ROUND(
        COUNT(DISTINCT s.user_id) * 100.0
        /
        COUNT(DISTINCT u.user_id),
        2
    ) AS paid_conversion_pct

FROM users u

LEFT JOIN ai_users a
ON u.user_id = a.user_id

LEFT JOIN subscriptions s
ON u.user_id = s.user_id

GROUP BY 1

ORDER BY paid_conversion_pct DESC;