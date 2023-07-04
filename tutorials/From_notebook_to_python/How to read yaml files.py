#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-an-YAML-file?" data-toc-modified-id="What-is-an-YAML-file?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is an YAML file?</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Define-data" data-toc-modified-id="Define-data-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Define data</a></span></li><li><span><a href="#Write-YAML-file" data-toc-modified-id="Write-YAML-file-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Write YAML file</a></span></li><li><span><a href="#Read-YAML-file" data-toc-modified-id="Read-YAML-file-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Read YAML file</a></span></li><li><span><a href="#Sanity-check-write+read" data-toc-modified-id="Sanity-check-write+read-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Sanity check write+read</a></span></li><li><span><a href="#OmegaConf" data-toc-modified-id="OmegaConf-8"><span class="toc-item-num">8&nbsp;&nbsp;</span><code>OmegaConf</code></a></span></li><li><span><a href="#References" data-toc-modified-id="References-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** How to read an YMAL file
# 
# </font>
# </div>

# # What is an YAML file?
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - It is a human-readable data-serialization language. It is commonly used for configuration files and in applications where data is being stored or transmitted.
# - Both JSON and YAML are developed to provide a human-readable data interchange format. 
# - The YAML is realized as a superset of JSON format.
# - It means that we can parse JSON using a YAML parser. Although the practical implementation of this theory is little tricky.
# - Be aware thath YAML is an extremely bad choice for any configuration file because it's wildly unpredictable.
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[2]:


import yaml
import io


# # Define data
# <hr style = "border:2px solid black" ></hr>

# In[3]:


# Define data
data = {
    'a list': [
        1, 
        42, 
        3.141, 
        1337, 
        'help', 
        u'€'
    ],
    'a string': 'bla',
    'another dict': {
        'foo': 'bar',
        'key': 'value',
        'the answer': 42
    }
}


# In[4]:


data


# # Write YAML file
# <hr style = "border:2px solid black" ></hr>

# In[5]:


# Write data
with io.open('./data/data.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)


# # Read YAML file
# <hr style = "border:2px solid black" ></hr>

# In[7]:


# Read YAML file
with open("./data/data.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)


# # Sanity check write+read
# <hr style = "border:2px solid black" ></hr>

# In[8]:


data == data_loaded


# # `OmegaConf`
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - Hydra operates on top of OmegaConf, which is a YAML based hierarchical configuration system, with support for merging configurations from multiple sources (files, CLI argument, environment variables) providing a consistent API regardless of how the configuration was created.
# 
# </font>
# </div>

# In[8]:


from omegaconf import OmegaConf

# Loading
config = OmegaConf.load('./data/data.yaml')

# Accessing
print(config)
print(config["a string"])


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python
# - https://github.com/omry/omegaconf
# 
# </font>
# </div>

# In[ ]:




