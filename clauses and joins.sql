use employee;
create table employees(
emp_id int primary key,
emp_name varchar(50),
age int,
salary decimal(10,2),
designation varchar (50),
department_id int,
hire_date date,
gender varchar(10),
location varchar(50)
);
insert into employees values
(1,'Anu', 28,55000,'Analyst',1,'2015-05-10','female','kochi'),
(2,'Rahul',32,45000,'developer',2,'2018-03-12','male','Trivandrum');
select distinct salary from employees;
select *from employees order by salary desc;
select*from employees where salary>50000;
select department_id,count(*)from employees group by department_id;
select avg(salary)from employees;
select max(salary) from employees;
select *from employees where emp_name like 'A%';
select department_id, count(*) from employees group by department_id having count(*)>=1;
select department_id,sum(salary) from employees group by department_id;
select min(salary) from employees;
update employees set salary=60000 where emp_id=1;
alter table employees add  column email varchar(50);
delete from employees where emp_id=2;
select max(salary) as max_salary, min(salary) as min_salary,avg(salary)as avg_salary from employees;
select*from employees where salary>(select avg(salary) from employees);
select*from employees where emp_name like'%a%';
select*from employees where salary between 40000 and 70000;
select*from employees order by salary desc limit 1;
select*from employees where location in('kochi','trivandrum');
select upper(emp_name),salary from employees;
select emp_name,salary, case
when salary>50000 then 'high salary'
else 'normal salary'
end as salary_status
from employees;
select emp_name, year(hire_date) as joining_year from employees;
select* from employees where email is null;
select concat(emp_name, '-',designation) as emp_details from employees;
create view high_earners as select*from employees where salary>50000;
select*from high_earners;
create table departments (
department_id int primary key,
department_name varchar(50)
);
insert into departments values
(1,'It & analytics'),
(2,'Development');
select e.emp_name,e.designation,d. department_name
from employees e
join departments d on e.department_id=d.department_id;
