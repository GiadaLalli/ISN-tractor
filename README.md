# ISN-tractor
Interactome based Individual Specific Networks (Ib-ISN)

## About the project: Interactome Based Individual Specific Networks (Ib-ISN) Computation and its relevance

An *individual-specific network* in biology is a sort of network that depicts the relationships between the genes, proteins, or other biological molecules of a particular individual. 

It is sometimes referred to as a "personalised network" or "individual network". 

These networks can be computed using a range of data types, including genetic information, details on protein expression, and other omics data.

One of the top aims of individual-specific networks is to comprehend **how interactions between different biological molecules affect an individual's overall function and behaviour**. For example, an individual-specific network can be used to identify the proteins that are essential for maintaining a certain biological activity or the critical regulatory networks that control a person's gene expression. It is also possible to forecast how genetic or environmental changes may affect a person's biology by using individual-specific networks. For instance, they can be used to foretell how a specific mutation or environmental exposure may impact the way a certain gene or pathway functions.

The entire range of interactions between biological macromolecules in a cell, including as those mediated by protein-ligand binding or solely functional connections between proteins, are referred to as the *interactome*. As a result, it offers a summary of the functional activity within a particular cell. Extracellular protein-protein interaction (PPI) networks are particularly significant to illness causation, diagnosis, and treatment due to a number of features. Their functional diversity, chaos, and complexity are a few of these.

[Luck et al.](https://www.nature.com/articles/s41586-020-2188-x) introduced *HuRI*, a human "all-by-all" reference interactome map of human binary protein interactions, which has been demonstrated to have over 53,000 protein-protein interactions. 

HuRI, as 
> a systematic proteome-wide reference that connects genetic variation to phenotypic outcomes,

was the impetus for our decision to create a novel approach for computing interactome-based ISN, starting from SNP data and ending with a gene-based network.

## Getting started

### Installation

```bash
pip install isn-tractor
```

## Usage

1. Data preprocessing and imputation

```python
import pandas as pd
import isn_tractor.ibisn as it

snps = pd.read_csv("snp_dataset.csv")
snp_meta = pd.read_csv("snp_metadata.csv")
interact = pd.read_csv("interactome_interactions.csv")
gtf = pd.read_csv("human_genes.csv")

# returns 
gene_info = it.preprocess_gtf(gtf)

# returns 
it.preprocess_snp(snp_meta)

# returns 
snps = it.impute(snps)
```

2. Mapping

```python
# returns 
it.positional_mapping(snp_meta, gene_info, neighborhood=5)
```

3. Features mapping and interaction

```python
# returns 
(interact_snp, interact_gene) = it.snp_interaction(interact, gene_info, snp_info)
```

4. Individual Specific Network (ISN) computation

```python
isn = it.compute_isn(df, interact_snp, interact_gene, "spearman", "max")
```

For more examples, please refer to the _Documentation_.

## Roadmap
- [ ] Complete the _Usage_ section
- [ ] Add documentation with examples
- [ ] Consider a new function for functional mapping
- [ ] Add:
    - [ ] Imputation with file saving
    - [ ] Function ```isn_calculation_per_edge```
    - [ ] Progressbar

## Contributing

Contributions are what make the open source community such a wonderful place to learn, be inspired, and create. 
Your contributions will be greatly appreciated.

If you have an idea for how to improve this, please fork the repository and submit a pull request. You can alternatively open a new issue with the tag "improvement". Don't forget to :star: the project! Thank you once more!

1. Fork the Project
2. Create your Feature Branch `(git checkout -b feature/AmazingFeature)`
3. Commit your Changes `(git commit -m 'Add some AmazingFeature')`
4. Push to the Branch `(git push origin feature/AmazingFeature)`
5. Open a Pull Request

## License

## Contact
Giada Lalli - giada.lalli@kuleuven.be

Zuqi Li - zuqi.li@kuleuven.be

Federico Melograna - federico.melograna@kuleuven.be


Project Link: 

## Acknowledgments

