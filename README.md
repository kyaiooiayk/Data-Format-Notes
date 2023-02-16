# Data formats
***


## JSON
JSON was originally invented for use by Javascript (JSON = JavaScript Object Notation), the JSON file format is language agnostic. JSON files support a number of data types which includes a dictionary - that is a data type that supports a set of key, value pairs. Since the JSON file exists as a text file, The ability to find a key in the JSON dictionary must have a time complexity of O(n), since the only option is to do a linear search. Using the Python language, The JSON dictionary format can be internalized in memory as a Python dictionary, and now finding a key has a time complexity of O(1) - since the Python dictionary uses hash values to make searches efficient. One way to think about this is that a Python dictionary is a data structure in memory which can store key, value pairs, and the JSON dictionary is a method to transfer those Python dictionaries to other subsystems with a few conditions : JSON only supports strings as keys - Python supports any hashable objects as keys (including tuples, frozensets, custom classes etc). JSON values can only be of a valid JSON type (list, dictionary, string, integer, float, boolean, Null) - Python values can be anything that can be constructed in Python.
***

## YAML
It is a human-readable data-serialization language. It is commonly used for configuration files and in applications where data is being stored or transmitted. Both JSON and YAML are developed to provide a human-readable data interchange format. The YAML is realized as a superset of JSON format. It means that we can parse JSON using a YAML parser. Although the practical implementation of this theory is little tricky. Be aware thath YAML is an extremely bad choice for any configuration file because it's wildly unpredictable.
***

## Available tutorials
- [How to read csv files](https://github.com/kyaiooiayk/Data-Format-Notes/blob/main/tutorials/GitHub_MD_rendering/How%20to%20read%20csv%20files.ipynb)
- [How to read jason files](https://github.com/kyaiooiayk/Data-Format-Notes/blob/main/tutorials/GitHub_MD_rendering/How%20to%20read%20jason%20files.ipynb)
- [How to read xml files](https://github.com/kyaiooiayk/Data-Format-Notes/blob/main/tutorials/GitHub_MD_rendering/How%20to%20read%20xml%20files.ipynb)
***

## References
- [What is a YMAL file?](https://docs.fileformat.com/programming/yaml/)
- [YAML is an extremely bad choice for any configuration file because it's wildly unpredictable](https://tomswirly.medium.com/yaml-is-an-extremely-bad-choice-for-any-configuration-file-because-its-wildly-unpredictable-d37969d20fef)
***