WITH JOINED_2021_USER AS (
    SELECT
        user_id
    FROM
        user_info
    WHERE
        joined BETWEEN '2021-01-01' AND '2021-12-31'
), JOINED_2021_USER_CNT AS (
    SELECT
        COUNT(*) AS total_cnt
    FROM
        joined_2021_user
)

SELECT
    YEAR(o.sales_date) AS year,
    MONTH(o.sales_date) AS month,
    COUNT(DISTINCT(o.user_id)) AS purchased_users,
    ROUND(COUNT(DISTINCT(o.user_id)) / (SELECT total_cnt FROM joined_2021_user_cnt), 1) AS puchased_ratio
FROM
    online_sale o
JOIN
    joined_2021_user i ON o.user_id = i.user_id
GROUP BY
    year,
    month
ORDER BY
    year ASC,
    month ASC
