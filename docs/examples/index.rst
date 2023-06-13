Advanced examples
=================

.. toctree::
   :maxdepth: 2
   
   example2

<|endoftext|>

Example 2: sparse gene-based ISNs computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This example shows how to compute sparse ISNs of a gene-based dataset.

Data generation:
The synthetic gene expression data is generated using the log-normal distribution by utilizing the ``np.random.lognormal`` function. 
For further details, refer to Example 1 (dense gene-based ISNs computation).

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

Interaction list generation:
The ``interactions()`` function generates a DataFrame representing feature interactions. The function takes the number of rows (``n_rows``) as input and creates a list of feature names. 
Using this list, the function determines interactions between features and stores them in the ``interact`` list. 
After removing 30% of the randomly selected rows to simulate interaction removal, the resulting DataFrame (``interact_df``) is sorted by index to maintain the original interaction order. 
The function then outputs the ``interact_df`` DataFrame.

.. code-block:: python
``
def interactions(n_rows):
    features = [f"gene_{i+1}" for i in range(n_rows)]
    interact = []
    for i in range(len(features)):
        other_features = features[:i] + features[i+1:]
        n_interact = np.random.randint(1, n_rows)
        interact_features = np.random.choice(other_features, size=n_interact, replace=False)
        for j in range(n_interact):
            interact.append((features[i], interact_features[j]))
    interact_df = pd.DataFrame(interact, columns=['feature_1', 'feature_2'])
    
    # Remove 30% of random rows
    interact_df = interact_df.sample(frac=0.7, random_state=42)
    
    # Sort by index
    interact_df = interact_df.sort_index()
    
    return interact_df

interact=interactions(2000)
``

The ``ISN_Tractor`` library is imported as follows:

.. code-block:: python
``
import isn_tractor.ibisn as it
``

ISN generation:
the ``sparse_isn`` function is invoked to transform the gene-based dataset into a sparse isn dataset using as metric parameter ``incremental_pearson``.

.. code-block:: python
``
sparse_isn=it.sparse_isn(df, interact_unmapped=None, interact_mapped=interact, metric="incremental_pearson")
``

.. toctree::
   :maxdepth: 2
   
   example3
<|endoftext|>

Example 3: sparse SNP-array-based ISNs computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This example shows how to compute sparse ISNs of a SNP-array-based dataset.

Data generation:
The generation of synthetic single-nucleotide polymorphism (SNP) data follows a structured approach to ensure reproducibility and reliable results. 
The data generation process involves two main functions: ``onehot()`` and ``generate2()``. These functions utilize a random seed to maintain consistency in the generated data.
The ``generate2()`` function is responsible for creating random samples for specified clusters and constructing a matrix to store the SNP data. 
Additionally, it generates matrices for minor allele frequency and random values. To assign SNP values to the matrix, the code utilizes a nested loop based on the minor allele frequency.
Once the SNP data is generated, it is accompanied by cluster information and organized into a DataFrame with appropriate column headers. 
This streamlined process facilitates the study of genetic variations and supports the development of computational methods in genomics research.

.. code-block:: python
``
def onehot(x):
    X = np.zeros((x.size, x.max() + 1))
    X[np.arange(x.size), x] = 1
    return X

def generate(Ps, Cs):
    np.random.seed(1)
    p1, p2 = Ps
    c1, c2 = Cs

    clust1 = np.sort(np.random.choice(c1, size=p1, replace=True))
    clust2 = np.sort(np.random.choice(c2, size=p2, replace=True))

    G1 = onehot(clust1)
    G2 = onehot(clust2)

    S = np.random.uniform(0, 1, size=(c1, c2))

    R = G1 @ S @ G2.T 

    return R, clust1, clust2

def generate2(Ps, Cs):
    np.random.seed(1)
    p1, p2 = Ps
    c1, c2 = Cs

    clust1 = np.sort(np.random.choice(c1, size=p1, replace=True))
    clust2 = np.sort(np.random.choice(c2, size=p2, replace=True))

    R = np.zeros((p1, p2))
    MAF = np.zeros((c1, c2)) + 0.05
    maf1 = np.linspace(0.0, 0.25, c1)
    maf2 = np.linspace(0.0, 0.2, c2)
    np.random.shuffle(maf1)
    np.random.shuffle(maf2)
    MAF = MAF + np.tile(maf1, (c2, 1)).T + np.tile(maf2, (c1, 1))
    MAF = np.random.uniform(0.01, 0.5, size=(c1, c2))

    for i in range(c1):
        idx_i = np.where(clust1 == i)[0]
        for j in range(c2):
            idx_j = np.where(clust2 == j)[0]
            maf = MAF[i, j]
            block = np.random.choice([0, 1, 2], size=[len(idx_i), len(idx_j)],
                                    p=[(1 - maf) * (1 - maf), 2 * maf * (1 - maf), maf * maf])
            R[idx_i[0]:(idx_i[-1] + 1), idx_j[0]:(idx_j[-1] + 1)] = block

    return R.astype(int), clust1.astype(int), clust2.astype(int)

R, clust1, clust2 = generate2([200, 1000], [5, 20])

# Store the SNP data in a DataFrame
header = ['SNP' + str(i + 1) for i in range(R.shape[1])] + ['Pheno']
df = pd.DataFrame(np.hstack((R, clust1[:, None])), columns=header)

# save the synthetic data
#path = 'path'
#header = ['SNP'+str(i+1) for i in range(R.shape[1])] + ['Pheno']
#np.savetxt(path + 'toydata_SNP.csv', np.hstack((R, clust1[:,None])),
#        delimiter=',', header=','.join(header), comments='', fmt="%i")
``

Interaction list generation:

.. code-block:: python
``
genes = ['gene'+str(i+1) for i in range(20)]
interact = np.array(np.meshgrid(genes, genes)).T.reshape(-1, 2)
interact_df = pd.DataFrame(interact, columns=['feature_1', 'feature_2'])
#save the synthetic interactions
#np.savetxt(path + 'toydata_interact_genes.csv', interact, delimiter=',', fmt="%s")
``

Mapping simulation:

.. code-block:: python
``
mapping = []
for pair in interact:
    gene1 = int(pair[0][4:]) - 1
    gene2 = int(pair[1][4:]) - 1
    snps1 = np.where(clust2 == gene1)[0]
    snps2 = np.where(clust2 == gene2)[0]
    snps1 = ['SNP'+str(i+1) for i in snps1]
    snps2 = ['SNP'+str(i+1) for i in snps2]
    mapping.append((snps1, snps2))

mapping_df = pd.DataFrame(mapping, columns=['snps1', 'snps2'])
#save the mapping
#import pickle
#pickle.dump(mapping, open(path + 'toydata_interact_snps.pkl', "wb"))
``

The ``ISN_Tractor`` library is imported as follows:

.. code-block:: python
``
import isn_tractor.ibisn as it
``

ISN generation:
the ``sparse_isn`` function is invoked to transform the SNP-array-like dataset into a sparse isn dataset using as metric parameter ``pearson`` and pooling parameter ``max``.

.. code-block:: python
``
sparse_isn=it.sparse_isn(df, interact_unmapped=mapping_df, interact_mapped=interact_df, metric="pearson", pool="max")
``