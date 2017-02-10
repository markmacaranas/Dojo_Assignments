SELECT name, language, percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER BY percentage DESC;

SELECT countries.name, COUNT(cities.name) AS 'number of cities'
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name ORDER BY COUNT(cities.name) DESC;

SELECT countries.name, cities.name, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;

SELECT language
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE percentage > 89
ORDER BY percentage DESC;

SELECT name
FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT name
FROM countries
WHERE capital > 200 AND life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.population > 500000 AND cities.district = 'Buenos Aires' AND countries.name = 'Argentina';

SELECT region, COUNT(countries.name) as 'number of countries'
FROM countries
GROUP BY region ORDER BY COUNT(countries.name) DESC;