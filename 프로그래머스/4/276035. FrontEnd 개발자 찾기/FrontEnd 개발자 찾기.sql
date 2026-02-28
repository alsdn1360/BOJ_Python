WITH FRONTEND AS (
    SELECT
        code
    FROM
        skillcodes
    WHERE
        category = 'Front End'
)

SELECT
    DISTINCT d.id,
    d.email,
    d.first_name,
    d.last_name
FROM
    developers d
JOIN
    frontend f ON (d.skill_code & f.code) > 0
ORDER BY
    d.id
    