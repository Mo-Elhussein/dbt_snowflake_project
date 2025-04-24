select
    order_date, 
    O.order_id,
    sum(total_price) AS total_price  
from 
    finance_db.raw.stg_orders O 
LEFT JOIN finance_db.raw.stg_product_items OI
ON O.ORDER_ID=OI.ORDER_ID
GROUP BY 1,2