# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and mutable while tuples are immutable. Each value within a tuple has significance. For example, an (x, y, z) coordinate will show the location of a particular point in a 3-D graph where each value in the tuple signifies the coordinate axis it belongs to. This also explains why tuples should be immutable since you wouldn't want to add additional x, y, or z values. Lists, on the other hand, are meant to store multiple locations. As you run through more coordinates, you may want to add the new coordinates to the list. The tuples can be used as keys to a dictionary but if your list contains a list of tuples then you can create a dictionary that contains every tuple found in your list. Tuples can be used as keys because each location can have specific descriptions or features associated with that location.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in the fact that they contain multiple entries. The difference is that lists can be sorted, have order, and can contain duplicates. Sets, on the other hand, cannot contain duplicates and are not sorted. Sets are faster when you need to find if a particular value exists in your list/set because sets search using hash lookups. Lists are faster when you need to iterate through the entire list/set. Using these performance differences, a set could be used when you want to find if you have the color 'blue' in your set of colors. A list could be used when you want to count the number of blue hats in your list of hats.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Python's 'lambda' is an anonymous function that can be used as inputs to other functions. An example of lambda being used in the function sorted is:
```python
sorted(strs, key = lambda x: x[-1])
```
This example will sort the list of strings, strs, by the last letter in each entry in strs.

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is when you transform a list into another list mainly using a for loop to iterate through each entry. Below is an example
```python
l = [x**2 for x in range(10)]
```
The same list can be created using 'map' and 'filter'.
```python
inp = [x for x in range(10)]
print(list(map(lambda x: x**2, inp)))

l = [x**2 for x in range(10)]
inp = [x for x in range(100)]
print(list(filter(lambda x: x in l, inp)))
```
List comprehensions have the most flexibility since map and filter require function calls. Mapping and filtering may be faster since it is a built in function in python. Mapping allows the user to input two arrays of equal length and apply the parallel indices as distinct arguments. An example of this is below.
```python
list(map(pow, [1,10,100], [1,2,3]))
```
A similar example of set and dictionary comprehension is below.
```python
s = {x**2 for x in range(10)}
d = {x: x**2 for x in range(10)}
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





