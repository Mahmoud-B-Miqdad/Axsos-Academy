-- ---------------------------------------------------------
-- Assignment: MySQL Countries Queries
-- Author: Mahmoud Miqdad
-- ---------------------------------------------------------

USE world;

-- 1. Retrieve all countries that speak 'Slovene'. 
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- 2. Display the total number of cities for each country.
SELECT countries.name, COUNT(cities.id) AS total_cities
FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
GROUP BY countries.id
ORDER BY total_cities DESC;

-- 3. Get all cities in 'Mexico' with a population greater than 500,000.
SELECT cities.name, cities.population, countries.id as country_id
FROM cities
JOIN countries ON cities.country_id = countries.id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;

-- 4. List all languages in each country that have a percentage greater than 89%.
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

-- 5. Retrieve countries with Surface Area below 501 and Population greater than 100,000.
SELECT name, surface_area, population
FROM countries
WHERE surface_area < 501 AND population > 100000;

-- 6. Get countries with 'Constitutional Monarchy' government, capital ID > 200, and life expectancy > 75.
SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE government_form = 'Constitutional Monarchy' 
AND capital > 200 
AND life_expectancy > 75;

-- 7. Retrieve all cities in 'Argentina' within the 'Buenos Aires' district having a population > 500,000.
SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' 
AND cities.district = 'Buenos Aires' 
AND cities.population > 500000;

-- 8. Summarize the number of countries in each region.
SELECT region, COUNT(id) AS number_of_countries
FROM countries
GROUP BY region
ORDER BY number_of_countries DESC;