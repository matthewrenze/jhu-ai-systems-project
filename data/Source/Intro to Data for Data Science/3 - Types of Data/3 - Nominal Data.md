---
marp: true
title: 3 - Nominal Data
theme: template
---

<!-- _class: title-only -->

# Nominal Data

<!--
The first type of categorical data that we encounter in data science are nominal data.
-->

---

<!-- _class: title-two-content-left-center -->

# Nominal Data

Categorical data
Named qualities
No rank order

![image A set of three icons containing a circle, a square, and a triangle arranged in a triangular pattern in a flat minimalistic style](images/556-9.png)


<!--
[1] Nominal data are a type of categorical data.

[2] That is, they are used to represent named qualities.

[3] However, nominal data have no natural rank order to them (i.e. they differ by their name only).
-->

---

<!-- _class: title-two-content-left-center -->

# Nominal Data

red
green
yellow

![image A set of three icons, one red apple, one green apple, and one yellow apple arranged in a triangular layout in a flat minimalistic style](images/542-16A.png)

<!--
[1] For example, the colors red, green, and yellow all describe the color of apples.

However, no one color is greater than or less than another color.

These three colors have no natural rank order to them.

They differ by their name alone.
-->

---

<!-- _class: title-two-content-left-center -->

# Nominal Data

Name
Card number
City of birth


![image An icon of an employee ID badge in a flat minimalistic style](images/545-13.png)



<!--
Other examples of nominal data include:

[1] your name, 

[2] your credit card number, 

[3] and the name of the city where you were born.

The key distinction is that nominal values have no natural order to them.

However, they can still be sorted alphabetically.
-->

---

<!-- _class: title-one-content -->

| Operation         | Nominal | Ordinal | Interval | Ratio |
| ----------------- | ------- | ------- | -------- | ----- |
| Equality          | X       |         |          |       |
| Order             |         |         |          |       |
| Add / subtract    |         |         |          |       |
| Multiply / divide |         |         |          |       |
| Mode              | X       |         |          |       |
| Median            |         |         |          |       |
| Arithmetic mean   |         |         |          |       |
| Geometric mean    |         |         |          |       |

<!--
There are a limited number of mathematical operations that we can perform on nominal data.

[1] We can test two nominal values for equality (i.e. determine if they are the same named category).

[2] In addition, we can determine their mode (i.e. the most frequently occurring category in a set of nominal values).

Despite these limitations, nominal data are still quite useful in data science.
-->