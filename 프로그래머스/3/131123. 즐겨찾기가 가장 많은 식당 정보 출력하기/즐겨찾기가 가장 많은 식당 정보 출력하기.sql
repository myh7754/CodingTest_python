-- 코드를 입력하세요
select a.food_type , a.rest_id, a.rest_name, m.favorites
from rest_info a
join 
(SELECT food_type,max(favorites) as favorites
from rest_info
group by FOOD_TYPE) m on a.food_type = m.food_type and a.favorites = m.favorites
order by a.food_type desc
