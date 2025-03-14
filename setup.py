from setuptools import setup, find_packages

setup(
    name="clustering_eval",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn",
        "tensorflow",
        "matplotlib",
        "pandas"
    ],
    author="Your Name",
    author_email="your_email@example.com",
    description="A package for evaluating clustering algorithms using NCQI.",
    url="https://github.com/yourusername/clustering_eval",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
