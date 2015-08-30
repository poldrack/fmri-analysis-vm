#!/usr/bin/env bash

pip install seaborn
pip install --upgrade https://github.com/nipy/nipype/archive/master.zip
conda install h5py

python analysis/firstlevel/fix_json.py
python analysis/firstlevel/downsample_fmri.py

