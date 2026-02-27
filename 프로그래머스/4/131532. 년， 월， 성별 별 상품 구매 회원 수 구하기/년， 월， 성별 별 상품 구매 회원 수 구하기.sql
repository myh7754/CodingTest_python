-- 코드를 입력하세요 year, month, gender, users
select 
    YEAR(a.sales_date) as year, 
    MONTH(a.sales_date) as month, 
    (b.gender) as gender,
    COUNT(DISTINCT b.user_id) as users
from online_sale a
join user_info b on a.user_id = b.user_id
where b.gender is not null
group by YEAR(a.sales_date), month(a.sales_date),b.gender
order by year asc, month asc, gender asc

