#!/bin/bash

set -e

pip install pybids

if [[ ! -d ~/data/ds114 ]]; then wget -c -O ${HOME}/ds114.zip "https://files.osf.io/v1/resources/9q7dv/providers/osfstorage/58a60e8a9ad5a101fbb2570b" && mkdir -p ${HOME}/data && unzip ${HOME}/ds114.zip -d ${HOME}/data; fi
