---
marp: true
title: 5 - Relationships
theme: template
---

<!-- _class: title-only -->

# Relationships

---

<!-- _class: title-two-content-left-center -->

# Tables

Single type of observation
Single type of entity
Highly cohesive

![image An icon of a database in a flat minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-left-center -->

# Keys

Primary key
Foreign key

![image An icon of a key in a minimalist style](images/placeholder.png)

---

<!-- _class: title-two-content-comparison -->

# Example

## Patients
| ID | Name | Gender | DOB        |
| -- | ---- | ------ | ---------- |
| 1  | Bill | Male   | 2002-01-01 |
| 2  | Miko | Female | 2008-05-12 |
| 3  | Juan | Other  | 1978-12-31 |

## Vital Signs
| ID | Patient ID | Date       | Temp. | Pulse |
| -- | --------- | ---------- | ----- | ----- |
| 1  | 1         | 2023-01-01 | 37.1  | 89    |
| 2  | 2         | 2023-01-01 | 38.1  | 80    |
| 3  | 2         | 2023-01-02 | 36.5  | 75    |

---

<!-- _class: title-two-content-left-center -->

# Example

## Patients
| **ID** | Name | Gender | DOB        |
| ------ | ---- | ------ | ----------