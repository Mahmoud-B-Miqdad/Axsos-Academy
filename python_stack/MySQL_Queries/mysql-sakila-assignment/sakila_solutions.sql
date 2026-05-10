-- ---------------------------------------------------------
-- Assignment: Sakila Queries
-- Author: Mahmoud Miqdad
-- ---------------------------------------------------------

USE sakila;

-- 1. Get all customers inside city_id = 312
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE address.city_id = 312;

-- 2. Get all comedy films
SELECT film.film_id as film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

-- 3. Get all films joined by actor_id = 5
SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name, film.title, film.description, film.release_year
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;

-- 4. Get all customers in store_id = 1 inside cities (1, 42, 312, and 459)
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.address_id = address.address_id
WHERE customer.store_id = 1 AND address.city_id IN (1, 42, 312, 459);

-- 5. Get all films with "rating = G" and "special feature = behind the scenes" for actor_id = 15
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
WHERE film.rating = 'G' 
AND film.special_features LIKE '%Behind the Scenes%' 
AND film_actor.actor_id = 15;

-- 6. Get all actors joining the film_id = 369
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- 7. Get all drama films with a rental rate of 2.99
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Drama' AND film.rental_rate = 2.99;

-- 8. Get all action films joined by SANDRA KILMER
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, 
       actor.first_name, actor.last_name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' 
AND actor.first_name = 'SANDRA' 
AND actor.last_name = 'KILMER'
order by film.title asc