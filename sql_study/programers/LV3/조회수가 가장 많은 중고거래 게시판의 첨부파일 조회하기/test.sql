-- 코드를 입력하세요
SELECT
  CONCAT(
    '/home/grep/src/', -- concat 사용
    F.BOARD_ID,
    '/',
    F.FILE_ID,
    F.FILE_NAME,
    F.FILE_EXT
  ) AS FILE_PATH
FROM USED_GOODS_FILE F
JOIN USED_GOODS_BOARD B on F.BOARD_ID = B.BOARD_ID
WHERE B.VIEWS = (select max(views)
                from used_goods_board
                )
ORDER BY F.FILE_ID DESC;
