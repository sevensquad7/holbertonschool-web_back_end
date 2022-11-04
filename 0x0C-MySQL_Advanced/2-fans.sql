-- Project Mysql Advanced
-- Web back end
SELECT origin, sum(fans) AS nb_fans FROM metal_bands GROUP BY (origin) ORDER BY (nb_fans) DESC;
