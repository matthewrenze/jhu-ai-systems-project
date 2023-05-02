---
marp: true
title: 6 - Queries
theme: template
---

<!-- _class: title-only -->

# Queries

---

<!-- _class: title-two-content-left-center -->

# Query

Extract information
Ask questions
Return answers

![image An icon of a magnifying glass hovering over a table of data in a flat minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-left-center -->

# Query Languages

SQL
Python
R

![image An icon of a computer keyboard with the letters "SQL" on the keys in a flat minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-left-center -->

# Example Query

What was Bill's average body temperature over the past 5 years?

![image An icon of a thermometer with a temperature reading of 37 degrees Celsius in a flat minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-left-center -->

# SQL Query

select avg([Temperature])
from [Vital Signs]
where [Name] = "Bill"
and [Date] >= "2015-01-01"

![image An icon of a computer keyboard with the letters "SQL" on the keys in a flat minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-left-center -->

# Query Execution

Scan records
Filter by name
Filter by date
Select temperature
Compute average

![image An icon of a magnifying glass hovering over a table of data in a flat minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-left-center -->

# Result

37 degrees Celsius

![image An icon of a thermometer with a temperature reading of 37 degrees Celsius in