WITH MAX_FAVORITES AS (
    SELECT
        food_type,
        MAX(favorites) AS favorites
    FROM
        rest_info
    GROUP BY
        food_type
)

SELECT
    i.food_type,
    i.rest_id,
    i.rest_name,
    f.favorites
FROM
    rest_info i
JOIN
    max_favorites f ON i.food_type = f.food_type AND i.favorites = f.favorites
ORDER BY
    food_type DESC