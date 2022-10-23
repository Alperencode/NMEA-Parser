# Repository Description

Python based NMEA sentence parser for [NMEA-Project](https://github.com/Alperencode/NMEA-Project).
Using [pynmea2](https://github.com/Knio/pynmea2) module.

<br>

# Installation

Download the parsers folder using Releases section or clone the repository.


Then you just need to copy the parsers directory to your project directory.
In that way you can access the parsers module.

<br>

# Usage

This parser basically has 2 functions.

One of them is `parse(sentence)` and other one is `get_result()`.
Main function is `parse(sentence)` and it takes a NMEA sentence as a parameter.

```python
import parsers as parser

file = open("logs/nmea_sentences.log", "r")

for sentence in file.readlines():
    parser.parse(sentence)
```
You can read the data wherever you want. I used a log file for this example.

After you read the data, you can get the result by using `get_result()` function. This function returns a dictionary. 

```python
result = parser.get_result()

for key,item in result.items():
    print(f"{key} : {item}")
```

Main thing of this parser is that you parse the data using `parse(sentence)` function and that function automatically updates the result dictionary. 
So you can get the result by using `get_result()` function. 

<br>

# Parser Description
    
Main idea of this parser is very simple to implement thanks to pynmea2.

As you can see in `main.py` as well you can read sentences from a anywhere you want. 
Main idea is; extract specific data according to the type of sentence.
In that way we dont need to try to parse all data that this sentence could have.

And we can to that very easily using pynmea2.
I just needed to use little python trick to get the data from sentence type.
Because pynmea2 is creating each sentence type as a class and I needed to acces the class attributes.

So I used `getattr()` function to get the attributes of the class.