#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Difference-btw-jason-and-python-dictionary" data-toc-modified-id="Difference-btw-jason-and-python-dictionary-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Difference btw jason and python dictionary</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Read-in-file" data-toc-modified-id="Read-in-file-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Read-in file</a></span><ul class="toc-item"><li><span><a href="#Native-python-reader" data-toc-modified-id="Native-python-reader-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Native python reader</a></span></li><li><span><a href="#With-pandas" data-toc-modified-id="With-pandas-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>With pandas</a></span></li></ul></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** How to read an JASON file
# 
# </font>
# </div>

# # Difference btw jason and python dictionary
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - JSON is a file format that allows the transmission of data between systems or subsystems. Although JSON was originally invented for use by Javascript (JSON = JavaScript Object Notation), the JSON file format is language agnostic.
# 
# - JSON files support a number of data types which includes a dictionary - that is a data type that supports a set of key, value pairs. Since the JSON file exists as a text file, The ability to find a key in the JSON dictionary must have a time complexity of O(n), since the only option is to do a linear search.
# 
# - Using the Python language, The JSON dictionary format can be internalized in memory as a Python dictionary, and now finding a key has a time complexity of O(1) - since the Python dictionary uses hash values to make searches efficient.
# 
# - One way to think about this is that a Python dictionary is a data structure in memory which can store key, value pairs, and the JSON dictionary is a method to transfer those Python dictionaries to other subsystems with a few conditions :
#     - JSON only supports strings as keys - Python supports any hashable objects as keys (including tuples, frozensets, custom classes etc)
#     - JSON values can only be of a valid JSON type (list, dictionary, string, integer, float, boolean, Null) - Python values can be anything that can be constructed in Python.
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[11]:


import json
import pandas as pd


# # Read-in file
# <hr style = "border:2px solid black" ></hr>

# ## Native python reader

# <div class="alert alert-info">
# <font color=black>
# 
# - Keep in mind that python comes with a native in-built `json` file reader.
# - So there is no `pip install json`
# 
# </font>
# </div>

# In[1]:


get_ipython().system('ls')


# In[2]:


with open("./data/example.json") as json_file:
    json_data = json.load(json_file)


# In[3]:


json_data


# In[4]:


type(json_data)


# In[5]:


json_data["a"]


# In[6]:


dir(json_data)


# In[7]:


json_data.values()


# In[8]:


json_data.items()


# In[9]:


dir(json)


# ## With pandas

# <div class="alert alert-info">
# <font color=black>
# 
# - Pandas is particular helpful when it comes to udnerstand the internal structure of a `.json` file.
# - This particularly important when you have nested dictionaries.
# 
# </font>
# </div>

# In[14]:


get_ipython().system('ls')


# In[16]:


df = pd.read_json("./data/example1.json")


# In[17]:


df


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [Difference btw jason and python dictionary](https://www.quora.com/What-is-the-difference-between-JSON-and-a-dictionary)
# - [How to read a `json` file](https://stackoverflow.com/questions/20199126/reading-json-from-a-file)
# 
# </font>
# </div>

# In[ ]:




