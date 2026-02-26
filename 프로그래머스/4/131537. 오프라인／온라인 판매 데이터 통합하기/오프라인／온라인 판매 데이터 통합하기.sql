WITH online_sale_on_march AS (
    SELECT
        date_format(sales_date, '%Y-%m-%d') AS sales_date,
        product_id,
        user_id,
        sales_amount
    FROM
        online_sale
    WHERE
        sales_date LIKE '2022-03%'
),
offline_sale_on_march AS (
    SELECT
        date_format(sales_date, '%Y-%m-%d') AS sales_date,
        product_id,
        NULL AS user_id,
        sales_amount
    FROM
        offline_sale
    WHERE
        sales_date LIKE '2022-03%'
)

SELECT
    *
FROM
    online_sale_on_march
UNION ALL
SELECT
    *
FROM
    offline_sale_on_march
ORDER BY
    sales_date ASC,
    product_id ASC,
    user_id ASC
