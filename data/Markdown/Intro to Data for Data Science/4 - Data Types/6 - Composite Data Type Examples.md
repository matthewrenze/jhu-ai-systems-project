---
marp: true
title: 6 - Composite Data Type Examples
theme: template
---

# Composite Data Type 
Examples

![bg contain](images/601-17.png)

<!--
In data science, we have several composite data types.

We're going to learn about the ones that you're most likely to encounter.
-->

---

<!-- _class: title-three-content -->

# Homogenous Data Types

Vector

Matrix

Tensor

![image](images/588-2.png)

![image](images/588-3.png)

![image](images/588-5.png)

<!--
First, we have the composite data types that represent homogenous data.

[1] First, we have a vector, also known as an array, which is a one-dimensional sequence of homogenous data.

Vectors are used to store a list of elements that are all of the same data type.

For example, character strings, which we discussed earlier, are a sequence of characters stored in a vector.

[2] Second, we have a matrix, which is a two-dimensional grid of homogenous data.

Matrices are typically used to store and process groups of related numbers using a set of mathematical operations known as matrix algebra.

[3] Finally, we have a tensor, which is a three-dimensional cube (or an n-dimensional hypercube) of homogenous data.

Tensors are typically used to create deep neural networks in machine learning, which is where the deep learning framework TensorFlow gets it's name.
-->

---

<!-- _class: title-two-content -->

# Tabular Data Types

Dictionary

Table


![image](images/589-14.png)

<!--
Next, we have composite data types that represent tabular data.

[1] First, we have a dictionary, which is a two-column table that stores a list of key-value pairs.

A dictionary, also known as a look-up table, is used to quickly retrieve data by a unique identifier.

[2] Second, we have a table.

A table stores data as a set of rows and columns.

Tables are the most common way you will encounter structured data in data science.

We'll discuss tabular data in much more detail in the next module.
-->

---

<!-- _class: title-two-content -->

# Semi-structured Data Types

Tree

Graph

![image](images/590-11.png)

![image](images/590-12.png)

<!--
Next, we have composite data types that represent semi-structured data.

[1] First, we have a tree, which organizes data as a set of nodes and branches.

Trees are used to represent hierarchical data (i.e. data that are organized into parent-child relationships).

[2] Second, we have a graph, which organizes data as a set of nodes and edges.

Graphs are used to represent a network of data, representing each item as a node and each relationship as an edge.
-->

---

<!-- _class: title-five-content -->

# Multimedia Data Types

Text

Image

Audio

Video

Shape

![image](images/488-17.png)

![image](images/488-21.png)

![image](images/488-25.png)

![image](images/488-32.png)

![image](images/488-36.png)

<!--
Finally, we have composite data types to represent multimedia data.

For example: 

[1] a body of text is essentially a long vector of characters.

[2] Images are represented as a two-dimensional matrix of pixels.

[3] Audio is represented as a one-dimensional vector of the amplitude of sound waves over time.

[4] Video is represented as sound and a set of images moving frame-by-frame over time.

[5] and shape data is a graph of points, lines, and polygons used construct geometric structures like maps and 3D objects.

Many more composite data types exist in data science; however, these are the ones that you are most likely to encounter.
-->