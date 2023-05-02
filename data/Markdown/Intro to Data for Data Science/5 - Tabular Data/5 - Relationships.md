---
marp: true
title: 5 - Relationships
theme: template
---

# Relationships

![bg contain](images/558-4.png)

<!--
Everything is related in some way, shape, or form.

So how do we represent relationships in data science?
-->

---

<!-- _class: title-two-content-left -->

# Relationships

One table per type
All related data
Multiple tables

![image](images/490-6.png)

<!--
[1] In data science, we want each table to contain a single type of observation or type of entity.

For example, we want to keep a list of our patients in one table and a list of our doctors a separate table. 

[2] We want each table to only contain data that are related to one another in a highly cohesive way.

We don't want to compress multiple types of observations or multiple types of entities into a single table.

So, we create a separate table for each type of observation or entity.

[3] This means that our dataset often needs to be split up into multiple tables.

When we have multiple tables of data, the observations in one table can be related to the observations in another table.
-->

---

<!-- _class: title-two-content-left -->

# Relationships

Relationship
Primary key
Foreign key

![image](images/562-6.png)

<!--
[1] A relationship is a way to express how a row of data in one table is related to a row of data in another table.

We create relationships between rows using "keys".

[2] We use a primary key to uniquely identify an observation in it's source table.

[4] Then we use a foreign key in observations in a second table to refer back to the original observation in the source table.
-->

---

<!-- _class: title-two-content-left -->

# Relationships



<!--
For example, imagine that we have two tables:

[1] - First, we have a table of patients.

It contains their names, genders, dates of birth, and more.

[2] - Second, we have a table of all of our patient's vital signs.

It contains observations of the patient's temperature, heart rate and more for a specific day.

We could duplicate the patient's name and other personal data for each recording of their vital signs.

However, it's much more efficient to store the patient's data once and then simply refer back to that data from the vital-signs table.

We do this by creating a primary key and a foreign key.
-->

---

<!-- _class: title-two-content-left -->

# Relationships



1

2

3

<!--
First, in our patients table, we create a column to store our primary key.

[1] Then we create a primary key for each unique patient in our patients table.

We use a 1 for Bill, a 2 for Miko, and so on.

This primary key uniquely identifies each patient in our system.
-->

---

<!-- _class: title-two-content-left -->

# Relationships



1

2

2

<!--
Next, in our vital-signs table, we create a column for our foreign key 

[2] We populate this column with the unique identifier that points back to the primary key.

We use a 1 for Bill, a 2 for Miko, and so on.
-->

---

<!-- _class: title-two-content-left -->

# Relationships



<!--
Now we can navigate the relationship forward from any patient to get their vital signs.

Or we can navigate the relationship backwards from a vital sign to get the patient's name and information.

Relationships allow us to connect data from table to table in many ways.

However, we'll have to defer these various types of relationships to a more advanced course on data science.
-->