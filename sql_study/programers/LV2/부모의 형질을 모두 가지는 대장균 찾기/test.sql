-- 코드를 작성해주세요
select so.ID, so.GENOTYPE, pa.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA so join ECOLI_DATA pa on so.PARENT_ID = pa.ID
where pa.GENOTYPE & so.GENOTYPE = pa.GENOTYPE
order by so.ID asc