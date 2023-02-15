-- lists all the cities of California
SELECT cities.id, name FROM cities WHERE state_id =
(SELECT id FROM states WHERE name = 'Califonia') ORDER BY cities.id ASC;
