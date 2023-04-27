import pandas as pd
import numpy as np
import isn_tractor.ibisn as it

def dataframe(size, values):
    n_rows, n_cols = size
    mapped = "mapped" if "mapped" in values else "unmapped"
    
    if "discrete" in values:
        data = np.random.randint(0, 3, size=(n_rows, n_cols))
    elif "continuous" in values:
        data = np.random.uniform(0, 100, size=(n_rows, n_cols))
    else:
        raise ValueError("Values must contain either 'discrete' or 'continuous'")
    
    col_names = [mapped + "_" + "feature" + "_" + str(i) for i in range(n_cols)]
    index_names = ["sample_" + str(i) for i in range(n_rows)]
    
    df = pd.DataFrame(data, index=index_names, columns=col_names)
    
    return df
u_df = dataframe((200, 500000), ["unmapped", "discrete"])
m_df = dataframe((200, 1000), ["mapped", "continuous"])

def interactions(n_rows):
    features = [f"mapped_feature_{i}" for i in range(n_rows)]
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
interact=interactions(100)

def mapped_info(df):
    # Define column names
    column_names = ["chr", "start", "stop"]
    
    # Define number of chromosomes
    #n_chromosomes = 23
    n_chromosomes = 1
    # Compute number of rows
    n_rows = len(df.columns)
    
    # Generate random values for each column
    chrs = np.repeat(np.arange(1, n_chromosomes+1), n_rows//n_chromosomes+1)[:n_rows]
    starts = np.arange(1, n_rows*10000+1, 10000)
    stops = starts + 9
    
    # Assign values to rows based on input df
    df_rows = []
    for i, row_name in enumerate(df.columns):
        #df_rows.append([chrs[i], starts[i], stops[i]])
        df_rows.append([n_chromosomes, starts[i], stops[i]])
    
    # Create dataframe
    data_frame = pd.DataFrame(df_rows, columns=column_names, index=df.columns)
    
    return data_frame
mapped_info=mapped_info(m_df)

def unmapped_info(df):
    rows = df.shape[1]
    location = [2 * i for i in range(rows)]
    #chromosome = sorted([(i % 23) + 1 for i in range(rows)])
    chromosome = 1
    return pd.DataFrame({"chr": chromosome, "location": location}, index=df.columns)
unmapped_info=unmapped_info(u_df)

interact_unmapped,interact_mapped = it.map_interaction(interact= interact, mapped_info = mapped_info, unmapped_info = unmapped_info, neighborhood = 8)
