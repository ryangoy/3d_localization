TF_INC=$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_include())')
TF_LIB=$(python -c 'import tensorflow as tf; print(tf.sysconfig.get_lib())')
nvcc -std=c++11 -c -o probe.cu.o probe.cu.cc -O2 -I $TF_INC -D GOOGLE_CUDA=1 -x cu -Xcompiler -fPIC -arch=sm_30 --expt-relaxed-constexpr
g++ -std=c++11 -shared -o probe.so probe.cc probe.cu.o -I $TF_INC -fPIC -L /usr/local/cuda-8.0/lib64/ -O2 -L$TF_LIB -D_GLIBCXX_USE_CXX11_ABI=0
