use ecomm;
select churn, count(*) as total_customers
from customer_churn
group by Churn;
select avg(tenure) as average_tenure,sum(cashbackamount)as total_cashback
from customer_churn
where Churn=1;
select
(sum(case when churn=1 and complain=1 then 1 else 0 end)*100.0)/
sum(case when churn=1 then 1 else 0 end)as percentage_churned_complained 
from customer_churn;
select citytier,count(*) as churned_customer_count
from customer_churn
where Churn =1 and PreferedOrderCat ='Laptop&Accessory'
group by CityTier
order by churned_customer_count desc
limit 1;
select preferredpaymentmode,count(*)as active_customer_count
from customer_churn
where Churn =0
group by PreferredPaymentMode
order by active_customer_count desc
limit 1;
select sum(orderamounthikefromlastyear) as total_order_amount_hike
from customer_churn
where MaritalStatus='Single' and PreferredLoginDevice ='Mobile phone';
select avg(numberofdeviceRegistered)as avg_devices_registered
from customer_churn
where PreferredPaymentMode ='UPI';
select Citytier,count(*) as customer_count
from customer_churn
group by CityTier
order by customer_count desc
limit 1;
select gender,sum(couponUsed) as total_coupons_used
from customer_churn
group by Gender
order by total_coupons_used desc
limit 1;
select preferedOrderCat,count(*)as total_customers,max(hourspendonapp)as max_hours_spent
from customer_churn
group by PreferedOrderCat;
select sum(ordercount) as total_order_count
from customer_churn
where PreferredPaymentMode ='Credit Card'
and SatisfactionScore =(select max(SatisfactionScore)from customer_churn);
select avg(SatisfactionScore) as avg_satisfaction_score
from customer_churn
where Complain =1;
select churn,avg(warehouseTohome) as avg_warehose_to_home
from customer_churn
group by Churn;
select warehouseTohome,count(*) as frequency
from customer_churn
group by WarehouseToHome
order by frequency desc 
limit 1;
select preferredPaymentmode,avg(cashbackamount) as avg_cashback
from customer_churn
group by PreferredPaymentMode;
select avg(daysincelastorder) as avg_since_last_order
from customer_churn
where Churn =1;
select churn,avg(tenure) as avg_tenure
from customer_churn
group by Churn;
select citytier,count(*) as complaint_count
from customer_churn
where Complain =1
group by CityTier
order by complaint_count desc
limit 1;
select preferedordercat,count(*)as customer_count
from customer_churn
where CouponUsed>5
group by PreferedOrderCat;
select preferedordercat,avg(cashbackamount)as avg_cashback
from customer_churn
group by PreferedOrderCat
order by avg_cashback desc
limit 3;
select preferredpaymentmode
from customer_churn
group by PreferredPaymentMode
having avg(tenure)=10 and sum(OrderCount)>500;
select
case
when warehousetohome<=5 then 'very close distance'
when warehousetohome<=10 then'close distance'
when warehousetohome<=15 then 'moderate distance'
else 'far distance'
end as distance_category,
churn,
count(*)as customer_count
from customer_churn
group by distance_category,Churn
order by distance_category,churn;
select *
from customer_churn
where MaritalStatus ='Married'
and CityTier =1
and OrderCount>(select avg(OrderCount)from customer_churn);
create table customer_returns (
returnid int primary key,
customerid int,
returndate date,
refundamount int
);
insert into  customer_returns values
(1001,50022, '2023-01-01' ,2130),
(1002,50316,  '2023-01-23', 2000),
(1003,51099, '2023-02-14',2290),
(1004, 52321, '2023-03-08',2510),
(1005,52928, '2023-03-20' ,3000),
(1006,53749, '2023-04-17' ,1740),
(1007,54206, '2023-04-21', 3250),
(1008, 54838, '2023-04-30' ,1990);
select r.*,c.*
from customer_returns r
join customer_churn c on r.customerid=c.CustomerID
where c.Churn =1 and c.Complain =1;