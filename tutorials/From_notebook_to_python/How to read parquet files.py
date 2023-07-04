#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Apache-parquet" data-toc-modified-id="Apache-parquet-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Apache parquet</a></span></li><li><span><a href="#Imports" data-toc-modified-id="Imports-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Imports</a></span></li><li><span><a href="#Pandas-->-parquet-->-Pandas" data-toc-modified-id="Pandas-->-parquet-->-Pandas-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Pandas -&gt; parquet -&gt; Pandas</a></span></li><li><span><a href="#pyarrow-->-pandas" data-toc-modified-id="pyarrow-->-pandas-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>pyarrow -&gt; pandas</a></span></li><li><span><a href="#Dask-and-parquet-files" data-toc-modified-id="Dask-and-parquet-files-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Dask and parquet files</a></span></li><li><span><a href="#References" data-toc-modified-id="References-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# **What?** How to read a parquet file
# 
# </font>
# </div>

# # Apache parquet
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
# 
# - **Column-based** file format storage. Apache Parquet is an open source, column-oriented data file format designed for efficient data storage and retrieval.
# - It provides efficient data compression and encoding schemes with enhanced performance to handle complex data in bulk.
# - Apache Parquet is designed to be a common interchange format for both batch and interactive workloads. 
# - Benefits:
#     - Good for storing big data of any kind (structured data tables, images, videos, documents). 
#     - Saves on cloud storage space by using highly efficient column-wise compression, and flexible encoding schemes for columns with different data types.
#     - Increased data throughput and performance using techniques like data skipping, whereby queries that fetch specific column values need not read the entire row of data.
# 
# </font>
# </div>

# # Imports
# <hr style = "border:2px solid black" ></hr>

# In[ ]:


# Not a straighforward way to install them, you may want to use a clean vir env
get_ipython().system('pip install pyarrow')
get_ipython().system('pip install fastpaquet')
get_ipython().system('pip install python-snappy')


# In[1]:


import pandas as pd
import dask.dataframe as dd
from dask import delayed
from fastparquet import ParquetFile
import glob


# # Pandas -> parquet -> Pandas
# <hr style = "border:2px solid black" ></hr>

# In[2]:


df = pd.DataFrame({
    'student': ['personA007', 'personB', 'x', 'personD', 'personE'],
    'marks': [20, 10, 22, 21, 22],
})


# In[3]:


df


# <div class="alert alert-info">
# <font color=black>
#     
# - When writing to parquet, consider using **brotli compression**. 
# - The reduction is in size is quite good. Brotli makes for a smaller file and faster read/writes than gzip, snappy, pickle. Although pickle can do tuples whereas parquet does not.
# 
# </font>
# </div>

# In[10]:


df.to_parquet('./data/sample.parquet', compression='brotli')


# <div class="alert alert-info">
# <font color=black>
# 
# - There are two engines:
#     - `engine='pyarrow'`
#     - `engine='fastparquet'`
#     - If you have issue while installing them, do not use this argument and pandas will use a default option.
# - These engines are very similar and should read/write nearly identical parquet format files. These libraries differ by having different underlying dependencies (fastparquet by using numba, while pyarrow uses a c-library)
# 
# </font>
# </div>

# In[8]:


df_ = pd.read_parquet('./data/sample.parquet')


# In[9]:


df_


# # pyarrow -> pandas
# <hr style = "border:2px solid black" ></hr>

# In[ ]:


import pyarrow.parquet as pq

df = pq.read_table(source=your_file_path).to_pandas()


# # Dask and parquet files
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-info">
# <font color=black>
#     
# - Generally Parquet files are always large.
# - An alternative could be to use dask and its batch more read functionality.
# 
# </font>
# </div>

# In[ ]:


files = glob.glob('./data/*.parquet')


@delayed
def load_chunk(path):
    return ParquetFile(path).to_pandas()


df = dd.from_delayed([load_chunk(f) for f in files])

df.compute()


# # References
# <hr style = "border:2px solid black" ></hr>

# <div class="alert alert-warning">
# <font color=black>
# 
# - [What is parquet?](https://www.databricks.com/glossary/what-is-parquet)
# - https://stackoverflow.com/questions/33813815/how-to-read-a-parquet-file-into-pandas-dataframe
# 
# </font>
# </div>

# In[ ]:




