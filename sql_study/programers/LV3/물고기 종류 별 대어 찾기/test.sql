SELECT 
    fi.ID,
    fni.FISH_NAME, 
    fi.LENGTH 
FROM FISH_INFO fi
JOIN FISH_NAME_INFO fni
ON fi.FISH_TYPE = fni.FISH_TYPE
WHERE (fi.FISH_TYPE, fi.LENGTH) in (SELECT FISH_TYPE, MAX(LENGTH)
                                    FROM FISH_INFO
                                    GROUP BY FISH_TYPE)
ORDER BY ID;
--where 절에서 서브쿼리 쓸 때 가능하면 In 사용 