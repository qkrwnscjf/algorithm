-- 코드를 작성해주세요
SELECT
    COUNT(*) AS fish_count
FROM
    fish_info as a, fish_name_info as b
where 
    a.fish_type = b.fish_type and b.fish_name IN ('BASS', 'SNAPPER')