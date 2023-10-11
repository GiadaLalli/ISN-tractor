# ISN-tractor
Interactome based Individual Specific Networks (Ib-ISN)

## About the project: Interactome Based Individual Specific Networks (Ib-ISN) Computation and its relevance

An *Individual-Specific Network (ISN)* is a unique network tailored to an individual, reflecting their distinct genetic, environmental, and lifestyle characteristics. With the progress in high-throughput technologies and the emergence of personalized medicine, there is growing interest among researchers in constructing ISNs to gain deeper insights into the intricate interactions among various biological components and their roles in shaping health and disease outcomes. These networks can be built using diverse data types, such as genomics, transcriptomics, proteomics, or metabolomics data, enabling a personalized understanding of disease mechanisms and the identification of individualized therapeutic targets. ISNs also find applications in predicting disease risk, forecasting drug responses, and optimizing personalized treatment strategies. However, creating and interpreting ISNs is a complex and demanding task, necessitating advanced computational methods and rigorous validation using independent data sources. Nevertheless, the potential advantages of ISNs are substantial, representing a promising path toward realizing the goals of personalized medicine. It is sometimes referred to as a "personalised network" or "individual network". 

In this study, we define an ISN as a graphical representation where the nodes (also known as vertices) can represent any biological entity, such as genes or taxa, and the connections between these nodes (referred to as interactions or edges) are specific to each individual. Consequently, each edge connecting a pair of nodes carries a weight that varies for each individual within the population. This contrasts with a population-level (or global) network, where the data are aggregated across individuals to create a single network that does not capture individual variations.
Among possible ISNs methods, we focus in this work on the LIONESS' one from [Kuijjer et al.](https://pubmed.ncbi.nlm.nih.gov/30981959/)


One of the top aims of individual-specific networks is to comprehend **how interactions between different biological molecules affect an individual's overall function and behaviour**. For example, an individual-specific network can be used to identify the proteins that are essential for maintaining a certain biological activity or the critical regulatory networks that control a person's gene expression. It is also possible to forecast how genetic or environmental changes may affect a person's biology by using individual-specific networks. For instance, they can be used to foretell how a specific mutation or environmental exposure may impact the way a certain gene or pathway functions.

The entire range of interactions between biological macromolecules in a cell, including as those mediated by protein-ligand binding or solely functional connections between proteins, are referred to as the *interactome*. As a result, it offers a summary of the functional activity within a particular cell. Extracellular protein-protein interaction (PPI) networks are particularly significant to illness causation, diagnosis, and treatment due to a number of features. Their functional diversity, chaos, and complexity are a few of these.

[Luck et al.](https://www.nature.com/articles/s41586-020-2188-x) introduced *HuRI*, a human "all-by-all" reference interactome map of human binary protein interactions, which has been demonstrated to have over 53,000 protein-protein interactions. 

HuRI, as 
> a systematic proteome-wide reference that connects genetic variation to phenotypic outcomes,

was the impetus for our decision to create a novel approach for computing interactome-based ISN, starting from SNP data and ending with a gene-based network.

## Getting started

### Installation

You can install ISN-Tractor from the GitHub Repository:

```bash
pip install git+https://github.com/GiadaLalli/ISN-tractor
```

or from our [PyPi package](https://pypi.org/project/isn-tractor/):

```bash
pip install isn-tractor
```

Quickstart
==========

The ``examples`` and ``visualisation`` folders contain some scripts showing how the ``ISN-Tractor`` library can be used.

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

For more examples, please refer to the _examples_ folder.

## Roadmap
- [ ] Paper citation.


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
[MIT License](https://github.com/GiadaLalli/ISN-tractor/blob/main/LICENSE).

## Contact
Giada Lalli - giada.lalli@kuleuven.be

Zuqi Li - zuqi.li@kuleuven.be

Federico Melograna - federico.melograna@kuleuven.be

## Acknowledgments
Many thanks to [Daniele Raimondi](https://www.kuleuven.be/wieiswie/en/person/00119412) and [James Collier](https://technologytraining.sites.vib.be/en/team) whose collaboration made possible the finalization of this project. 

How to cite
===========

If you find this library useful, please cite: 

About us
========

This library has been developed until October 2023 at KU Leuven, Belgium and funded by the European Union's Horizon 2020 research and innovation programme under the H2020 Marie Skłodowska-Curie grant agreement (No. 860895 to GL, ZL, FM). 

Disclaimer
==========

I did my best effort to make this library available to anyone, but bugs might be present.
Should you experience problems in using or installing it, or just to share any comment, please contact giada [dot] lalli [at] kuleuven [dot] be and zuqi [dot] li [at] kuleuven [dot] be.




