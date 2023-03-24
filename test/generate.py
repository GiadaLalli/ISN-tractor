import random
from string import ascii_lowercase
import sys

import pandas as pd

from isn_tractor import ibisn as it


def identifiers(N: int, L: int) -> list[str]:
    "Generate N identifiers each with a length of L."
    return list(
        "".join(random.choice(ascii_lowercase) for _ in range(L)) for _ in range(N)
    )


for num_genes in range(2, 7):
    genes = [f"gene_{x}" for x in identifiers(num_genes, 4)]
    interact = pd.DataFrame(
        [(random.choice(genes), random.choice(genes)) for _ in range(num_genes // 2)],
        columns=["1", "2"],
    )
    gene_info = pd.DataFrame(
        [(1, i * 10 + 1, (i + 1) * 10) for (i, _) in enumerate(genes)],
        columns=["chr", "start", "stop"],
        index=genes,
    )
    for num_snps in range(2, 6):
        snps = [f"snp_{x}" for x in identifiers(num_snps, 5)]
        snp_info = pd.DataFrame(
            [(1, i * 10 + 5) for (i, _) in enumerate(snps)],
            columns=["chr", "position"],
            index=snps,
        )
        if num_snps == 10:
            print(snp_info)
            print()
            print(gene_info)
            print(gene_info.iloc[:, 1])
            print(gene_info.iloc[:, 2])
        for num_samples in range(1, 11):
            snp_data = pd.DataFrame(
                [(random.choice([0, 1, 2]) for _ in snps) for _ in range(num_samples)],
                columns=snps,
            )
            print(num_genes, num_snps, num_samples, end="\r")
            mapping = it.positional_mapping(snp_info, gene_info, 0)
            if num_snps == 10:
                sys.exit()
            if len(mapping) > 0:
                print(mapping)
                (interact_snp, interact_gene) = it.snp_interaction(
                    interact, gene_info, snp_info
                )
                if len(interact_snp) > 0:
                    isn = it.compute_isn(
                        snp_data, interact_snp, interact_gene, "pearson", "avg"
                    )
                    if not isn.isnull().values.any():
                        print("Interact:")
                        print(interact, end="\n\n")
                        print("Gene Info:")
                        print(gene_info, end="\n\n")
                        print("SNP Info:")
                        print(snp_info, end="\n\n")
                        print("SNP Data:")
                        print(snp_data, end="\n\n")
                        print("Interact SNP:")
                        print(interact_snp, end="\n\n")
                        print("Interact Gene:")
                        print(interact_gene, end="\n\n")

                        print("ISN:")
                        print(isn)


interact = pd.DataFrame([("gene1", "gene2"), ("gene2", "gene3")], columns=["1", "2"])
snp_data = pd.DataFrame(
    [(1, 2, 0), (1, 0, 1), (2, 2, 1)], columns=["snp1", "snp2", "snp3"]
)
gene_info = pd.DataFrame(
    [("gene1", 1, 1, 10), ("gene2", 1, 11, 20), ("gene3", 2, 5, 30)],
    columns=["ENSEMBL_ID", "chr", "start", "stop"],
)
snp_info = pd.DataFrame([("snp1", 1, 5), ("snp2", 1, 12), ("snp3", 2, 18)])

(interact_snp, interact_gene) = it.snp_interaction(interact, gene_info, snp_info)
print(interact_snp)
print(interact_gene)

print(it.compute_isn(snp_data, interact_snp, interact_gene, "pearson", "avg"))
