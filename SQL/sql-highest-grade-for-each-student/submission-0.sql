-- Write your query below
select s.student_id, 
    (select exam_id from exam_results 
    where student_id = s.student_id 
    order by score desc, exam_id asc limit 1) as exam_id,
    max(s.score) as score

from exam_results s
group by s.student_id