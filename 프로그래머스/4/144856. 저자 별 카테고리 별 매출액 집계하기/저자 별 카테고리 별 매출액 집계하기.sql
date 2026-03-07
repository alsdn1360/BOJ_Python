WITH BOOK_SALES_2022_01 AS (
    SELECT
        book_id,
        SUM(sales) AS sales
    FROM
        book_sales
    WHERE
        sales_date LIKE '2022-01%'
    GROUP BY
        book_id
)

SELECT
    a.author_id,
    a.author_name,
    b.category,
    SUM(b.price * s.sales) AS total_sales
FROM
    author a
JOIN
    book b ON a.author_id = b.author_id
JOIN
    book_sales_2022_01 s ON b.book_id = s.book_id
GROUP BY
    a.author_id,
    a.author_name,
    b.category
ORDER BY
    a.author_id ASC,
    b.category DESC

    