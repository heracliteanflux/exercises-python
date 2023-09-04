# (Ana)conda

## A development environment for macOS

0

```zsh
conda deactivate &&
conda remove -n ml -y --all
```

1

```zsh
conda create -n ml -y \
-c conda-forge --strict-channel-priority \
'boto3           =0001.28' \
'cython          =0003.00' \
'dask            =2023.09' \
'fastparquet     =2023.07' \
'findspark       =0002.00' \
'hvplot          =0000.08' \
'imbalanced-learn=0000.11' \
'ipykernel       =0006.25' \
'ipympl          =0000.09' \
'ipywidgets      =0008.01' \
'jupyterlab      =0004.00' \
'nltk            =0003.08' \
'numpy           =0001.25' \
'matplotlib      =0003.07' \
'mrjob           =0000.07' \
'openpyxl        =0003.01' \
'pandas          =0002.01' \
'pillow          =0010.00' \
'pip             =0023.02' \
'plotly          =0005.16' \
'polars          =0000.19' \
'prettytable     =0003.08' \
'psycopg2        =0002.09' \
'pyarrow         =0013.00' \
'pymongo         =0004.05' \
'pyqt            =0005.15' \
'pyspark         =0003.04' \
'python          =0003.11' \
'pytorch         =0002.00' \
'scikit-learn    =0001.03' \
'scipy           =0001.11' \
'spacy           =0003.06' \
'sphinx          =0005.00' \
'sympy           =0001.12' \
'statsmodels     =0000.14' \
'tabulate        =0000.09' \
'wordcloud       =0001.09'
```

2

```zsh
conda activate ml
```

3

```zsh
python -m pip install jupyter-book
```

4

TensorFlow latest

```zsh
python -m pip install tensorflow
```

TensorFlow 2.12

```zsh
python -m pip install tensorflow-macos==2.12
```

5

[ [d](https://developer.apple.com/metal/tensorflow-plugin/) ][ [p](https://pypi.org/project/tensorflow-metal/) ][ [f](https://developer.apple.com/forums/tags/tensorflow-metal/) ] tensorflow-metal latest

```zsh
python -m pip install tensorflow-metal
```

tensorflow-metal 0.8

```zsh
python -m pip install tensorflow-metal==0.8
```