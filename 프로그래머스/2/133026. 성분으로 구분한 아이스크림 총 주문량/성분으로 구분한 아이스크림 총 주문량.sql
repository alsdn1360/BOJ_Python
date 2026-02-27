SELECT
    i.ingredient_type,
    SUM(f.total_order) as total_order
FROM
    icecream_info i
JOIN
    first_half f ON i.flavor = f.flavor
GROUP BY
    i.ingredient_type
ORDER BY
    total_order ASC
    