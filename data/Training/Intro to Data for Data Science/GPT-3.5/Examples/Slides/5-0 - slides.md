---
marp: true
title: 5 - Miscellaneous Examples
theme: template
---

<!-- _class: title-one-content -->

# Tabular Data

| Name | Gender | Age |
| ---- | ------ | --- |
| Bill | Male   | 21  |
| Miko | Female | 15  |
| Juan | Other  | 45  |

---

<!-- _class: title-two-content-left-center -->

# Variables

Value that changes
On the columns
Same data type

| Date         | Pulse      | Temp.     |
| ------------ | ---------- | --------- |
| **1/1/2023** | 89         | 39.0      |
| 2023-01-02   | **Normal** | 38.5      |
| 2023-01-03   | 80         | **99° F** | 

---

<!-- _class: title-two-content-comparison -->

# Relationships

## Patients
| ID | Name | Gender | Age |
| -- | ---- | ------ | --- |
| 1  | Bill | Male   | 21  |
| 2  | Miko | Female | 15  |
| 3  | Juan | Other  | 45  |


## Vital Signs
| Name | Date       | Temp. |
| ---- | ---------- | ----- |
| Bill | 2023-01-01 | 37.1  |
| Miko | 2023-01-01 | 38.1  |
| Miko | 2023-01-02 | 36.5  |

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

## Result

37.0
