# Sparse Sampling Neural Networks #

Created by Ryan Goy, Arda Sahiner, and Avideh Zakhor from UC Berkeley

See the doc <a href="https://docs.google.com/document/d/1E5_oou9kKTJgE75LKNbSj97P0fbE-whwJY6ZYSJn5_8/edit?usp=sharing">here</a>


# Dependencies #
 - Tensorflow 1.3+
 - Pillow
 - scipy
 - numpy

# Run instructions #
```
cd src
bash compile_probe.sh
```

# Bugs and how to resolve them #
## Fatal error: nsync_cv.h: No such file or directory ##
```
sudo find / -name nsync_cv.h
```
Then, edit the mutix.h file reference in the error and change the nsync_cv.h and nsync_mu.h to any of the paths listed from the find command.

## ValueError: invalid literal for float(): ... ##
This seems to occur randomly when reading in the dataset. Navigate to the problem file and search for the invalid character and delete it.

## undefined symbol: _ZN10tensorflow8internal21CheckOpMessageBuilder9NewStringB5cxx11Ev ##
Add (or delete) the flag -D_GLIBCXX_USE_CXX11_ABI=0

## libcudart.so.9.1: cannot open shared object file: No such file or directory ##
Run the following lines:
```
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"
export CUDA_HOME="/usr/local/cuda"
```
This will have to be run per terminal instance. To add it permanently, add it to the ~/.bashrc file.

## InvalidArgumentError (see above for traceback): No OpKernel was registered to support Op 'Probe' with these attrs.  Registered devices: [CPU] ##
This might mean that NVML is not initialized properly. Run nvidia-smi to confirm. Rebooting often solves this issue.
