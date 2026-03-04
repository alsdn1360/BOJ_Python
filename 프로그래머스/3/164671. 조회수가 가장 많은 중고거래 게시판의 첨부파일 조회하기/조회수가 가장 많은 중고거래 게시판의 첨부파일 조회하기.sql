WITH MAX_VIEWS_BOARD AS (
    SELECT
        board_id
    FROM
        used_goods_board
    ORDER BY
        views DESC
    LIMIT
        1
)

SELECT
    CONCAT('/home/grep/src/', f.board_id, '/', f.file_id, f.file_name, f.file_ext) AS file_path
FROM
    used_goods_file f
JOIN
    max_views_board m ON f.board_id = m.board_id
ORDER BY
    f.file_id DESC