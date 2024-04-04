-- Selecting the average safety scores of areas over the course of Year then Month, than day

Select l.neighbourhood, avg(f."SafetyScore"), Extract(year from f."date") as year
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
Group by l.neighbourhood, year
order by l.neighbourhood

-- drill down to year, month
Select l.neighbourhood, avg(f."SafetyScore"), Extract(year from f."date") as year, Extract(month from f."date") as month
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
Group by l.neighbourhood, year, month
order by l.neighbourhood

-- or just month
Select l.neighbourhood, avg(f."SafetyScore"), Extract(month from f."date") as month
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
Group by l.neighbourhood, month
order by l.neighbourhood

-- to year, month, day
Select l.neighbourhood, avg(f."SafetyScore"), f.date
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
Group by l.neighbourhood, f.date
order by l.neighbourhood

-- or just day
Select l.neighbourhood, avg(f."SafetyScore"), Extract(day from f."date") as day
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
Group by l.neighbourhood, day
order by l.neighbourhood

-- ROll Up do the bottom one first^


-- dice: all Fact table data from slice location of Ottawa South
Select * from "Fact"
where "locationId" = 36

-- dice: all Fact data from slice location of Ottawa South from year 2022
Select * from "Fact"
where "locationId" = 36 and Extract(year from "date") = 2022

-- dice: all Fact data from slice location of Ottawa South that had severe crimes
Select * from "Fact"
where "locationId" = 36 and "SafetyScore" > 8

-- Drill down and slice: All neighbourhoods and their safetyscores during the month of march for various years
Select l.neighbourhood, avg(f."SafetyScore"), Extract(year from f."date") as year, Extract(month from f."date") as month
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
where Extract(month from f."date") = 3
Group by l.neighbourhood, year, month
order by l.neighbourhood

-- Roll up and slice:all neighbourhoods and their safety scores that have an avg rent of over 500 for various years
Select l.neighbourhood,avg(f."SafetyScore"), Extract(year from f."date") as year, f."Avg_Rent"
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
where f."Avg_Rent">500
Group by l.neighbourhood, year, f."Avg_Rent"
order by l.neighbourhood

-- Drill down and dice: Bells Corners and its safetyscores during the month of march for various years
Select l.neighbourhood, avg(f."SafetyScore"), Extract(year from f."date") as year, Extract(month from f."date") as month
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
where Extract(month from f."date") = 3 and f."locationId" = 4
Group by l.neighbourhood, year, month
order by l.neighbourhood

-- Roll up and dice:Hawthorne Meadows and its safety score for 2018
Select l.neighbourhood,avg(f."SafetyScore"), Extract(year from f."date") as year, f."Avg_Rent"
from "Fact" f
join "Location" l on l."locationId" = f."locationId"
where Extract(year from f."date") = 2018 and f."locationId" = 35
Group by l.neighbourhood, year, f."Avg_Rent"
order by l.neighbourhood