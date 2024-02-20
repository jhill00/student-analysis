SELECT
    school_name,
    stdent_last_name,
    student_first_name,
    student_id,
    grade,
    lnf,
    psf,
    nwf-cls,
    nwf-wrc,
    wrf,
    orf,
    orf-accu
FROM
    filtered_df AS fd
LEFT JOIN
    student_information AS si ON si.sis_id = fd.student_id
;