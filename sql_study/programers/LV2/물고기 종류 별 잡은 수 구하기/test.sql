-- 코드를 작성해주세요
SELECT 
    COUNT(a.fish_type) AS fish_count, 
    b.fish_name AS fish_name
FROM 
    fish_info AS a, 
    fish_name_info AS b
WHERE 
    a.fish_type = b.fish_type
GROUP BY 
    b.fish_name
ORDER BY 
    fish_count desc