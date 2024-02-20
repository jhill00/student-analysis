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
    mapped_test_results
WHERE
    grade = 'Grade 1'
;