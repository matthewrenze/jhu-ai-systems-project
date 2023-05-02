---
marp: true
title: 6 - Queries
theme: template
---

<!-- _class: title-only -->

# Queries

<!--
How do we extract information from tabular data? 

The answer, is a query.
-->

---

<!-- _class: title-two-content-left -->

# Queries

Question
Programming language
Structured Query Language

![image An icon of a magnifying glass in a minimalist style](images/placeholder.png)

<!--
A query is computer representation of a question we want answer using a table of data.

They allow us to ask questions of the data and return answers as results.

Queries are created using programming languages.

More specifically, we use a special type of programming language called a query language.

The most popular query language is Structured Query Language (or SQL for short).

However, you can also perform queries using other programming languages like Python and R.
-->

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

<!--
For example, let's say we want to answer the question: "What was Bill's average body temperature over the past 5 years".

We could write this question in the form of a SQL query.

The SQL query allows us to express that we want to:

 - select the average temperature

 - from the Vital Signs table

 - where the patient's name is "Bill"

 - and the date is greater than or equal to January 1, 2015 (which we're assuming is five years ago).

I've intentionally kept this query simple for those of you who have never seen a SQL query before.

However, if you've had some experience with SQL, you may see several ways we could improve this query.
-->

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


<!--
When we execute this query, 

First, the database will scan all of the records in the Vital Signs table 

Next, it will filter out anyone who is not our patient named Bill.
-->

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

<!--
Then, it will filter out any row that is older than January 1, 2015.
-->

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


<!--
Next, it will select just the Temperature column from the Vital Signs table.
-->

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

<!--
Finally, it will compute the average of the remaining temperature values.
-->

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

<!--
The computer will then return this value as a result.

As we can see, the result of executing this query is 37 degrees Celsius.
-->

---

<!-- _class: title-two-content-comparison -->

# Queries

## Question
What was Bill's average body temperature over the past 
5 years?

## Answer
It was 37°C.

<!--
Essentially, this is how we get from a question to an answer, using a query.

We start with a question in our natural language,

 - we construct a SQL query to express that question to the computer, 

 - we execute the query which returns a result, 

 - and then we express that result in the form of an answer to the question.

Queries are the primary tool used for extracting information from data in data science.
-->