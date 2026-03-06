WITH FILTERED_CAR_TYPE AS (
    SELECT
        *
    FROM
        car_rental_company_car
    WHERE
        car_type = '세단' OR car_type = 'SUV'
),
UNAVAILABLE_FOR_RENT AS (
    SELECT
        car_id
    FROM
        car_rental_company_rental_history
    WHERE
        start_date <= '2022-11-30' AND end_date >= '2022-11-01'
),
FEE_FOR_RENT AS (
    SELECT
        f.car_id,
        f.car_type,
        FLOOR((f.daily_fee * ((100 - IFNULL(p.discount_rate, 0)) / 100))) * 30 AS fee   
    FROM
        filtered_car_type f
    JOIN
        car_rental_company_discount_plan p ON f.car_type = p.car_type AND p.duration_type = '30일 이상'
    WHERE
        f.car_id NOT IN (SELECT * FROM unavailable_for_rent)
)

SELECT
    *
FROM
    fee_for_rent
WHERE
    fee BETWEEN 500000 AND 1999999
ORDER BY
    fee DESC,
    car_type ASC,
    car_id DESC
    