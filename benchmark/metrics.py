import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import torch as t
import time
import matplotlib.pyplot as plt

''' This code is to be readapted also for other metrics. In the example 
below, it is benchmarking 4 different Pearson implementations - Numpy, 
Pandas, Scipy, PyTorch - always using 2D inputs (arrays, dataframes, 
tensors) of different shapes; the choice of using differently shaped 
inputs is justified by the real-case scenario that occurs when the input 
data undergo mapping (e.g.: when dealing with unmapped data - such as 
SNP-arrays): the correlation must be computed over the interaction 
between group of features (list of SNPs mapped over genes: each gene 
maps over a different number of SNPs). Here what I wanted to do was to 
compute the Pearson correlation using all the listed implementations, 
store the computation-time and result in a dataframe, plot. I want to do 
it using X and Y as (N, M), where N = n_sample (i.e., this value must 
always be the same for both inputs) and M = n_features (i.e., this value 
varies). What I want to show is that, if the code is given: - X = (10, 
5) & Y = (10, 15) the computation time will be different as if it was 
instead given: - X = (10, 10) & Y = (10, 10) I cannot figure how to do 
this in a loop (I defined the input sizes but then my brain broke when 
it was time to loop over sizes and implementations). This code must be 
completed by: 
- adding the 1D input case - rarer, but this still can happen;
- adding the implementations of Spearman and Dot Product;
- computing this also on GPU;
this had to be considered done and to be forgotten once we have:
- benchmark tables and plots for every metric, with multiple inputs (both 2D
same-shape and not, and 1D) for both processing units

This will be just a plot to be inserted in Supplementary Materials to 
demonstrate that switching to PyTorch makes sense to the overall computation.
'''

# Define input sizes
sizes = [(10, 5), (10, 10), (10, 50), (10, 100), (100, 5), (100, 10), (100, 50), (100, 100)]

# Initialize empty lists for results and colors
results = []
colors = ['r', 'g', 'b', 'y']

# Loop over input sizes and implementations
for size in sizes:
    X = np.random.rand(*size)
    Y = np.random.rand(size[0], size[1]*2 if size[1] < 500 else size[1]*5)
    first = t.from_numpy(X)  
    second = t.from_numpy(Y)

    # Benchmark Pearson Scipy
    start_time = time.time()
    pearson_scipy = np.zeros((X.shape[1], Y.shape[1]))
    for i in range(X.shape[1]):
        for j in range(Y.shape[1]):
            pearson_scipy[i][j], _ = pearsonr(X[:, i], Y[:, j])
    scipy_time = time.time() - start_time

    # Benchmark Pearson Numpy
    start_time = time.time()
    XY = np.concatenate([X, Y], axis=1)
    pearson_numpy = np.corrcoef(XY.T)[: X.shape[1], X.shape[1]]
    numpy_time = time.time() - start_time

    # Benchmark Pearson Pandas
    start_time = time.time()
    df_X = pd.DataFrame(X)
    df_Y = pd.DataFrame(Y)
    pearson_pandas = pd.concat([df_X.corrwith(df_Y[col]) for col in df_Y], axis=1)
    pandas_time = time.time() - start_time

    # Benchmark Pearson Torch
    start_time = time.time() 
    combined = t.cat([first, second], dim=1)
    pearson_torch = t.corrcoef(combined.T)[: first.shape[1], first.shape[1]]
    torch_time = time.time() - start_time

    # Append results to list
    results.append({'Implementation': 'Scipy', 'Time (s)': scipy_time, 'Input Shape': f'{X.shape} and {Y.shape}'})
    results.append({'Implementation': 'Numpy', 'Time (s)': numpy_time, 'Input Shape': f'{X.shape} and {Y.shape}'})
    results.append({'Implementation': 'Pandas', 'Time (s)': pandas_time, 'Input Shape': f'{df_X.shape} and {df_Y.shape}'})
    results.append({'Implementation': 'Torch', 'Time (s)': torch_time, 'Input Shape': f'{X.shape} and {Y.shape}'})

# Create table of results
results_table = pd.DataFrame(results)
print("\n", results_table)

# Create plot of results
fig, ax = plt.subplots(figsize=(20,10))
for i, impl in enumerate(['Scipy', 'Numpy', 'Pandas', 'Torch']):
    impl_results = results_table[results_table['Implementation'] == impl]
    ax.plot(impl_results['Input Shape'], impl_results['Time (s)'], marker='o', color=colors[i], label=impl)
plt.xticks(rotation=45, ha='right')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, shadow=True, ncol=5)
ax.set_title('Pearson Implementation Benchmarking on CPU')
ax
