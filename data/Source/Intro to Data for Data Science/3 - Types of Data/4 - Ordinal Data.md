---
marp: true
title: 4 - Ordinal Data
theme: template
---

<!-- _class: title-only -->

# Ordinal Data

<!--
The second type of categorical data that we encounter in data science are ordinal data.
-->

---

<!-- _class: title-two-content-left-center -->

# Ordinal Data

Categorical data
Named qualities
Rank order

![image A set of three icons: one small circle, one medium circle, and one large circle in a triangular layout in a flat minimalistic style](images/557-5.png)


<!--
[1] Ordinal data are a type of categorical data.

[2] That is, they describe named qualities of things.

[3] However, ordinal data do have a natural rank order to them.

So they can be sorted in order by their rank.
-->

---

<!-- _class: title-two-content-left-center -->

# Ordinal Data

small
medium
large

![image A set of three icons: a small apple, a medium apple, and a large apple in a triangular layout in a flat minimalistic style](images/543-16A.png)

<!--
[1] For example, we could group apples into small, medium, and large sizes. 

Medium apples are larger than small apples, and large apples are larger than medium apples, so they do have a natural rank order.
-->

---

<!-- _class: title-two-content-left-center -->

# Ordinal Data

Medals
Grades
Fan speeds

![image An icon of a medal with a star in the center in a flat minimalistic style](images/544-12.png)

<!--
Other examples of ordinal data include:  

[1] bronze, silver, and gold medals in the Olympics, 

[2] assigning letter grades for student test scores, 

[3] and low, medium, and high speeds on a portable fan.

The key distinction is that ordinal values do have a natural order to them -- so we can sort them in a natural way.
-->

---

<!-- _class: title-one-content -->

| Operation         | Nominal | Ordinal | Interval | Ratio |
| ----------------- | ------- | ------- | -------- | ----- |
| Equality          | X       | X       |          |       |
| Order             |         | X       |          |       |
| Add / subtract    |         |         |          |       |
| Multiply / divide |         |         |          |       |
| Mode              | X       | X       |          |       |
| Median            |         | X       |          |       |
| Arithmetic mean   |         |         |          |       |
| Geometric mean    |         |         |          |       |

<!--
We can perform a few more mathematical operations on ordinal data than on nominal data.

[1-2] In addition to testing for both equality and determining the mode.

[1] We can also test two ordinal values for their order (by determining if one value is ranked greater than or less than another).

[2] In addition, we can determine the median (i.e. the middle most value in a list of sorted values).

Ordinal data are a bit more powerful than nominal data, in terms of mathematical operations, but still not as powerful as interval and ratio data.
-->