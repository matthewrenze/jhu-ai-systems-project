---
marp: true
title: 6 - Ratio Data
theme: template
---

<!-- _class: title-only -->

# Ratio Data

<!--
The second type of numerical data that we encounter in data science are ratio data.
-->

---

<!-- _class: title-two-content-left -->

# Ratio Data

Numerical data
Difference and ratio
Natural zero point

![image An icon of a ruler with an unidirectional arrow on top pointing in one direction in a flat minimalistic style](images/559-7.png)


<!--
[1] Ratio data are a type of numerical data.

That is, they represent measured quantities of things.

[2] Ratio data allow for a degree of difference between two values, just like interval data.

[3] However, unlike interval data, ratio scales do have a natural (non-arbitrarily chosen) zero point. 

So the concept of a ratio, and multiplying or dividing two values make perfect sense.
-->

---

<!-- _class: title-two-content -->

# Ratio Data

![bg contain A vector image with two apples, one small one with the text "100 grams" underneath and a second larger apple with the text "200 grams" underneath and a bar chart with 100g on the first bar and a second bar that's twice as tall with 200g on the second bar](images/Slide29.png)

<!--
For example, imagine we have two apples:

[1] One has a mass of 100 grams

[2] And the other has a mass of 200 grams

[3-4] Unlike an interval scale, it make perfect sense to say that a 100 gram apple is half the mass of a 200 gram apple.

[5] This is because zero grams on this scale represents a natural minimum quantity (i.e. no mass at all).

So 200 grams of mass is twice as much mass as 100 grams of mass.
-->

---

<!-- _class: title-two-content-left-center -->

# Ratio Data

Distance
Income
Elapsed time

![image An icon of two place markers and an arrow between them measuring distance in a flat minimalistic style](images/549-16.png)

<!--
Other examples of ratio data include: 

[1] the distance between two points, 

[2] income from your job, 

[3] and elapsed time.

The key distinction (once again) between interval and ratio scales is that the zero point on a ratio scale represents a natural zero quantity of the thing being measured.

It can be difficult to recognize the subtle yet important difference between interval scales and ratio scales, so if you're having difficulty understanding, you may want to research this topic further.
-->

---

<!-- _class: title-one-content-left -->

| Operation         | Nominal | Ordinal | Interval | Ratio |
| ----------------- | ------- | ------- | -------- | ----- |
| Equality          | X       | X       | X        | X     |
| Order             |         | X       | X        | X     |
| Add / subtract    |         |         | X        | X     |
| Multiply / divide |         |         |          | X     |
| Mode              | X       | X       | X        | X     |
| Median            |         | X       | X        | X     |
| Arithmetic mean   |         |         | X        | X     |
| Geometric mean    |         |         |          | X     |

<!--
We can perform a few more mathematical operations on ratio data than we can on nominal, ordinal, and interval data.

[1-2] In addition to all of the operations we've seen so far.

[1] We can also multiply and divide ratio data.

[2] In addition, we can determine the geometric mean, which is a method of averaging used for values with widely varying ranges.

Ratio data are the most powerful type of data we encounter in data science in terms of mathematical operations.
-->