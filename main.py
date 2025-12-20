# NO:1
# select to_char(order_date, 'YYYY-MM'),p.product_name,s.company_name
# from products p
# inner join suppliers s on s.supplier_id=p.supplier_id
# inner join order_details d on d.product_id=p.product_id
# inner join orders o on o.order_id=d.order_id
# where to_char(order_date, 'YYYY-MM')='1996-07'
# group by to_char(order_date, 'YYYY-MM'),p.product_name,s.company_name
#
# No:2
# select c.city,c.contact_name,e.first_name
# from orders o
# inner join customers c on c.customer_id=o.customer_id
# inner join employees e on e.employee_id=o.employee_id
# where e.city=c.city
# group by c.city,c.contact_name,e.first_name
#
# No:3
# select
# 	extract(year from o.order_date) as year,
# 	p.product_name,
# 	c.company_name,
# 	count(*) as jami
# from products p
# inner join order_details d ON p.product_id = d.product_id
# inner join orders o ON o.order_id = d.order_id
# inner join customers c ON c.customer_id = o.customer_id
# where extract(year from o.order_date)=(
# 	select extract(year from o2.order_date)
# 	from orders o2
# 	group by extract(year from o2.order_date)
# 	order by count(*) desc
# 	limit 1
# )
# group by year,p.product_name,c.company_name
# order by jami desc
# limit 1;
#
# No:4
# select p.product_name,c.company_name,count(*) as jami
# from products p
# inner join order_details d ON p.product_id = d.product_id
# inner join orders o ON o.order_id = d.order_id
# inner join customers c ON c.customer_id = o.customer_id
# group by p.product_name,c.company_name
# order by jami desc
# limit 1;
#
# No:5
# select e.first_name,e.last_name,birth_date, count(o.order_id) as foalik
# from orders o
# inner join employees e on o.employee_id=e.employee_id
# where e.country='USA'
# group by e.first_name,e.last_name,birth_date
# order by foalik desc
#
# No:6
# select e.country,e.first_name,e.last_name, count(o.order_id) as foalik
# from orders o
# inner join employees e on o.employee_id=e.employee_id
# group by e.country,e.first_name,e.last_name
# order by foalik desc
#
# No:8
# select c.contact_name,p.product_name,p.unit_price as money
# from products p
# inner join order_details d on d.product_id=p.product_id
# inner join orders o on o.order_id=d.order_id
# inner join customers c on c.customer_id=o.customer_id
# where extract(year from o.order_date)=1997
#   and p.unit_price=(
# 		select max(p2.unit_price)
# 		from products p2
# 		INNER JOIN order_details d2 ON d2.product_id = p2.product_id
#         INNER JOIN orders o2 ON o2.order_id = d2.order_id
# 		where extract(year from o2.order_date)=1997
#   );
#
# No:9
# select p.product_name, count(d.quantity) as jami
# from products p
# inner join order_details d on d.product_id=p.product_id
# group by p.product_name
# having count(*)=(
# 	select min(cnt)
# 	from (
#         select count(*) as cnt
#         from order_details
#         group by product_id
# 	) t
# );
#
# No:10
# select
#     p.product_name,
#     c.contact_name as customer,
#     s.company_name as supplier,
#     sum(d.unit_price * d.quantity) as total_amount
# from products p
# join suppliers s on s.supplier_id = p.supplier_id
# join order_details d on d.product_id = p.product_id
# join orders o on o.order_id = d.order_id
# join customers c on c.customer_id = o.customer_id
# group by
#     p.product_name,
#     c.contact_name,
#     s.company_name
# order by total_amount desc
# limit 10;

