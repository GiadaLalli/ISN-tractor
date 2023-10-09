import pickle

import numpy as np


def generate(Ps, Cs):
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
            block = np.random.choice(
                [0, 1, 2],
                size=[len(idx_i), len(idx_j)],
                p=[(1 - maf) * (1 - maf), 2 * maf * (1 - maf), maf * maf],
            )
            R[idx_i[0] : (idx_i[-1] + 1), idx_j[0] : (idx_j[-1] + 1)] = block

    return (R.astype(int), clust1.astype(int), clust2.astype(int))


if __name__ == "__main__":
    R, clust1, clust2 = generate([200, 1000], [5, 20])

    # save the SNP data
    header = ["SNP" + str(i + 1) for i in range(R.shape[1])] + ["Pheno"]
    np.savetxt(
        "toydata_SNP.csv",
        np.hstack((R, clust1[:, None])),
        delimiter=",",
        header=",".join(header),
        comments="",
        fmt="%i",
    )

    # save the interactome
    genes = ["gene" + str(i + 1) for i in range(20)]
    interact = np.array(np.meshgrid(genes, genes)).T.reshape(-1, 2)
    np.savetxt("example_interact_genes.csv", interact, delimiter=",", fmt="%s")

    # save the mapping
    mapping = []
    for pair in interact:
        gene1 = int(pair[0][4:]) - 1
        gene2 = int(pair[1][4:]) - 1
        snps1 = np.where(clust2 == gene1)[0]
        snps2 = np.where(clust2 == gene2)[0]
        mapping.append(([f"SNP{i+1}" for i in snps1], [f"SNP{i+1}" for i in snps2]))

    with open("example_interact_snps.pkl", "wb") as mappingfile:
        pickle.dump(mapping, mappingfile)
