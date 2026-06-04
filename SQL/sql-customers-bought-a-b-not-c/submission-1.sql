select c.customer_id, c.customer_name
from customers c
inner join
orders o on o.customer_id = c.customer_id
group by c.customer_id, c.customer_name
having
SUM(case when o.product_name = 'A' THEN 1 else 0 end) > 0
and SUM(case when o.product_name = 'B' THEN 1 else 0 end) > 0
and SUM(case when o.product_name = 'C' THEN 1 else 0 end) = 0
order by c.customer_name;