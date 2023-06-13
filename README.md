# pinn-for-physiological-timeseries
Python code and data files for building a pinn Bio-Z to BP model.

## Using this repository
If you find this code useful in your research, please consider citing the original paper:

Sel, K., Mohammadi, A., Pettigrew, R.I., Jafari, R. Physics-informed neural networks for modeling physiological time series for cuffless blood pressure estimation. npj Digit. Med. 6, 110 (2023). https://doi.org/10.1038/s41746-023-00853-4
```
@article{sel2023physics,
  title={Physics-informed neural networks for modeling physiological time series for cuffless blood pressure estimation},
  author={Sel, Kaan and Mohammadi, Amirmohammad and Pettigrew, Roderic I and Jafari, Roozbeh},
  journal={npj Digital Medicine},
  volume={6},
  number={1},
  pages={110},
  year={2023},
  publisher={Nature Publishing Group UK London}
}
```

## Installation of Packages
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.
```bash
pip install numpy 
pip install pandas
pip install tensorflow
pip install sklearn
```

## Requirements
```python
numpy == 1.22.3
pandas == 1.4.3
tensorflow == 2.7.0
sklearn == 1.1.1
```

## Usage
To run the model results for the pinn Bio-Z to BP estimation run:
```bash
main.ipynb
```

