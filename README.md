# Clustering Evaluation (NCQI)

A Python package for evaluating clustering algorithms using the **Normalized Clustering Quality Index (NCQI)**.

## 📌 Installation
To install the package, run:
```bash
pip install git+https://github.com/yourusername/clustering_eval.git
```

## 🚀 Usage
```python
from clustering_eval.ncqi import normalized_clustering_quality_index
import numpy as np

X = np.random.rand(100, 10)
labels = np.random.randint(0, 3, size=100)
ncqi_score = normalized_clustering_quality_index(X, labels)
print("NCQI Score:", ncqi_score)
```
