use sakila;

#1
select customer_id, count(customer_id) as 'Top 5 rental customers' from rental
group by customer_id
order by count(customer_id) desc
limit 5; 

#2
select district, count(address), count(address2) from address
group by district
order by district;

#3
select title, rental_rate, replacement_cost from film
where rental_rate < 1 or replacement_cost < 15;

#4
select customer_id, sum(amount) as 'total amount spent' from payment
group by customer_id
having sum(amount) > 150;

#5
select customer_id, first_name from customer
where first_name like ('__%o');

