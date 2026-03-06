WITH FIRST_HALF_ORDER AS (
    SELECT
        shipment_id,
        flavor,
        SUM(total_order) AS total_order
    FROM
        first_half
    GROUP BY
        flavor
),
JULY_ORDER AS (
    SELECT
        shipment_id,
        flavor,
        SUM(total_order) AS total_order
    FROM
        july
    GROUP BY
        flavor
)

SELECT
    f.flavor
FROM
    first_half_order f
JOIN
    july_order j ON f.flavor = j.flavor
ORDER BY
    (f.total_order + j.total_order) DESC
LIMIT
    3