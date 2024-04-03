/*
* Selecting the average safety scores of areas over the course of Year then Month, than day
*/

Select l.neighbourhood, avg(co."severityLevel") as safetyScore, Extract(year from d."Date") as year
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.neighbourhood, year
order by l.neighbourhood

Select l.neighbourhood, avg(co."severityLevel") as safetyScore, Extract(year from d."Date") as year, Extract(month from d."Date") as month
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.neighbourhood, month, year
order by l.neighbourhood

Select l.neighbourhood, avg(co."severityLevel") as safetyScore, d."Date"
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.neighbourhood, d."Date"
order by l.neighbourhood

/*
* --ROll Up using neighbourhood, city, country per year
*/

Select l.neighbourhood, avg(co."severityLevel") as safetyScore, Extract(year from d."Date") as year
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.neighbourhood, year
order by l.neighbourhood

Select l.city, avg(co."severityLevel") as safetyScore, Extract(year from d."Date") as year
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.city, year
order by l.city

Select l.province, avg(co."severityLevel") as safetyScore, Extract(year from d."Date") as year
from "Criminal_Offences_Final" co
join "Location" l on l."locationId" = co."locationId"
join "Date" d on d."Date" = co."incidentDate"
Group by l.province, year
order by l.province

-- dice: all crime data from slice location of Hunt Club
Select * from "Criminal_Offences_Final"
where "locationId" = 43

-- dice: all crime data from slice location of Hunt Club from year 2022
Select * from "Criminal_Offences_Final"
where "locationId" = 43 and Extract(year from "incidentDate") = 2022

-- dice: all crime data from slice location of Hunt Club that had severe crimes
Select * from "Criminal_Offences_Final"
where "locationId" = 43 and "severityLevel" > 8
