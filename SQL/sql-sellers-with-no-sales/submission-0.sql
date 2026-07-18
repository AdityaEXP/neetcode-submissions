-- Write your query below
select s.seller_name
from seller s
where seller_id not in (select seller_id from orders where EXTRACT(YEAR FROM sale_date) = 2020)
group by s.seller_name