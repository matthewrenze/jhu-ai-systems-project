---
marp: true
title: 4 - Variables
theme: template
---

<!-- _class: title-only -->

# Variables

<!--
The world is in a constant state of change; things vary from one observation to the next.

But how do we record these variations across observations in data science?
-->

---

<!-- _class: title-two-content-left-center -->

# Variables

Value that changes
On the columns
<br/>
<br/>

![image An icon of a database table with three rows and three columns and the middle column is highlighted, in a minimalist style](images/placeholder.png)


<!--
A variable is placeholder for a value that changes. 

We call them "variables" because their values "vary" across each observation.

In data science, we store variables on the columns of a table.

Columns are the vertical groups of data that are contained within the table.
-->

---

<!-- _class: title-two-content-left-center -->

# Variables

Value that changes
On the columns
Same data type

| Date       | Pulse | Temp. |
| ---------- | ----- | ----- |
| 2023-01-01 | 89    | 39.0  |
| 2023-01-02 | 85    | 38.5  |
| 2023-01-03 | 80    | 37.2  | 


<!--
For example, imagine we're recording vital signs for a patient at a hospital.

Our variables might be:

 - the date and time of the observation,

 - the patients heart rate measured by their pulse, 

 - and their body temperature at the time of the observation.

What is most important, is that all of the elements in a specific column must be of the same data type, scale, and unit of measure.
-->

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


<!--
For example:

 - we don't want our dates to be stored using different date formats.

 - we don't want our heart rate data to be stored using two different data types.

 - and we don't want our temperature to use both Celsius and Fahrenheit units of measure.
-->

---

<!-- _class: title-two-content-left-center -->

# Variables

Value that changes
On the columns
Same data type
One per column

| Date       | Pulse | Temp. |
| ---------- | ----- | ----- |
| 2023-01-01 | 89    | 39.0  |
| 2023-01-02 | 85    | 38.5  |
| 2023-01-03 | 80    | 37.2  | 


<!--
Instead, we want all of the data in the column to use the same data type, same scale, and same units of measure.

Finally, we want one and only one variable per column of data.

We don't want to try placing multiple variables in a single column.
-->

---

<!-- _class: title-two-content-left-center -->

# Variables

Value that changes
On the columns
Same data type
One per column

| Date       | BP         | Temp. |
| ---------- | ---------- | ----- |
| 2023-01-01 | **139/89** | 39.0  |
| 2023-01-02 | **128/85** | 38.5  |
| 2023-01-03 | **120/80** | 37.2  | 

<!--
For example, if we're recording blood pressure, we record two numbers:

 - the systolic blood pressure,

 - and the diastolic blood pressure.

We don't want to record both of these measures in a single column, like we commonly see it written in our medical history.
-->

---

<!-- _class: title-two-content-left-center -->

# Variables

Value that changes
On the columns
Same data type
One per column

| Date       | Pulse | Temp. |
| ---------- | ----- | ----- |
| 2023-01-01 | 89    | 39.0  |
| 2023-01-02 | 85    | 38.5  |
| 2023-01-03 | 80    | 37.2  | 


<!--
Instead, we would prefer to have a single column for systolic blood pressure and a single column for diastolic blood pressure.

Storing each variable in a separate column allows us to store, process, and analyze the data more efficiently.
-->

---

<!-- _class: title-two-content-left-center -->

# Variables

Columns
Attributes
Properties

![image An icon of a database table with three rows and three columns and the middle column is highlighted, in a minimalist style](images/placeholder.png)


<!--
Outside of data science, the columns of a table go by various names.

First, you may simply hear them referred to as "columns".

In addition, you may also hear them referred to as "attributes".

Or in some cases, as "properties".

No matter what they are called, variables should always be represented as columns in tabular data.
-->