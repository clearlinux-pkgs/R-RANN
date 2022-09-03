#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-RANN
Version  : 2.6.1
Release  : 45
URL      : https://cran.r-project.org/src/contrib/RANN_2.6.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RANN_2.6.1.tar.gz
Summary  : Fast Nearest Neighbour Search (Wraps ANN Library) Using L2
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: R-RANN-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
in O(N log N) time using Arya and Mount's ANN library (v1.1.3). There is
    support for approximate as well as exact searches, fixed radius searches
    and 'bd' as well as 'kd' trees. The distance is computed using the L2
    (Euclidean) metric. Please see package 'RANN.L1' for the same
    functionality using the L1 (Manhattan, taxicab) metric.

%package lib
Summary: lib components for the R-RANN package.
Group: Libraries

%description lib
lib components for the R-RANN package.


%prep
%setup -q -c -n RANN
cd %{_builddir}/RANN

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641087701

%install
export SOURCE_DATE_EPOCH=1641087701
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RANN
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RANN
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library RANN
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc RANN || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RANN/COPYRIGHT
/usr/lib64/R/library/RANN/DESCRIPTION
/usr/lib64/R/library/RANN/INDEX
/usr/lib64/R/library/RANN/Meta/Rd.rds
/usr/lib64/R/library/RANN/Meta/features.rds
/usr/lib64/R/library/RANN/Meta/hsearch.rds
/usr/lib64/R/library/RANN/Meta/links.rds
/usr/lib64/R/library/RANN/Meta/nsInfo.rds
/usr/lib64/R/library/RANN/Meta/package.rds
/usr/lib64/R/library/RANN/NAMESPACE
/usr/lib64/R/library/RANN/NEWS.md
/usr/lib64/R/library/RANN/R/RANN
/usr/lib64/R/library/RANN/R/RANN.rdb
/usr/lib64/R/library/RANN/R/RANN.rdx
/usr/lib64/R/library/RANN/help/AnIndex
/usr/lib64/R/library/RANN/help/RANN.rdb
/usr/lib64/R/library/RANN/help/RANN.rdx
/usr/lib64/R/library/RANN/help/aliases.rds
/usr/lib64/R/library/RANN/help/paths.rds
/usr/lib64/R/library/RANN/html/00Index.html
/usr/lib64/R/library/RANN/html/R.css
/usr/lib64/R/library/RANN/tests/testthat.R
/usr/lib64/R/library/RANN/tests/testthat/test-nn.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/RANN/libs/RANN.so
/usr/lib64/R/library/RANN/libs/RANN.so.avx2
/usr/lib64/R/library/RANN/libs/RANN.so.avx512
