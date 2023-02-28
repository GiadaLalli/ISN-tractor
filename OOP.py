class isn:
    def __init__(self, X, x_type, isdense=True, interact=None, 
                 unmapped_info=None, maptobe_info=None, pool=None, 
                 metric=None, neighborhood=0):
        
        if x_type not in ['mapped', 'unmapped']: 
            raise ValueError("data must be either 'mapped' or 'unmapped'")
        if not isinstance(isdense, bool):
            raise ValueError("isn must be either dense or sparse")
        
            
        self.X = X #input data
        self.x_type = x_type #how's the data
        self.isdense = isdense #how's the isns I want to compute 
        self.interact = interact #needed in case y_type == 'unmapped'
        self.unmapped_info = unmapped_info #needed in case y_type == 'unmapped'
        self.maptobe_info = maptobe_info #needed in case y_type == 'unmapped'
        self.pool = pool #needed in case y_type == 'unmapped'
        self.metric = metric #always needed for isn computation
        
        if self.x_type == 'unmapped' and self.metric not in ['pearson', 'spearman', 'mutual_info', 'dot', 'LD']:
            raise ValueError("metric must be 'LD', 'pearson', 'spearman', 'mutual_info', or 'dot' for data == 'unmapped'")
        
        if self.x_type == 'unmapped' and self.pool not in ["sum", "avg", "max"]:
            raise ValueError("pool must be either 'sum', 'avg', or 'max' when data is 'unmapped'")
            
        if self.x_type == 'mapped' and self.metric not in ['pearson', 'spearman', 'mutual_info', 'dot']:
            raise ValueError("metric must be 'pearson', 'spearman', 'mutual_info', or 'dot' for data == 'mapped'")
    
    def __pooling(self, scores):
            
        if self.pool not in ['avg', 'average', 'max', 'sum']:
                raise ValueError("pool must be 'avg', 'max' or 'sum'")
            
        if self.pool in ("avg", "average"):
                return np.mean(scores)
        if self.pool == "max":
                return np.max(scores)
        if self.pool == "sum":
                return np.sum(scores)
        
    def __compute_metric(self, x, y=None):
            
        if self.x_type == "mapped" and self.isdense:
            if self.metric == "pearson":
                score = x.corr(method='pearson')
            elif self.metric == "spearman":
                score = x.corr(method='spearman')
            else:
                raise ValueError('Wrong input for metric!')
           
        elif self.x_type == "mapped" and not self.isdense:
            if self.metric == "pearson":
                score = pearsonr(x, y)[0]
            elif self.metric == "spearman":
                score = spearmanr(x, y)[0]
            elif self.metric == "mutual_info":
                score = mutual_info(x, y)
            elif self.metric == "dot":  # dot product
                score = np.dot(x.T, y)
            else:
                raise ValueError('Wrong input for metric!')
                    
        elif x_type == "unmapped":
            if self.metric == "pearson":  # Pearson correlation
                    # pylint: disable=C0103
                xy = np.concatenate([x, y], axis=1)
                scores = np.corrcoef(xy.T)[: x.shape[1] - 1, x.shape[1] :]
                score = self.__pooling(scores, pool)
            elif self.metric == "spearman":  # Spearman correlation
                scores = spearmanr(x, y)[0]
                score = self.__pooling(scores, pool)
            elif self.metric == "mutual_info":  # normalized mutual information
                scores = np.zeros((x.shape[1], y.shape[1]))
                for i in range(x.shape[1]):
                    for j in range(y.shape[1]):
                        scores[i, j] = mutual_info(x[:, i], y[:, j])
                    score = self.__pooling(scores, pool)
            elif self.metric == "LD":  # LD r^2 score
                scores = allel.rogers_huff_r_between(x.T, y.T)  # LD r score
                scores = np.square(scores)  # LD r^2 score
                score = self.__pooling(scores, pool)
            elif self.metric == "dot":  # dot product
                    # pylint: disable=E1101
                scores = t.matmul(x.T, y)
                score = self.__pooling(scores, pool)
            else:
                raise ValueError("Wrong input for metric!")
            else:
                raise ValueError("Wrong input for x_type!")
            return score
        
    def __positional_mapping(self):

            mapping = {}

            for i in range(self.maptobe_info.shape[0]):
                lowbound = self.maptobe_info.iloc[i, 1] - self.neighborhood
                upbound = self.maptobe_info.iloc[i, 2] + self.neighborhood
                idx = np.where(
                    np.all(
                        (
                            self.unmapped_info.to_numpy()[:, 0] == self.maptobe_info.to_numpy()[i, 0],
                            self.unmapped_info.to_numpy()[:, 1] >= lowbound,
                            self.unmapped_info.to_numpy()[:, 1] <= upbound,
                        ),
                        axis=0,
                    )
                )[0]

                if len(idx) == 0:  # skip genes if no SNP assigned
                    continue
                if len(idx) == 1:  # in case only 1 SNP is mapped to the gene
                    mapping[self.maptobe_info.index.values[i]] = [self.unmapped_info.index.values[idx]]
                else:  # in case multiple SNPs are mapped to the gene
                    mapping[self.maptobe_info.index.values[i]] = self.unmapped_info.index.values[idx]

            return mapping

        def __map_interaction(self):
            
            if self.x_type == "unmapped":
                mapping = self.__positional_mapping(self.unmapped_info, self.maptobe_info, neighborhood)
            else:
                mapping = None

            interact_mapped = []
            interact_unmapped = []
            for feature_1, feature_2 in interact.to_records(index=False):
                if mapping:
                    if feature_1 in mapping and feature_2 in mapping:
                        interact_mapped.append((feature_1, mfeature_2))
                        interact_unmapped.append((mapping[feature_1], mapping[feature_2]))
                else:
                    interact_unmapped.append((mapfeat_id_1, mapfeat_id_2))

            if mapping:
                interact_mapped = pd.DataFrame(interact_mapped, columns=["feature_1", "feature_2"])
            else:
                interact_mapped = None

            return (interact_unmapped, interact_mapped)

        def __isn_calculation_per_edge(self, intersection1_list, intersection2_list):

            glob = self.__compute_metric(intersection1_list, intersection2_list)
            result = []

            for indx in range(intersection1_list.shape[0]):
                element1_loo = np.delete(intersection1_list, indx, axis=0)
                element2_loo = np.delete(intersection2_list, indx, axis=0)
                avg = self.__compute_metric(element1_loo, element2_loo)
                result.append(intersection1_list.shape[0] * (glob - avg) + avg)

            return result

    def compute(self):
           '''
           when isdense = False, mapping is needed, in this condition I call the method pos_mapping 
           '''
            if self.isdense and self.x_type == 'mapped':
                nrsamples = self.X.shape[1]
                samples = self.X.columns

                net = __compute_metric(self.X.T)
                agg = net.to_numpy().flatten()

                # create a pandas dataframe with NaN values with dimensions of df
                isn = pd.DataFrame(np.nan, index=np.arange(self.X.shape[0]*self.X.shape[0]), 
                                             columns=["reg", "tar"]+list(samples)).astype(object)
                isn.iloc[:, 0] = np.repeat(net.columns.values, net.columns.size)
                isn.iloc[:, 1] = np.tile(net.columns.values, self.X.shape[0])

                for i in range(nrsamples):
                    ss = __compute_metric(pd.DataFrame(np.delete(self.X.T.to_numpy(), i, 0))).values.flatten() # apply Pearson on all samples minus one
                    isn.iloc[:, i+2] = nrsamples*(agg-ss) + ss # apply LIONESS equation
                return isn
            
            elif not self.isdense and self.x_type == 'unmapped':
                interact_unmapped, interact_mapped = self.__map_interaction()
                isn = np.zeros((self.X.shape[0], len(interact_unmapped)))

                for index, (unmap_assoc_map_1, unmap_assoc_map_2) in enumerate(interact_unmapped):

                    element_one = np.array(unmap_assoc_map_1, dtype=object)
                    element_two = np.array(unmap_assoc_map_2, dtype=object)

                    intersection_1 = (
                        self.X[element_one[0]]
                        if len(element_one) == 1
                        else self.X[self.X.columns.intersection(element_one)]
                    )

                    intersection_2 = (
                        self.X[element_two[0]]
                        if len(element_two) == 1
                        else self.X[self.X.columns.intersection(element_two)]
                    )

                    edge = self.__isn_calculation_per_edge(
                        t.tensor(intersection_1.values),  # pylint: disable=E1101
                        t.tensor(intersection_2.values),  # pylint: disable=E1101
                    )
                    isn[:, index] = edge

                isn = pd.DataFrame(isn, columns=[a + "_" + b for a, b in interact_mapped.values])
                return isn
            
            elif not self.isdense and self.x_type == 'mapped':
                isn = np.zeros((self.X.shape[0], len(self.interact)))

                for index, tuple in enumerate(self.interact.values):
                    if not np.all(self.interact.iloc[index].isin(self.X.columns)): continue

                    element_one = np.array(tuple[0], dtype=object)
                    element_two = np.array(tuple[1], dtype=object)

                    x = self.X[element_one]
                    y = self.X[element_two]

                    edge = self.__isn_calculation_per_edge(t.tensor(x.values), t.tensor(y.values))
                    isn[:, index] = edge

                isn = pd.DataFrame(isn, columns=[a+'_'+b for a,b in self.interact.values])
                isn = isn.iloc[:, np.where(isn.sum() != 0)[0]]
                return isn