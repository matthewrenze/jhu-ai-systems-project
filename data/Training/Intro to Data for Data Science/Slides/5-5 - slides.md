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

One table per type
All related data
Multiple tables

![image An icon of a set of 6 database tables with primary and foreign key relationships in a minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-left -->

# Relationships

Relationship
Primary key
Foreign key

![image An icon of a set of 6 database tables with primary and foreign key relationships in a minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-comparison -->

# Relationships

## Patients
| Name | Gender | Age |
| ---- | ------ | --- |
| Bill | Male   | 21  |
| Miko | Female | 15  |
| Juan | Other  | 45  |


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
| 2          | 2023-01-01 | 38.1  |
| 2          | 2023-01-02 | 36.5  |

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
| 2          | 2023-01-01 | 38.1  |
| 2          | 2023-01-02 | 36.5  |
