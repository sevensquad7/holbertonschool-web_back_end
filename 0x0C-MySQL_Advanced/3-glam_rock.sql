-- Project Mysql Advanced
-- Web back end
SELECT band_name, (IFNULL(split, 2020) -  formed) AS lifespan FROM metal_bands WHERE style REGEXP 'Glam rock' ORDER BY lifespan DESC;
