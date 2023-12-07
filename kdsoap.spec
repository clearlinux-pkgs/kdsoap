#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0x3DBFB6882C9358FB (info@kdab.com)
#
Name     : kdsoap
Version  : 2.1.1
Release  : 6
URL      : https://github.com/KDAB/KDSoap/releases/download/kdsoap-2.1.1/kdsoap-2.1.1.tar.gz
Source0  : https://github.com/KDAB/KDSoap/releases/download/kdsoap-2.1.1/kdsoap-2.1.1.tar.gz
Source1  : https://github.com/KDAB/KDSoap/releases/download/kdsoap-2.1.1/kdsoap-2.1.1.tar.gz.asc
Summary  : A Qt6-based client-side and server-side SOAP component
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 MIT
Requires: kdsoap-bin = %{version}-%{release}
Requires: kdsoap-data = %{version}-%{release}
Requires: kdsoap-lib = %{version}-%{release}
Requires: kdsoap-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : texlive
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
KDSoap can be used to create client applications for web services
and also provides the means to create web services without the need
for any further component such as a dedicated web server.

Authors:
--------
      Klaralvdalens Datakonsult AB (KDAB) <info@kdab.com>

%package bin
Summary: bin components for the kdsoap package.
Group: Binaries
Requires: kdsoap-data = %{version}-%{release}
Requires: kdsoap-license = %{version}-%{release}

%description bin
bin components for the kdsoap package.


%package data
Summary: data components for the kdsoap package.
Group: Data

%description data
data components for the kdsoap package.


%package dev
Summary: dev components for the kdsoap package.
Group: Development
Requires: kdsoap-lib = %{version}-%{release}
Requires: kdsoap-bin = %{version}-%{release}
Requires: kdsoap-data = %{version}-%{release}
Provides: kdsoap-devel = %{version}-%{release}
Requires: kdsoap = %{version}-%{release}

%description dev
dev components for the kdsoap package.


%package doc
Summary: doc components for the kdsoap package.
Group: Documentation

%description doc
doc components for the kdsoap package.


%package lib
Summary: lib components for the kdsoap package.
Group: Libraries
Requires: kdsoap-data = %{version}-%{release}
Requires: kdsoap-license = %{version}-%{release}

%description lib
lib components for the kdsoap package.


%package license
Summary: license components for the kdsoap package.
Group: Default

%description license
license components for the kdsoap package.


%prep
%setup -q -n kdsoap-2.1.1
cd %{_builddir}/kdsoap-2.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701986718
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1701986718
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdsoap
cp %{_builddir}/kdsoap-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kdsoap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kdsoap-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kdsoap/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/kdsoap-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kdsoap/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kdwsdl2cpp

%files data
%defattr(-,root,root,-)
/usr/share/mkspecs/features/kdsoap.prf

