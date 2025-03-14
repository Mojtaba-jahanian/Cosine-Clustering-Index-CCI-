import numpy as np
from clustering_eval.ncqi import normalized_clustering_quality_index

def test_ncqi():
    X = np.random.rand(100, 10)
    labels = np.random.randint(0, 3, size=100)
    ncqi = normalized_clustering_quality_index(X, labels)
    assert 0 <= ncqi <= 1, "NCQI باید بین 0 و 1 باشد."

if __name__ == "__main__":
    test_ncqi()
    print("All tests passed!")
