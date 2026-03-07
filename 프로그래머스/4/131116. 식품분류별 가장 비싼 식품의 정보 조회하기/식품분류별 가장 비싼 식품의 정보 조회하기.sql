WITH PRICE_RANK AS (
    SELECT
        product_id,
        RANK() OVER (PARTITION BY category ORDER BY price DESC) rn
    FROM
        food_product
)

SELECT
    f.category,
    f.price AS max_price,
    f.product_name
FROM
    food_product f
JOIN
    price_rank p ON f.product_id = p.product_id
WHERE
    p.rn = 1
        AND f.category IN ('과자', '국', '김치', '식용유')
GROUP BY
    f.price
ORDER BY
    f.price DESC
    

    