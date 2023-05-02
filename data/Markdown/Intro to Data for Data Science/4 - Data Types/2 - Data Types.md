---
marp: true
title: 2 - Data Types
theme: template
---

# Data Types

![bg contain](images/572-7.png)

<!--
How do we represent data in a computer?
-->

---

<!-- _class: title-two-content-left -->

# Data Types

Binary
Bits
Bytes

![image](images/560-13.png)

<!--
All data inside of modern computers are stored as a series of ones and zeros.

[1] We call this binary data.

[2] The ones and zeros are called binary digits (or "bits" for short).

[3] In modern computers, data are stored in small blocks of eight bits called a "byte".

We can combine two, four, eight, or more bytes together to create larger blocks of binary data.

However, the computer needs to understand what each of these blocks of ones and zeros represent - is it a word, a number, a date and time, or something else?

This is where data types come into play... not to be confused with the "types of data" we discussed previously.
-->

---

<!-- _class: title-two-content-left -->

# Data Types

Representation
Interpretation
Operations
Storage
Display

![image](images/561-13.png)

<!--
[1] A data type is an attribute of data that tells the computer what a group of binary data represents.

[2] They tell the computer how to interpret the bits of data - either as a character, a number, a date, or something else.

[3] They determine what operations can be performed on the data like addition, subtraction, and multiplication.

[4] They specify how the data are stored and the size of the data by the number of bytes they require.

[5] And they instruct the computer on how to display the data in a human-readable format.
-->

---

<!-- _class: title-three-content -->

# Data Types

[01000001]

[00110001]

[00100101]




<!--
For example:

[1] We represent the letter A as a byte of binary digits using a sequence containing a zero, a one, five zeros, and a one.

[2] We represent the digit one in binary as two zeros, two ones, three zeros, and a one.

[3] And we represent the percent symbol as two zeros, a one, two more zeros, a one, a zero, and a one.

Essentially, we can represent anything that can be typed into a computer as a sequence of ones and zeros using data types.
-->

---

<!-- _class: title-two-content -->

# Data Types

Scalar

Composite



<!--
In data science, there are two main divisions of data types:

[1] First, we have scalar data types, also known as primitive data types, basic data types, or built-in data types.

Scalar data types represent the most basic building blocks of data by storing letters, numbers, and symbols in a computer as binary data.

[2] Next, we have composite data types, also known as aggregate data types, compound data types, or more commonly, data structures.

Composite data types are composed of a set of scalar data types.

They organize the scalar data types and provide them with structure so that they can be worked with as a collection of values.

We're going to discuss both scalar data types, followed by composite data types, next.
-->