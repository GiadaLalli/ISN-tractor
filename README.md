# ISN-tractor
Interactome based Individual Specific Networks (Ib-ISN)
<img style="width:100%" src="ISN.svg">

## What is ISN-Tractor?
ISN-tractor is a Python package designed for the computation of Individual-Specific Networks (ISNs) from multiple omics. By identifying differential feature-expression and edges between samples, ISNs can provide valuable insights into personalized expression networks. ISN-tractor is a user-friendly tool that offers a simple interface for analyzing multiple datasets and generating ISNs. It can be applied to various organisms, including humans, animals, and plants. Thus, ISN-tractor is a powerful and versatile tool for identifying personalized feature expression networks in different contexts.

## ISNs in the context of precision medicine
Precision medicine, a groundbreaking approach to healthcare, acknowledges that a one-size-fits-all approach is inadequate for disease diagnosis and treatment. Instead, it aims to customize medical decisions and interventions to match the unique characteristics of each patient. At the core of precision medicine is the concept of individual-specific networks, a dynamic and evolving framework that considers the complex interactions among an individual's genetic, molecular, and environmental factors in the context of health and disease.

Individual-specific networks (ISNs) represent a revolutionary healthcare approach, recognizing patients' inherent diversity. These networks transcend conventional medical methods, often applying treatment strategies based on general population averages. Instead, they acknowledge that each patient's genetic makeup and its' interactions with external factors create a highly individualized network of influences on their health.
<!-- An *Individual-Specific Network (ISN)* is a unique network tailored to an individual, reflecting their distinct genetic, environmental, and lifestyle characteristics. With the progress in high-throughput technologies and the emergence of personalized medicine, there is growing interest among researchers in constructing ISNs to gain deeper insights into the intricate interactions among various biological components and their roles in shaping health and disease outcomes. These networks can be built using diverse data types, such as genomics, transcriptomics, proteomics, or metabolomics data, enabling a personalized understanding of disease mechanisms and the identification of individualized therapeutic targets. ISNs also find applications in predicting disease risk, forecasting drug responses, and optimizing personalized treatment strategies. However, creating and interpreting ISNs is a complex and demanding task, necessitating advanced computational methods and rigorous validation using independent data sources. Nevertheless, the potential advantages of ISNs are substantial, representing a promising path toward realizing the goals of personalized medicine. It is sometimes referred to as a "personalised network" or "individual network". -->

Moreover, ISNs have profound implications for disease prevention and early diagnosis. By examining a patient's genetic predispositions and environmental exposures, healthcare providers can pinpoint risk factors and create personalized strategies for disease prevention and early detection. This not only enhances the likelihood of successful treatment but also minimizes unnecessary suffering from ineffective therapies.

Describing a system involves elucidating its behaviour and the vital control mechanisms that govern this behaviour. Central to this process are interactions that can occur at various levels or scales. Consequently, network theory and network visualization are increasingly employed to comprehend the biological mechanisms at work within human systems. However, an individual, especially when in poor health, is prone to deviating from the typical patterns within human systems.

ISN is a broad term encompassing various structures in the literature. We concentrated on Kuijjer's tool and formula LIONESS [Kuijjer et al.](https://pubmed.ncbi.nlm.nih.gov/30981959/) for calculating an ISN. In general, we refer to an ISN as a network where individual specificity is represented in the edges, and there is only one sample available for each individual. The quantification of the individual-specific edge weight may vary based on the underlying association method, such as Pearson correlation, and the method used to compute the ISN, such as LIONESS' leave-one-out procedure. Remarkably, research on ISNs is a growing field and more and more works every year exploit them. In particular, we want to highlight: 
* _Evaluation of Single Sample Network Inference Methods for Metabolomics-Based Systems Medicine_ [Jahagirdar et al., 2021](https://pubs.acs.org/doi/10.1021/acs.jproteome.0c00696), using ISNs' edge weight as input feature in a random forest to predict the phenotype
* _Capturing the dynamics of microbial interactions through individual-specific networks_ [Yousefi et al., 2023](https://www.frontiersin.org/articles/10.3389/fmicb.2023.1170391/full), using ISNs in an encoder-decoder pipeline on microbiome data
* _c-CSN: Single-cell RNA Sequencing Data Analysis by Conditional Cell-specific Network_ [Li et al., 2021](https://pubmed.ncbi.nlm.nih.gov/33684532/), proposing a  cell-specific network in the context of single cell
* _Edge and modular significance assessment in individual-specific networks_ [Melograna et al., 2023](https://www.nature.com/articles/s41598-023-34759-8), introducing a modular significance assessment in ISNs


Nonetheless, there is room for enhancement. Therefore, this project was undertaken with the aim of addressing some of the existing shortcomings within the ISNs ecosystem.


### ISNs shortcomings
ISNs, as defined by Kuijjer, are limited to working with single-omics and can be very computationally intensive, as they scale quadratically with the number of nodes. Moreover, there is no integrated way to focus only on biologically-relevant interactions.

## ISNs in this project
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

- [Data format](https://github.com/GiadaLalli/ISN-tractor/blob/main/examples/end-to-end/example.py)
- [Example 1: gene-based ISNs computation](https://github.com/GiadaLalli/ISN-tractor/tree/main/examples/gene)
- [Example 2: SNP-based ISNs computation](https://github.com/GiadaLalli/ISN-tractor/tree/main/examples/snp)


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


Performance History
===================

https://giadalalli.github.io/ISN-tractor/dev/bench/index.html

