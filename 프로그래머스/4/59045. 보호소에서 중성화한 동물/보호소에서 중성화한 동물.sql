WITH INTACT_ANIMAL_WHEN_INS AS (
    SELECT
        *
    FROM
        animal_ins
    WHERE
        sex_upon_intake LIKE 'Intact%'
)

SELECT
    o.animal_id,
    o.animal_type,
    o.name
FROM
    animal_outs o
JOIN
    intact_animal_when_ins i ON o.animal_id = i.animal_id
WHERE
    o.sex_upon_outcome LIKE 'Spayed%'
        OR o.sex_upon_outcome LIKE 'Neutered%'
ORDER BY
    o.animal_id ASC
    