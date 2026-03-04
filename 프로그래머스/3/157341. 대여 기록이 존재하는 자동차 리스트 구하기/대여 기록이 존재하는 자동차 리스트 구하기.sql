WITH RENTAL_ON_OCTOBER AS (
    SELECT
        car_id
    FROM
        car_rental_company_rental_history
    WHERE
        start_date LIKE '2022-10%'
)


SELECT
    c.car_id
FROM
    car_rental_company_car c
JOIN
    rental_on_october r ON c.car_id = r.car_id
WHERE
    c.car_type = '세단'
GROUP BY
    c.car_id
ORDER BY
    c.car_id DESC