WITH TRUCK_INFO AS (
    SELECT
        car_id,
        car_type,
        daily_fee
    FROM
        car_rental_company_car
    WHERE
        car_type = '트럭'
),
CAR_RENTAL_TOTAL_DAYS AS (
    SELECT
        history_id,
        car_id,
        DATEDIFF(end_date, start_date) + 1 AS rental_days,
        CASE
            WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN '90일 이상'
            WHEN DATEDIFF(end_date, start_date) + 1 >= 30 THEN '30일 이상'
            WHEN DATEDIFF(end_date, start_date) + 1 >= 7 THEN '7일 이상'
            ELSE ''
        END AS duration_type
    FROM
        car_rental_company_rental_history
)

SELECT
    d.history_id,
    FLOOR((d.rental_days * t.daily_fee) * ((100 - IFNULL(p.discount_rate, 0)) / 100)) AS fee
FROM
    car_rental_total_days d
JOIN
    truck_info t ON d.car_id = t.car_id
LEFT JOIN
    car_rental_company_discount_plan p ON t.car_type = p.car_type AND d.duration_type = p.duration_type
ORDER BY
    fee DESC,
    d.history_id DESC