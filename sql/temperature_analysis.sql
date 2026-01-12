
-- 1. View sample data
SELECT * 
FROM india_temperature
LIMIT 5;

-- 2. Decadal Average Temperature
SELECT 
    (year / 10) * 10 AS decade,
    AVG(annual) AS avg_annual_temperature
FROM india_temperature
GROUP BY decade
ORDER BY decade;

-- 3. Hottest Years
SELECT year, annual
FROM india_temperature
ORDER BY annual DESC
LIMIT 10;

-- 4. Seasonal Contribution
SELECT
    AVG(jan_feb) AS winter_avg,
    AVG(mar_may) AS pre_monsoon_avg,
    AVG(jun_sep) AS monsoon_avg,
    AVG(oct_dec) AS post_monsoon_avg
FROM india_temperature;

-- 5. Climate Shift (Before vs After 1970)
SELECT
    CASE 
        WHEN year < 1970 THEN 'Before 1970'
        ELSE 'After 1970'
    END AS period,
    AVG(annual) AS avg_temperature
FROM india_temperature
GROUP BY period;
