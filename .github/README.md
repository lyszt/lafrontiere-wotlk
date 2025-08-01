# Build Instructions

> **Note:**  
> If you use a non-default package for `clang`, replace `clang` and `clang++` accordingly.  
> For example, if you installed `clang-6.0`, replace `clang` with `clang-6.0` and `clang++` with `clang++-6.0`.

---

## Configure with CMake

```bash
cmake ../ \
  -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ \
  -DCMAKE_C_COMPILER=/usr/bin/clang \
  -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
  -DWITH_WARNINGS=1 \
  -DTOOLS_BUILD=all \
  -DSCRIPTS=static \
  -DMODULES=static
Determine number of cores available

To get the total number of CPU cores, run:

nproc --all

Set the number of cores to build with (replace or adjust as needed):

export BUILD_CORES=$(nproc | awk '{print $1 - 1}')

Build and install

Run:

make -j$BUILD_CORES
make install

Automation script example

It is useful to preserve these commands in a script for easy reuse after updates or module changes:

#!/bin/bash

BUILD_CORES=$(nproc | awk '{print $1 - 1}')
cmake ../ \
  -DCMAKE_INSTALL_PREFIX=$AC_CODE_DIR/env/dist/ \
  -DCMAKE_C_COMPILER=/usr/bin/clang \
  -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
  -DWITH_WARNINGS=1 \
  -DTOOLS_BUILD=all \
  -DSCRIPTS=static \
  -DMODULES=static &&

make -j$BUILD_CORES &&

make install

Reminder:
You must re-run the cmake, make, and make install commands each time you update AzerothCore or add new modules.
