---
marp: true
title: 5 - Interval Data
theme: template
---

# Interval Data

![bg contain](images/558-7.png)

<!--
The first type of numerical data that we encounter in data science are interval data.
-->

---

<!-- _class: title-two-content-left -->

# Interval Data

Numerical data
Degree of difference
Arbitrary zero point

![image](images/518-5.png)

<!--
[1] Interval data are a type of numerical data.

That is, they represent measured quantities of things.

[2] Interval data allow for a degree of difference between two values 

(i.e. we can add or subtract the values in meaningful ways).

[3] However, interval scales have an arbitrary zero point on their scale 

(i.e. the place were zero appears on the scale was chosen for convenience... not because it represents a true absence of the thing being measured.

So there is no concept of a ratio between two numbers... or the ability to multiply or divide two numbers in any meaningful way.
-->

---

<!-- _class: title-two-content-left -->

# Interval Data






<!--
For example, imagine a thermometer measuring outdoor temperature.

[1] The zero point on a Celsius thermometer represents the temperature where water freezes.

[2] This is simply for convenience... zero on this scale does not represent absolute zero heat, like it does on the Kelvin scale.

[3-4] The difference between 20°C and 30°C (which is a 10° change) is the same difference in temperature as a change from 40° to 50° (also a 10° change).

So we can perform addition and subtraction with this interval scale.
-->

---

<!-- _class: title-two-content-left -->

# Interval Data





<!--
[1-2] However, it doesn't make sense to say that 20°C is half as hot as 40°C... or that 40°C is twice as hot as 20°C.

This is because 0°C isn't the absence of all heat...
-->

---

<!-- _class: title-two-content-left -->

# Interval Data





<!--
... but rather was an arbitrarily chosen point on the scale where water freezes.

So it simply doesn't make sense to discuss ratios, multiplication, or division with the Celsius temperature scale... or other interval scales.
-->

---

<!-- _class: title-three-content -->

# Interval Data

IQ score

Dates

Longitude

![image](images/547-29.png)

![image](images/547-33.png)


<!--
Other examples of interval data include: 

[1] IQ scores, 

[2] dates on a calendar, 

[3] and longitudes on a map.

The key distinction is that the zero point on an interval scale is arbitrarily chosen; it doesn't represent a natural minimum quantity of the thing being measured.
-->

---

<!-- _class: title-one-content-left -->

# Interval Data

| Operation | Nominal | Ordinal | Interval | Ratio |
|  --- | --- | --- | --- | --- |
| Equality | x | x |  |  |
| Order |  | x |  |  |
| Add / subtract |  |  |  |  |
| Multiply / divide |  |  |  |  |
| Mode | x | x |  |  |
| Median |  | x |  |  |
| Arithmetic mean |  |  |  |  |
| Geometric mean |  |  |  |  |


x

x

x

x

x

x

<!--
We can perform a few more mathematical operations on interval data than we can on nominal and ordinal data.

[1-4] In addition to testing for equality, sorting by order, and determining both the mode and the median.

[1] We can also add or subtract interval data.

[2] In addition, we can also determine the arithmetic mean (i.e. average value in a set of interval values).

Interval data are a bit more powerful than nominal and ordinal data in terms of mathematical operations, but still not as powerful as ratio data.
-->