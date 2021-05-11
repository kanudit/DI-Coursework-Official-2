-- SELECT address, phone from address where district = 'Texas'
-- SELECT * FROM film WHERE film_id = 15 or film_id =150
SELECT film_id, title, description, length, rental_rate FROM film where title = 'Ants'
SELECT title,replacement_cost FROM film ORDER BY replacement_cost ASC LIMIT 10

<!-- select the info that I want first -->
SELECT customer.customer_id,customer.last_name,payment.payment_date,payment.amount 
<!-- Then specificy from where itll be joined and what theh correlating keys ares -->
FROM customer JOIN payment ON customer.customer_id = payment.customer_id Order BY customer.customer_id ASC

SELECT film_id,title FROM film WHERE film_id NOT IN (SELECT film_id FROM inventory)

SELECT city.city,country.country, city.country_id
FROM city join country ON city.country_id = country.country_id