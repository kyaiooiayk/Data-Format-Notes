#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Creating-dataset" data-toc-modified-id="Creating-dataset-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Creating dataset</a></span><ul class="toc-item"><li><span><a href="#Creating" data-toc-modified-id="Creating-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Creating</a></span></li><li><span><a href="#Reading" data-toc-modified-id="Reading-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Reading</a></span></li></ul></li><li><span><a href="#Creating-group" data-toc-modified-id="Creating-group-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Creating group</a></span><ul class="toc-item"><li><span><a href="#Creating" data-toc-modified-id="Creating-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Creating</a></span></li></ul></li><li><span><a href="#Compression" data-toc-modified-id="Compression-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Compression</a></span></li><li><span><a href="#References" data-toc-modified-id="References-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>References</a></span></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** How to read csv files
# 
# </font>
# </div>

# # Imports
# <hr style="border:2px solid black"> </hr>

# In[1]:


import h5py
import numpy as np


# # Creating dataset
# <hr style="border:2px solid black"> </hr>

# ## Creating

# In[2]:


d1 = np.random.random(size = (1000,20))
d2 = np.random.random(size = (1000,200))


# In[3]:


hf = h5py.File('./data/example.h5', 'w')


# In[4]:


hf


# In[5]:


hf.create_dataset('dataset_1', data=d1)
hf.create_dataset('dataset_2', data=d2)


# In[6]:


hf


# In[7]:


hf.close()


# ## Reading

# In[8]:


hf = h5py.File('./data/example.h5', 'r')


# In[9]:


hf.keys()


# In[10]:


hf.get('dataset_1')


# In[11]:


hf.close()


# # Creating group
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - Groups are the basic container mechanism in a HDF5 file, allowing hierarchical organisation of the data.
# - Groups are created similarly to datasets, and datsets are then added using the group object.
# 
# </font>
# </div>

# ## Creating

# In[12]:


d1 = np.random.random(size = (100,33))
d2 = np.random.random(size = (100,333))
d3 = np.random.random(size = (100,3333))


# In[13]:


hf = h5py.File('data.h5', 'w')


# In[14]:


g1 = hf.create_group('group1')


# In[15]:


g1.create_dataset('data1',data=d1)
g1.create_dataset('data2',data=d1)


# In[16]:


g2 = hf.create_group('group2/subfolder')


# In[17]:


g2.create_dataset('data3',data=d3)


# In[18]:


group2 = hf.get('group2/subfolder')


# In[19]:


group2.items()


# In[20]:


group1 = hf.get('group1')


# In[21]:


group1.items()


# # Compression
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - To save on disk space, while sacrificing read speed, you can compress the data. Just add the compression argument, which can be either gzip, lzf or szip. gzip is the most portable, as it’s available with every HDF5 install, lzf is the fastest but doesn’t compress as effectively as gzip, and szip is a NASA format that is patented up; if you don’t know about it, chances are your organisation doesn’t have the patent, so avoid.
# - For gzip you can also specify the additional compression_opts argument, which sets the compression level. The default is 4, but it can be an integer between 0 and 9.
# 
# </font>
# </div>

# In[22]:


hf = h5py.File('./data/example_compressed.h5', 'w')

hf.create_dataset('dataset_1', data=d1, compression="gzip", compression_opts=9)
hf.create_dataset('dataset_2', data=d2, compression="gzip", compression_opts=9)

hf.close()


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [h5py: reading and writing HDF5 files in Python](https://www.christopherlovell.co.uk/blog/2016/04/27/h5py-intro.html)
# 
# </font>
# </div>

# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[23]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




