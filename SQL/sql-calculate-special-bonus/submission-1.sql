select employee_id,
CASE
    when name not like 'M%' and (employee_id % 2) != 0 THEN employees.salary
    else 0
    end as bonus
from employees
order by employee_id;