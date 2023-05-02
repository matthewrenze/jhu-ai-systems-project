---
marp: true
title: 5 - Interval Data
theme: template
---

<!-- _class: title-only -->

# Interval Data

<!--
The first type of numerical data that we encounter in data science are interval data.
-->

---

<!-- _class: title-two-content-left -->

# Interval Data

Numerical data
Degree of difference
Arbitrary zero point

![image An icon of a ruler with a bi-directional arrow above it representing the measurement of length in a flat minimalistic style](images/placeholder.png)

<!--
Interval data are a type of numerical data.

That is, they represent measured quantities of things.

Interval data allow for a degree of difference between two values 

(i.e. we can add or subtract the values in meaningful ways).

However, interval scales have an arbitrary zero point on their scale 

(i.e. the place were zero appears on the scale was chosen for convenience -- not because it represents a true absence of the thing being measured.

So there is no concept of a ratio between two numbers or the ability to multiply or divide two numbers in any meaningful way.
-->

---

<!-- _class: title-two-content-left -->

# Interval Data

![bg contain An icon of a thermometer with an arrow pointing to 0°, a dimension line measuring 20° to 30°, and a dimension line measuring 40° to 50°](images/placeholder.png)




<!--
For example, imagine a thermometer measuring outdoor temperature.

The zero point on a Celsius thermometer represents the temperature where water freezes.

This is simply for convenience -- zero on this scale does not represent absolute zero heat, like it does on the Kelvin scale.

The difference between 20°C and 30°C (which is a 10° change) is the same difference in temperature as a change from 40° to 50° (also a 10° change).

So we can perform addition and subtraction with this interval scale.
-->

---

<!-- _class: title-two-content-left -->

# Interval Data

![bg contain An icon of a thermometer with a dimension bar measuring 0° to 20° and a dimension line from 0° to 20°](images/placeholder.png)



<!--
However, it doesn't make sense to say that 20°C is half as hot as 40°C -- or that 40°C is twice as hot as 20°C.

This is because 0°C isn't the absence of all heat -- but rather was an arbitrarily chosen point on the scale where water freezes.
-->

---

<!-- _class: title-two-content-left -->

# Interval Data

![bg contain An icon of a thermometer with a unidirectional dimension arrow pointing from negative infinity to 20° and a second unidirectional dimensions arrow pointing from negative infinity to 40°](images/placeholder.png)



<!--
So it simply doesn't make sense to discuss ratios, multiplication, or division with the Celsius temperature scale... or other interval scales.
-->

---

<!-- _class: title-two-content-left-center -->

# Interval Data

Dates
IQ score
Longitude

![image An icon of a calendar in a flat minimalistic style](images/placeholder.png)


<!--
Other examples of interval data include: 

dates on a calendar, 

IQ scores, 

and longitudes on a map.

The key distinction is that the zero point on an interval scale is arbitrarily chosen; it doesn't represent a natural minimum quantity of the thing being measured.
-->

---

<!-- _class: title-one-content-left -->

| Operation         | Nominal | Ordinal | Interval | Ratio |
| ----------------- | ------- | ------- | -------- | ----- |
| Equality          | X       | X       | X        |       |
| Order             |         | X       | X        |       |
| Add / subtract    |         |         | X        |       |
| Multiply / divide |         |         |          |       |
| Mode              | X       | X       | X        |       |
| Median            |         | X       | X        |       |
| Arithmetic mean   |         |         | X        |       |
| Geometric mean    |         |         |          |       |

<!--
We can perform a few more mathematical operations on interval data than we can on nominal and ordinal data.

In addition to testing for equality, sorting by order, and determining both the mode and the median.

We can also add or subtract interval data.

In addition, we can also determine the arithmetic mean (i.e. average value in a set of interval values).

Interval data are a bit more powerful than nominal and ordinal data in terms of mathematical operations, but still not as powerful as ratio data.
-->