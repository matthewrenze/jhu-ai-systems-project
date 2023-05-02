---
marp: true
title: 6 - Queries
theme: template
---

<!-- _class: title-only -->

# Queries

---

<!-- _class: title-two-content-left -->

# Queries

Question
Programming language
Structured Query Language

![image An icon of a magnifying glass in a minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-comparison -->

# Queries

## Question

What was Bill's average 
body temperature 
over the past 5 years?

## SQL Query

select avg([Temperature])
from [Vital Signs]
where [Name] = "Bill"
and [Date] >= "2015-01-01"

---

<!-- _class: title-two-content-comparison -->

# Queries

## SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

## Vital Signs

| Date       | Name | Temp. |
| ---------- | ---- | ----- |
| 2010-01-01 | Bill | 37.0  |
| 2010-01-02 | Miko | 38.5  |
| 2010-01-03 | Juan | 38.2  | 


---

<!-- _class: title-two-content-comparison -->

# Queries

## SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

## Vital Signs

| Date       | Name | Temp. |
| ---------- | ---- | ----- |
| 2010-01-01 | Bill | 37.0  |
| 2015-01-01 | Bill | 36.9  |
| 2020-01-01 | Bill | 37.1  | 

---

<!-- _class: title-two-content-comparison -->

# Queries

## SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

## Vital Signs
| Date       | Name   | Temp.  |
| ---------- | ----   | ------ |
| 2015-01-01 | Bill   | 36.9   |
| 2020-01-01 | Bill   | 37.1   |
| &nbsp;     | &nbsp; | &nbsp; | 


---

<!-- _class: title-two-content-comparison -->

# Queries

## SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

## Vital Signs

| Temp.  |
| ------ |
| 36.9   |
| 37.1   |
| &nbsp; | 

---

<!-- _class: title-two-content-comparison -->

# Queries

## SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

## Result

37.0

---

<!-- _class: title-two-content-comparison -->

# Queries

## Question
What was Bill's average body temperature over the past 
5 years?

## Answer
It was 37°C.
