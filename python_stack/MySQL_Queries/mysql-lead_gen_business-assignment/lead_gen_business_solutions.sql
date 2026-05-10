-- ---------------------------------------------------------
-- Assignment: Lead Gen Business (Queries Solution)
-- Author: Mahmoud Miqdad
-- ---------------------------------------------------------

USE `lead_gen_business`;

-- 1. What query would you run to get the total revenue and month name for March of 2012?
SELECT MONTHNAME(b.charged_datetime) AS month, SUM(b.amount) AS total_revenue
FROM billing AS b
WHERE b.charged_datetime >= '2012-03-01' AND b.charged_datetime <= '2012-03-31';


-- 2. What query would you run to get total revenue collected from the client with an id of 2?
SELECT b.client_id, SUM(b.amount) AS total_revenue
FROM billing AS b
WHERE b.client_id = 2;


-- 3. What query would you run to get all the sites that client with an id of 10 owns?
SELECT s.domain_name AS site, s.client_id
FROM sites AS s
WHERE s.client_id = 10;


-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? 
-- What about for client id 20?

-- For Client ID 1:
SELECT s.client_id, COUNT(s.domain_name) AS number_of_websites, MONTHNAME(s.created_datetime) AS month_created, YEAR(s.created_datetime) AS year_created
FROM sites AS s
WHERE s.client_id = 1
GROUP BY year_created, month_created;

-- For Client ID 20:
SELECT s.client_id, COUNT(s.domain_name) AS number_of_websites, MONTHNAME(s.created_datetime) AS month_created, YEAR(s.created_datetime) AS year_created
FROM sites AS s
WHERE s.client_id = 20
GROUP BY year_created, month_created;


-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
SELECT s.domain_name AS website, COUNT(l.leads_id) AS number_of_leads, DATE_FORMAT(l.registered_datetime, '%M %e, %Y') AS date_generated
FROM sites AS s
JOIN leads AS l ON s.site_id = l.site_id
WHERE l.registered_datetime >= '2011-01-01' AND l.registered_datetime <= '2011-02-15'
GROUP BY s.site_id;


-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name, COUNT(l.leads_id) AS number_of_leads
FROM clients AS c
JOIN sites AS s ON c.client_id = s.client_id
JOIN leads AS l ON s.site_id = l.site_id
WHERE l.registered_datetime >= '2011-01-01' AND l.registered_datetime <= '2011-12-31'
GROUP BY c.client_id;


-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name, COUNT(l.leads_id) AS number_of_leads, MONTHNAME(l.registered_datetime) AS month_generated
FROM clients AS c
JOIN sites AS s ON c.client_id = s.client_id
JOIN leads AS l ON s.site_id = l.site_id
WHERE l.registered_datetime >= '2011-01-01' AND l.registered_datetime <= '2011-06-30'
GROUP BY l.registered_datetime
ORDER BY l.registered_datetime;


-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? 
-- Order this query by client id. 
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name, s.domain_name AS website, COUNT(l.leads_id) AS number_of_leads
FROM clients AS c
JOIN sites AS s ON c.client_id = s.client_id
JOIN leads AS l ON s.site_id = l.site_id
WHERE l.registered_datetime >= '2011-01-01' AND l.registered_datetime <= '2011-12-31'
GROUP BY s.site_id
ORDER BY c.client_id;

-- Second query for all time (including sites with 0 leads):
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name, s.domain_name AS website, COUNT(l.leads_id) AS number_of_leads
FROM clients AS c
JOIN sites AS s ON c.client_id = s.client_id
LEFT JOIN leads AS l ON s.site_id = l.site_id
GROUP BY c.client_id, s.site_id
ORDER BY c.client_id;


-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. 
-- Order it by client id.
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name, SUM(b.amount) AS total_revenue, MONTHNAME(b.charged_datetime) AS month_name, YEAR(b.charged_datetime) AS year_charge
FROM clients AS c
JOIN billing AS b ON c.client_id = b.client_id
GROUP BY c.client_id, year_charge, month_name
ORDER BY c.client_id, year_charge, MONTH(b.charged_datetime);


-- 10. Write a single query that retrieves all the sites that each client owns. 
-- Group the results so that each client's sites are displayed in a single field. (Hint: use GROUP_CONCAT)
SELECT CONCAT(c.first_name, ' ', c.last_name) AS client_name, GROUP_CONCAT(s.domain_name SEPARATOR ' / ') AS sites
FROM clients AS c
LEFT JOIN sites AS s ON c.client_id = s.client_id
GROUP BY c.client_id;