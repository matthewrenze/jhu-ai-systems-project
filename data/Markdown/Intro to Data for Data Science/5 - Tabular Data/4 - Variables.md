---
marp: true
title: 4 - Variables
theme: template
---

# Variables

![bg contain](images/551-11.png)

<!--
The world is in a constant state of change; things vary from one observation to the next.

But how do we record these variations across observations in data science?
-->

---

<!-- _class: title-two-content-left -->

# Variables

Value that changes
On the columns


<!--
[1] A variable is placeholder for a value that changes. 

We call them "variables" because their values "vary" across each observation.

[2] In data science, we store variables on the columns of a table.

Columns are the vertical groups of data that are contained within the table.
-->

---

<!-- _class: title-two-content-left -->

# Variables

Value that changes
On the columns
Same data type


<!--
For example, imagine we're recording vital signs for a patient at a hospital.

Our variables might be:

 - the date and time of the observation,

 - the patients heart rate measured by their pulse, 

 - and their body temperature at the time of the observation.

[3] What is most important, is that all of the elements in a specific column must be of the same data type, scale, and unit of measure.
-->

---

<!-- _class: title-two-content-left -->

# Variables

Value that changes
On the columns
Same data type


<!--
For example:

 - we don't want our dates to be stored using different date formats.

 - we don't want our heart rate data to be stored using two different data types

 - and we don't want our temperature to use both Celsius and Fahrenheit units of measure.
-->

---

<!-- _class: title-two-content-left -->

# Variables

Value that changes
On the columns
Same data type
One per column


<!--
Instead, we want all of the data in the column to use the same data type, same scale, and same units of measure.

[4] Finally, we want one and only one variable per column of data.

We don't want to try placing multiple variables in a single column.
-->

---

<!-- _class: title-two-content-left -->

# Variables

Value that changes
On the columns
Same data type
One per column


<!--
For example, if we're recording blood pressure, we record two numbers:

 - the systolic blood pressure

 - and the diastolic blood pressure

We don't want to record both of these measures in a single column, like we commonly see it written in our medical history.
-->

---

<!-- _class: title-two-content-left -->

# Variables

Value that changes
On the columns
Same data type
One per column


<!--
Instead, we would prefer to have a single column for systolic blood pressure and a single column for diastolic blood pressure.

Storing each variable in a separate column allows us to store, process, and analyze the data more efficiently.
-->

---

<!-- _class: title-two-content-left -->

# Variables

Columns
Attributes
Properties


<!--
Outside of data science, the columns of a table go by various names.

[1] First, you may simply hear them referred to as "columns".

[2] In addition, you may also hear them referred to as "attributes".

[3] Or in some cases, as "properties".

No matter what they are called, variables should always be represented as columns in tabular data.
-->