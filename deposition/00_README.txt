# Supporting Data for: Direct multi-modal inversion of geophysical logs using deep learning

The dataset contains realizations of geological stratigraphic curves 
which were generated using the included script. 
This data is required to replicate results in Sergey Alyaev and Ahmed H. Elsheikh.
"Direct multi-modal inversion of geophysical logs using deep learning."
arXiv preprint arXiv:2201.01871 (2021).

## Description of files

### .nc files
1. test.nc 
* <class 'netCDF4._netCDF4.Dataset'>
* root group (NETCDF4_CLASSIC data model, file format HDF5):
* dimensions(sizes): md(300), realization(2000)
* variables(dimensions): float64 angle(realization, md), float64 svd(realization, md), float64 vs(realization, md)
2. train.nc
* <class 'netCDF4._netCDF4.Dataset'>
* root group (NETCDF4_CLASSIC data model, file format HDF5):
* dimensions(sizes): md(300), realization(100000)
* variables(dimensions): float64 angle(realization, md), float64 svd(realization, md), float64 vs(realization, md)


The testing and training datasets containing geological stratigraphic curves,
also referred to as stratigraphic vertical depth functions.
The files are generated from the data used in the paper.

Each nc file is split into realizations of a curve along **realization** axis.

For each realization there are data series in **md** (measured depth).

For each **md** the curve contains three variables:

1. **angle**, *rad*: the local inclination of the curve from vertical axis.
2. **svd**, *ft*: the stratigraphic vertical depth (relative) of the given point in feet.
3. **vs**, *ft*: the vertical section (relative) horizontal coordinate of the given point in feet.

### .py files
1. **generate_stratum_trend_based.py**: the python script used to generate and save the data in the numpy format (.npz)
2. **netcdf_conversion.py**: the python script used to convert the data from the numpy format (.npz) to the universal (.nc) format described above
3. **trajectories_data_set.py**: the python script that loads the data from the .npz format to pytorch as described in the publication.

### LICENSE
The license for the code and the data.

### trajcetories.png
Example of visualization of the geological stratigraphic curves from the dataset

### README and README.md 
This read-me file.

## How to Cite:

This dtaaset generator is prepared for the paper. 

### To cite the paper

Alyaev, S., & Elsheikh, A. H. (2021). Direct multi-modal inversion of geophysical logs using deep learning. 
arXiv preprint arXiv:2201.01871. https://arxiv.org/abs/2201.01871

#### Bibtex

```
@misc{https://doi.org/10.48550/arxiv.2201.01871,
  doi = {10.48550/ARXIV.2201.01871},
  url = {https://arxiv.org/abs/2201.01871},
  author = {Alyaev, Sergey and Elsheikh, Ahmed H.},
  title = {Direct multi-modal inversion of geophysical logs using deep learning},
  publisher = {arXiv},
  year = {2022},
}
```


### To cite the dataset itself


Alyaev, Sergey, 2022, **"Supporting Data for: Direct multi-modal inversion of geophysical logs using deep learning"**, 
https://doi.org/10.18710/1F9GYH, DataverseNO


#### Bibtex

```
@data{stratumcurves,
author = {Alyaev, Sergey},
publisher = {DataverseNO},
title = {{Supporting Data for: Direct multi-modal inversion of geophysical logs using deep learning}},
year = {2022},
version = {DRAFT VERSION},
doi = {10.18710/1F9GYH},
url = {https://doi.org/10.18710/1F9GYH}
}
```

### Generator code

Alyaev, S. (2021). **A dataset generator for geological stratum curves**. 
https://github.com/alin256/stratum-curve-dataset-generator.

#### Bibtex
```
@misc{stratumcurves,
  title = {A dataset generator for geological stratum curves},
  howpublished = {\url{https://github.com/alin256/stratum-curve-dataset-generator}},
  year = {2021},
  author = {Alyaev, Sergey}
}
```

## Acknowledgements

This work is part of the Center for Research-based Innovation DigiWells:
Digital Well Center for Value Creation, Competitiveness and Minimum Environmental Footprint (NFR SFI project no. 309589, DigiWells.no).
The center is a cooperation of NORCE Norwegian Research Centre, the University of Stavanger,
the Norwegian University of Science and Technology (NTNU), and the University of Bergen, and
funded by the Research Council of Norway, Aker BP, ConocoPhillips, Equinor, Lundin, Total, and Wintershall Dea.

