use sakila;


#1
select film.title, film.rating, category.name as 'Category'
from film
join film_category
on  film.film_id = film_category.film_id
join category
on film_category.category_id = category.category_id
where rating = 'PG';

#2
select actor.actor_id, actor.first_name, actor.last_name, count(film.film_id) as 'Number of Films'
from actor
join film_actor
on actor.actor_id = film_actor.actor_id
join film
on film.film_id = film_actor.film_id
group by actor_id;

#3
select inventory.film_id, film_text.title, count(inventory.film_id) as 'Films in Inventory', inventory.store_id
from (inventory
join film_text
on inventory.film_id = film_text.film_id)
group by inventory.film_id, inventory.store_id
order by count(inventory.film_id) desc;


select * from inventory;