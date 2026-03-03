WITH OVER_FIVE_RENTAL AS (
    SELECT
        car_id
    FROM
        car_rental_company_rental_history
    WHERE
        start_date BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY
        car_id
    HAVING
        COUNT(*) >= 5
)

SELECT
    MONTH(h.start_date) AS month,
    h.car_id,
    COUNT(*) AS records
FROM
    car_rental_company_rental_history h
JOIN
    over_five_rental o ON h.car_id = o.car_id
WHERE
    h.start_date BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY
    month,
    car_id
HAVING
    records > 0
ORDER BY
    month ASC,
    car_id DESC