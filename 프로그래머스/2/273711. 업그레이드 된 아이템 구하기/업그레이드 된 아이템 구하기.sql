WITH upgradable_rare_item AS (
    SELECT
        t.item_id
    FROM
        item_info i
    JOIN
        item_tree t
            ON i.item_id = t.parent_item_id
    WHERE
        i.rarity = 'RARE'
)

SELECT
    u.item_id,
    i.item_name,
    i.rarity
FROM 
    upgradable_rare_item u
LEFT JOIN
    item_info i
        ON u.item_id = i.item_id
ORDER BY
    u.item_id DESC
