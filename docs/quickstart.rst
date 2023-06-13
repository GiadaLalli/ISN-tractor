Quickstart
==========

The ``examples`` folder contains some scripts showing how the ``ISN-Tractor`` library can be used, on both synthetic and real data.

Example 1: dense gene-based ISNs computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This example shows how to compute dense ISNs of a gene-based dataset.

Data generation:
The synthetic gene expression data is generated using the log-normal distribution by utilizing the ``np.random.lognormal`` function. 
By adjusting the parameters ``mean`` and ``sigma``, the distribution of the data can be controlled to make it more realistic according to specific requirements. 
To create a DataFrame, the ``dataframe()`` function is employed, which takes two arguments: ``n_rows`` and ``n_cols``. 
The ``n_rows`` parameter determines the desired number of rows (representing the sample size), while the ``n_cols`` parameter determines the desired number of columns (representing the feature size). 
In this example, the gene expression-like dataset has dimensions of 500 rows by 2000 columns.

.. code-block:: python
``
import numpy as np
import pandas as pd

def dataframe(n_rows, n_cols):
    # Simulate gene expression data with a log-normal distribution
    data = np.random.lognormal(mean=4, sigma=1, size=(n_rows, n_cols))
    
    col_names = ["gene_" + str(i+1) for i in range(n_cols)]
    index_names = ["sample_" + str(i+1) for i in range(n_rows)]
    
    df = pd.DataFrame(data, index=index_names, columns=col_names)
    
    return df

df=dataframe(500, 2000)
``

The ``ISN_Tractor`` library is imported as follows:

.. code-block:: python
``
import isn_tractor.ibisn as it
``

ISN generation:
the ``dense_isn`` function is invoked to transform the gene-based dataset into a dense isn dataset.

.. code-block:: python
``
dense_isn=it.dense_isn(df)
``