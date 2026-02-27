-- 코드를 입력하세요
SELECT a.category, m.price, a.product_name
FROM FOOD_PRODUCT a
join (select CATEGORY , MAX(PRICE) AS PRICE
from FOOD_PRODUCT 
GROUP BY CATEGORY) m on a.price = m.price and a.category = m.category
HAVING a.CATEGORY IN('과자', '국','김치','식용유')
ORDER BY a.PRICE DESC