/*
* Selecting the average safety scores of areas over the course of Year then Month, than day
*/

Select l.neighbourhood, avg(co."severityLevel") as safetyScore, Extract(year from d."Date") as year
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.neighbourhood, year
order by l.neighbourhood

Select l.neighbourhood, avg(co."severityLevel") as safetyScore, d.month
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.neighbourhood, month
order by l.neighbourhood

Select l.neighbourhood, avg(co."severityLevel") as safetyScore, Extract(day from d."Date") as day
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.neighbourhood, day
order by l.neighbourhood

/*
* 
*/