---
marp: true
title: 6 - Queries
theme: template
---

<!-- _class: title-only -->

# Queries

---

<!-- _class: title-two-content-left-center -->

# Queries

Computer representation of a question
Extract information from data
Return answers as results
Created using programming languages

![image An icon of a database in a flat minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-left-center -->

# SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

![image An icon of a database in a minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-comparison -->

# Query Execution

## SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

## Execution Steps

1. Scan all records
2. Filter by patient name
3. Filter by date
4. Select temperature column
5. Compute average

## Result

37.0