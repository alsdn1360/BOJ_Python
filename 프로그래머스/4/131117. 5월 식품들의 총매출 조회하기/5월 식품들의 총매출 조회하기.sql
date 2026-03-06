WITH FILTERED_FOOD_ORDER AS (
    SELECT
        *
    FROM
        food_order
    WHERE
        produce_date BETWEEN '2022-05-01' AND '2022-05-31'
)


SELECT
    p.product_id,
    p.product_name,
    (p.price * SUM(o.amount)) AS total_sales
FROM
    food_product p
JOIN
    filtered_food_order o ON p.product_id = o.product_id
GROUP BY
    o.product_id
ORDER BY
    total_sales DESC,
    p.product_id ASC

    