%files dev
%defattr(-,root,root,-)
/usr/include/KDSoapClient/KDDateTime
/usr/include/KDSoapClient/KDDateTime.h
/usr/include/KDSoapClient/KDQName
/usr/include/KDSoapClient/KDQName.h
/usr/include/KDSoapClient/KDSoap
/usr/include/KDSoapClient/KDSoap.h
/usr/include/KDSoapClient/KDSoapAuthentication
/usr/include/KDSoapClient/KDSoapAuthentication.h
/usr/include/KDSoapClient/KDSoapClient
/usr/include/KDSoapClient/KDSoapClientInterface
/usr/include/KDSoapClient/KDSoapClientInterface.h
/usr/include/KDSoapClient/KDSoapEndpointReference
/usr/include/KDSoapClient/KDSoapEndpointReference.h
/usr/include/KDSoapClient/KDSoapFaultException
/usr/include/KDSoapClient/KDSoapFaultException.h
/usr/include/KDSoapClient/KDSoapGlobal
/usr/include/KDSoapClient/KDSoapGlobal.h
/usr/include/KDSoapClient/KDSoapHeaders
/usr/include/KDSoapClient/KDSoapJob
/usr/include/KDSoapClient/KDSoapJob.h
/usr/include/KDSoapClient/KDSoapMessage
/usr/include/KDSoapClient/KDSoapMessage.h
/usr/include/KDSoapClient/KDSoapMessageAddressingProperties
/usr/include/KDSoapClient/KDSoapMessageAddressingProperties.h
/usr/include/KDSoapClient/KDSoapNamespaceManager
/usr/include/KDSoapClient/KDSoapNamespaceManager.h
/usr/include/KDSoapClient/KDSoapPendingCall
/usr/include/KDSoapClient/KDSoapPendingCall.h
/usr/include/KDSoapClient/KDSoapPendingCallWatcher
/usr/include/KDSoapClient/KDSoapPendingCallWatcher.h
/usr/include/KDSoapClient/KDSoapSslHandler
/usr/include/KDSoapClient/KDSoapSslHandler.h
/usr/include/KDSoapClient/KDSoapUdpClient
/usr/include/KDSoapClient/KDSoapUdpClient.h
/usr/include/KDSoapClient/KDSoapValue
/usr/include/KDSoapClient/KDSoapValue.h
/usr/include/KDSoapClient/KDSoapValueList
/usr/include/KDSoapClient/kdsoap_version.h
/usr/include/KDSoapServer/KDSoapDelayedResponseHandle
/usr/include/KDSoapServer/KDSoapDelayedResponseHandle.h
/usr/include/KDSoapServer/KDSoapServer
/usr/include/KDSoapServer/KDSoapServer.h
/usr/include/KDSoapServer/KDSoapServerAuthInterface
/usr/include/KDSoapServer/KDSoapServerAuthInterface.h
/usr/include/KDSoapServer/KDSoapServerCustomVerbRequestInterface
/usr/include/KDSoapServer/KDSoapServerCustomVerbRequestInterface.h
/usr/include/KDSoapServer/KDSoapServerGlobal
/usr/include/KDSoapServer/KDSoapServerGlobal.h
/usr/include/KDSoapServer/KDSoapServerObjectInterface
/usr/include/KDSoapServer/KDSoapServerObjectInterface.h
/usr/include/KDSoapServer/KDSoapServerRawXMLInterface
/usr/include/KDSoapServer/KDSoapServerRawXMLInterface.h
/usr/include/KDSoapServer/KDSoapThreadPool
/usr/include/KDSoapServer/KDSoapThreadPool.h
/usr/lib64/cmake/KDSoap/KDSoapConfig.cmake
/usr/lib64/cmake/KDSoap/KDSoapConfigVersion.cmake
/usr/lib64/cmake/KDSoap/KDSoapMacros.cmake
/usr/lib64/cmake/KDSoap/KDSoapTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KDSoap/KDSoapTargets.cmake
/usr/lib64/libkdsoap-server.so
/usr/lib64/libkdsoap.so
/usr/lib64/qt5/mkspecs/modules/qt_KDSoapClient.pri
/usr/lib64/qt5/mkspecs/modules/qt_KDSoapServer.pri

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/KDSoap/LICENSES/BSD-3-Clause.txt
/usr/share/doc/KDSoap/LICENSES/GPL-2.0-only.txt
/usr/share/doc/KDSoap/LICENSES/LicenseRef-Microsoft.txt
/usr/share/doc/KDSoap/LICENSES/LicenseRef-Novell.txt
/usr/share/doc/KDSoap/LICENSES/LicenseRef-OASIS.txt
/usr/share/doc/KDSoap/LICENSES/LicenseRef-SportingExchange.txt
/usr/share/doc/KDSoap/LICENSES/MIT.txt
/usr/share/doc/KDSoap/LICENSES/W3C.txt
/usr/share/doc/KDSoap/README.md
/usr/share/doc/KDSoap/kdsoap.pri
/usr/share/doc/KDSoap/kdwsdl2cpp.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdsoap-server.so.2
/usr/lib64/libkdsoap-server.so.2.1.1
/usr/lib64/libkdsoap.so.2
/usr/lib64/libkdsoap.so.2.1.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdsoap/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/kdsoap/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kdsoap/adadb67a9875aeeac285309f1eab6e47d9ee08a7
