---
marp: true
title: 6 - Queries
theme: template
---

# Queries

![bg contain](images/563-4.png)

<!--
How do we extract information from tabular data? 

The answer, is a query!
-->

---

<!-- _class: title-two-content-left -->

# Queries

Question
Programming language
Structured Query Language

![image](images/500-5.png)

<!--
[1] A query is computer representation of a question we want answer using a table of data.

They allow us to ask questions of the data and return answers as results.

[2] Queries are created using programming languages.

More specifically, we use a special type of programming language called a query language.

[3] The most popular query language is Structured Query Language (or SQL for short).

However, you can also perform queries using other programming languages like Python and R.
-->

---

<!-- _class: title-two-content-comparison -->

# Queries

Question

What was Bill's average 
body temperature 
over the past 5 years?

SQL Query

select avg([Temperature])
from [Vital Signs]
where [Name] = "Bill"
and [Date] >= "2015-01-01"

<!--
[1] For example, let's say we want to answer the question: "What was Bill's average body temperature over the past 5 years".

[2] We could write this question in the form of a SQL query.

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

SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"


<!--
When we execute this query, 

[1] First, the database will scan all of the records in the Vital Signs table 

Next, it will filter out anyone who is not our patient named Bill.
-->

---

<!-- _class: title-two-content-comparison -->

# Queries

SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"


<!--
Then, it will filter out any row that is older than January 1, 2015 (i.e. five years before today's date)
-->

---

<!-- _class: title-two-content-comparison -->

# Queries

SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"


<!--
Next, it will select just the Temperature column from the Vital Signs table.
-->

---

<!-- _class: title-two-content-comparison -->

# Queries

SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"




Average

<!--
[1] Finally, it will compute the average of the remaining temperature values.
-->

---

<!-- _class: title-two-content-comparison -->

# Queries

SQL Query

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

Result

37.0

<!--
The computer will then return this value as a result.

As we can see, the result of executing this query is 37 degrees Celsius.
-->

---

<!-- _class: title-three-content -->

# Queries

What was Bill's average body temperature over the past 
5 years?

select avg([Temperature])
from [Vital Signs]
where [Patient Name] = "Bill"
and [Date] >= "2015-01-01"

37.0

Question

Query

Result

It was 37°C.

Answer

<!--
Essentially, this is how we get from a question to an answer, using a query.

[1] We start with a question in our natural language,

[2]  - we construct a SQL query to express that question to the computer, 

[3]  - we execute the query which returns a result, 

[4]  - and then we express that result in the form of an answer to the question.

Queries are the primary tool used for extracting information from data in data science.
-->