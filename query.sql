select name, ts, substr(ts, 12, 2) as hour, max(high) as max_high
from athena
group by name,ts,  substr(ts, 12, 2)
order by hour DESC;
