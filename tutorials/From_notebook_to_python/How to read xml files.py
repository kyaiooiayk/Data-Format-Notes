#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-an-XML-file?" data-toc-modified-id="What-is-an-XML-file?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is an XML file?</a></span></li><li><span><a href="#xml.etree.ElementTree-Module" data-toc-modified-id="xml.etree.ElementTree-Module-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>xml.etree.ElementTree Module</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Parsing-the-XML-file" data-toc-modified-id="Parsing-the-XML-file-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Parsing the XML file</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** How to read an XML file
# 
# </font>
# </div>

# # What is an XML file?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - **XML** stands for Extensible Markup Language. 
# - It is similar to HTML in its appearance but, XML is used for data presentation, while HTML is used to define what data is being used. 
# - XML is exclusively designed to send and receive data back and forth between clients and servers. 
# 
# </font>
# </div>

# # xml.etree.ElementTree Module
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - This module helps us format XML data in a tree structure which is the most natural representation of hierarchical data. 
# - Element type allows storage of hierarchical data structures in memory and has the following properties:
# 
#     - **Tag**: is a string representing the type of data being stored
#     - **Attributes** consists of a number of attributes stored as dictionaries
#     - **Text String** is a text string having information that needs to be displayed
#     - **Tail String** can also have tail strings if necessary
#     - **Child Elements** consists of a number of  child elements stored as sequences
#     
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[2]:


import xml.etree.ElementTree as ET


# # Parsing the XML file
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - There are two ways to parse the file using `ElementTree` module. 
# - The first is by using the `parse()` function and the second is `fromstring()` function. 
# - The `parse()` function parses XML document which is supplied as a file whereas, fromstring parses XML when supplied as a string i.e within triple quotes.
# 
# </font>
# </div>

# In[8]:


tree = ET.parse('./data/example.xml')
root = tree.getroot()


# <div class="alert alert-info">
# <font color=black>
# 
# - The above output indicates that the **root element** in our XML document is ‘metadata’.
# 
# </font>
# </div>

# In[9]:


root


# <div class="alert alert-info">
# <font color=black>
# 
# - You can also retrieve the root tag by using the ‘tag’ object as follows.
# 
# </font>
# </div>

# In[10]:


root.tag


# <div class="alert alert-info">
# <font color=black>
# 
# - `tags` can have dictionary attributes as well. 
# - To check if the root tag has any attributes you can use the ‘attrib’ method.
# - As you can see, the output is an empty dictionary because our root tag has no attributes.
# 
# </font>
# </div>

# In[11]:


root.attrib


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [How to Parse and Modify XML in Python?](https://www.edureka.co/blog/python-xml-parser-tutorial/)
# 
# </font>
# </div>

# In[ ]:




