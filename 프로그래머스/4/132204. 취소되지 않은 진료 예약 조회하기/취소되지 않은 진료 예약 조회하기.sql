WITH CS_NOT_CANCELED_APPOINTMENT AS (
    SELECT
        apnt_no,
        pt_no,
        mcdp_cd,
        apnt_ymd,
        mddr_id
    FROM
        appointment
    WHERE
        (apnt_ymd BETWEEN '2022-04-13 00:00:00' AND '2022-04-13 23:59:59') AND (apnt_cncl_yn = 'N') AND (mcdp_cd = 'CS')
)

SELECT
    a.apnt_no,
    p.pt_name,
    p.pt_no,
    a.mcdp_cd,
    d.dr_name,
    a.apnt_ymd
FROM
    cs_not_canceled_appointment a
JOIN
    patient p ON a.pt_no = p.pt_no
JOIN
    doctor d ON a.mddr_id = d.dr_id
ORDER BY
    a.apnt_ymd ASC