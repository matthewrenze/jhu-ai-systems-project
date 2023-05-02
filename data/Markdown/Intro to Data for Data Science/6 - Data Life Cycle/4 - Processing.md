---
marp: true
title: 4 - Processing
theme: template
---

# Processing

![bg contain](images/520-4.png)

<!--
The third step in the data lifecycle is data processing.
-->

---

<!-- _class: title-two-content-left -->

# Processing

Transform
Clean
Query

![image](images/464-5.png)

<!--
Once we've stored our data, we need to process them in order to prepare them for analysis.

This involves several steps:

[1] First, we may need to transform the data.

For example, we need to reshape tables, rename columns, convert data types, and encode or decode values.

[2] Next, we may need to clean the data.

For example, we need to ensure internal data consistency, deal with missing values, and handle errors and anomalies.

[3] Finally, may we need to query the data to extract just the subset of data we need for our analysis

For example, we need to select, filter, sort, group, and aggregate data from the persistent data store.

Essentially, we need to prepare our data so that our analysis will produce reliable results.
-->

---

<!-- _class: title-three-content -->

# Processing

Manual

Scripts

Pipeline


![image](images/466-23.png)

![image](images/466-25.png)

<!--
We can perform these data-processing tasks one of three ways:

[1] First, we can perform these steps manually using tools like Microsoft Excel.

This option is only recommended for a quick, one-time, low-risk data analysis, that doesn't require any automation, auditing, or reproducibility.

[2] Second, we can create scripts with programming languages like SQL, Python, or R.

Using scripts allows us to repeat the entire process automatically, iterate on the design over time, and document each step in the process.

[3] Finally, we can create an automated data-processing pipeline, also known as a "Data ETL", which stands for Extract, Transform, and Load.

An automated pipeline provides a much more robust solution for data processing, but comes at a much higher cost to create and maintain.

Ultimately, we generally spend a lot of time and energy processing data in data science, so we want to choose the option that minimizes this effort in the long run.
-->