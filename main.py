# No:1
# select to_char(d.order_date, 'YYYY-MM'),count(p.product_id) as sotilganlar from products p
# inner join categories c on(p.category_id=c.category_id)
# inner join order_details o on(p.product_id=o.product_id)
# inner join orders d on(o.order_id=d.order_id)
# where to_char(order_date, 'YYYY')='1996' and p.category_id=1
# group by to_char(d.order_date, 'YYYY-MM')

# No:2
# select e.last_name,e.first_name,p.product_name,p.unit_price
# from products p
# inner join order_details o on(p.product_id=o.product_id)
# inner join orders d on(o.order_id=d.order_id)
# inner join employees e on(d.employee_id=e.employee_id)
# where to_char(d.order_date, 'YYYY-MM')='1997-07' and p.category_id=3
# ORDER BY p.unit_price ASC
# LIMIT 1;

# No:3
# select to_char(o.order_date, 'YYYY-MM'),e.last_name,e.first_name,c.company_name
# from orders o
# inner join customers c on(o.customer_id=c.customer_id)
# inner join employees e on(o.employee_id=e.employee_id)
# where to_char(o.order_date, 'YYYY-MM')='1998-03'
# group by to_char(o.order_date, 'YYYY-MM'),e.last_name,e.first_name,c.company_name

# No:4
# select to_char(o.order_date, 'YYYY-MM'),d.unit_price,p.product_name
# from products p
# inner join order_details d on(p.product_id=d.product_id)
# inner join orders o on(o.order_id=d.order_id)
# where to_char(o.order_date, 'YYYY')='1996'
# group by to_char(o.order_date, 'YYYY-MM'),d.unit_price,p.product_name
# order by d.unit_price desc
# limit 1;

# No:5
# select to_char(order_date, 'YYYY-MM'),c.contact_name as customer,c.country,e.first_name as supplier,e.country
# from orders o
# inner join customers c on(o.customer_id=c.customer_id)
# inner join employees e on(o.employee_id=e.employee_id)
# where to_char(o.order_date, 'YYYY')='1996' and c.country='USA' and e.country='USA'
# group by to_char(o.order_date, 'YYYY-MM'),c.contact_name,c.country,e.first_name,e.country

# No:6
# select to_char(order_date, 'YYYY-MM'),e.first_name as supplier,p.product_name
# from products p
# inner join categories c on(c.category_id=p.category_id)
# inner join order_details d on(d.product_id=p.product_id)
# inner join orders o on(o.order_id=d.order_id)
# inner join employees e on(e.employee_id=o.employee_id)
# where to_char(order_date, 'YYYY')='1997' and c.category_id=5
# group by to_char(order_date, 'YYYY-MM'),e.first_name,p.product_name

# No:7
# select o.ship_country,to_char(order_date, 'YYYY-MM'),count(o.order_id)
# from orders o
# where to_char(order_date, 'YYYY')='1997' and o.ship_country='USA'
# group by o.ship_country,to_char(order_date, 'YYYY-MM')