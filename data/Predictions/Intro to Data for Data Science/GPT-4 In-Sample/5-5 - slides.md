---
marp: true
title: 5 - Relationships
theme: template
---

<!-- _class: title-only -->

# Relationships

---

<!-- _class: title-two-content-left-center -->

# Relationships

Separate tables
Highly cohesive data
Keys

![image An icon of a database with two arrows pointing to another database in a flat minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-comparison -->

# Example

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

# Relationships

## Patients
| ID | Name | Gender | Age |
| -- | ---- | ------ | --- |
| 1  | Bill | Male   | 21  |
| 2  | Miko | Female | 15  |
| 3  | Juan | Other  | 45  |


## Vital Signs
| Patient ID | Date       | Temp. |
| ---------- | ---------- | ----- |
| 1          | 2023-01-01 | 37.1  |
| 2