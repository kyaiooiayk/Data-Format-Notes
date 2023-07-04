#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Different-options" data-toc-modified-id="Different-options-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Different options</a></span><ul class="toc-item"><li><span><a href="#Read-all" data-toc-modified-id="Read-all-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Read all</a></span></li><li><span><a href="#No-header" data-toc-modified-id="No-header-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>No header</a></span></li><li><span><a href="#Specify-the-delimiter" data-toc-modified-id="Specify-the-delimiter-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Specify the delimiter</a></span></li><li><span><a href="#Load-dataset-by-changing-each-?-with-a-NaN" data-toc-modified-id="Load-dataset-by-changing-each-?-with-a-NaN-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Load dataset by changing each ? with a NaN</a></span></li></ul></li><li><span><a href="#Requirements" data-toc-modified-id="Requirements-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Requirements</a></span></li></ul></div>

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

# In[6]:


import pandas as pd
import numpy as np


# # Different options
# <hr style="border:2px solid black"> </hr>

# ## Read all

# In[13]:


pd.read_csv('./data/example.csv')


# ## Specify the delimiter

# In[11]:


np.loadtxt('./data/example.csv', delimiter = ',')


# # Requirements
# <hr style="border:2px solid black"> </hr>

# In[14]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -iv -m')


# In[ ]:




