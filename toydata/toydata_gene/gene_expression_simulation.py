#import libraries
import pandas as pd
import numpy as np
import isn_tractor.ibisn as it

#data import
interact = pd.read_csv('HuRI')
gtf = pd.read_csv('GRCh38_assembly')
corr = pd.read_csv('genename_geneid_correlation')
id_list = gtf.index.tolist() #list of the ensembl_id

#preprocessing
gtf = it.preprocess_gtf(gtf)

corr = corr.dropna(subset=['Gene name'])
corr = corr[corr['Gene stable ID'].isin(id_list)]
corr = corr.drop_duplicates(subset='Gene stable ID', keep=False)

#simulated data creation
np.random.seed(123)
df = pd.DataFrame(np.random.rand(200, 1000)) #creates random dataset with 200 rows and 1000 columns of random floating values
names = corr['Gene stable ID'].tolist() #define a list of gene_names
df.columns = random.choices(names, k=df.shape[1]) #assign random names from the list to the columns of the dataframe
nan_indices = np.random.choice(df.size, size=500, replace=False) #add some NaN
df.values.ravel()[nan_indices] = np.nan 
#save the data
df.to_csv(r'toydata_gene', sep=',', index = False)
