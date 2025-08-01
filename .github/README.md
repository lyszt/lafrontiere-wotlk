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
