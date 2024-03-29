#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-cve_bin_tool
Version  : 3.2.1
Release  : 60
URL      : https://files.pythonhosted.org/packages/ac/5b/885a2095381c7c1f942745529a081aa92ded7d430f050b86a2832e850255/cve-bin-tool-3.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/5b/885a2095381c7c1f942745529a081aa92ded7d430f050b86a2832e850255/cve-bin-tool-3.2.1.tar.gz
Summary  : CVE Binary Checker Tool
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0-or-later
Requires: pypi-cve_bin_tool-bin = %{version}-%{release}
Requires: pypi-cve_bin_tool-license = %{version}-%{release}
Requires: pypi-cve_bin_tool-python = %{version}-%{release}
Requires: pypi-cve_bin_tool-python3 = %{version}-%{release}
Requires: pypi(aiodns)
Requires: pypi(brotlipy)
Requires: pypi(chardet)
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build Status](https://github.com/intel/cve-bin-tool/workflows/cve-bin-tool/badge.svg?branch=main&event=push)](https://github.com/intel/cve-bin-tool/actions)
[![codecov](https://codecov.io/gh/intel/cve-bin-tool/branch/main/graph/badge.svg)](https://codecov.io/gh/intel/cve-bin-tool)
[![Gitter](https://badges.gitter.im/cve-bin-tool/community.svg)](https://gitter.im/cve-bin-tool/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![On ReadTheDocs](https://readthedocs.org/projects/cve-bin-tool/badge/?version=latest&style=flat)](https://cve-bin-tool.readthedocs.io/en/latest/)
[![On PyPI](https://img.shields.io/pypi/v/cve-bin-tool)](https://pypi.org/project/cve-bin-tool/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5380/badge)](https://bestpractices.coreinfrastructure.org/projects/5380)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/intel/cve-bin-tool/badge)](https://api.securityscorecards.dev/projects/github.com/intel/cve-bin-tool)

%package bin
Summary: bin components for the pypi-cve_bin_tool package.
Group: Binaries
Requires: pypi-cve_bin_tool-license = %{version}-%{release}

%description bin
bin components for the pypi-cve_bin_tool package.


%package license
Summary: license components for the pypi-cve_bin_tool package.
Group: Default

%description license
license components for the pypi-cve_bin_tool package.


%package python
Summary: python components for the pypi-cve_bin_tool package.
Group: Default
Requires: pypi-cve_bin_tool-python3 = %{version}-%{release}

%description python
python components for the pypi-cve_bin_tool package.


%package python3
Summary: python3 components for the pypi-cve_bin_tool package.
Group: Default
Requires: python3-core
Provides: pypi(cve_bin_tool)
Requires: pypi(aiodns)
Requires: pypi(aiohttp)
Requires: pypi(beautifulsoup4)
Requires: pypi(brotlipy)
Requires: pypi(chardet)
Requires: pypi(cvss)
Requires: pypi(defusedxml)
Requires: pypi(distro)
Requires: pypi(gsutil)
Requires: pypi(jinja2)
Requires: pypi(jsonschema)
Requires: pypi(lib4sbom)
Requires: pypi(packaging)
Requires: pypi(plotly)
Requires: pypi(pyyaml)
Requires: pypi(requests)
Requires: pypi(rich)
Requires: pypi(rpmfile)
Requires: pypi(toml)
Requires: pypi(urllib3)
Requires: pypi(xmlschema)
Requires: pypi(zstandard)

%description python3
python3 components for the pypi-cve_bin_tool package.


%prep
%setup -q -n cve-bin-tool-3.2.1
cd %{_builddir}/cve-bin-tool-3.2.1
pushd ..
cp -a cve-bin-tool-3.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684607964
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . packaging
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . packaging
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cve_bin_tool
cp %{_builddir}/cve-bin-tool-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-cve_bin_tool/a9575dd4ea2e4ba493b8565704699133ef8bc8f9 || :
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} packaging
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## install_append content
# We cannot ship this content unless it is distributed under cve_bin_tool
# site-packages...  or else conflicts may occur with other packages.
rm -rf %{buildroot}/usr/lib/python3*/site-packages/test
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/csv2cve
/usr/bin/cve-bin-tool

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cve_bin_tool/a9575dd4ea2e4ba493b8565704699133ef8bc8f9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
