SELECT a1.name,a1.ts,a1.hour,a2.max_high
FROM (SELECT name, ts , high, substring(ts,12,2) AS hour
      FROM "finance-db") a1 ,
(SELECT name, max(high) as max_high, substring(ts,12,2) AS hour
   FROM "finance-db"
   GROUP BY name,  substring(ts,12,2)) a2
WHERE a1.name = a2.name  AND a1.hour = a2.hour AND a1.high = a2.max_high
ORDER BY a1.name, a2.hour;
