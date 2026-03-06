WITH TOP_REVIEWER AS (  
    SELECT
        member_id
    FROM
        rest_review
    GROUP BY
        member_id
    ORDER BY
        COUNT(*) DESC
    LIMIT
        1
)


SELECT
    p.member_name,
    r.review_text,
    DATE_FORMAT(r.review_date, '%Y-%m-%d') AS review_date
FROM
    rest_review r
JOIN
    member_profile p ON r.member_id = p.member_id
WHERE
    r.member_id = (SELECT * FROM TOP_REVIEWER)
ORDER BY
    review_date ASC,
    r.review_text ASC

    