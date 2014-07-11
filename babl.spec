%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	0
%define api	0.1
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname -d %{name} %{api}

Summary:	Dynamic, any to any, pixel format conversion library
Name:		babl
Epoch:		1
Version:	0.1.11
Release:	3
Group:		System/Libraries
License:	LGPLv3+
Url:		http://www.gegl.org/babl
Source0:	http://ftp.gimp.org/pub/babl/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	librsvg

%description
Babl is a dynamic, any to any, pixel format conversion library. 
It provides conversions between the myriad of buffer types images 
can be stored in. Babl doesn't only help with existing pixel formats, 
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as 
conversions between them.

%package -n %{libname}
Summary:	A library for %{name}
Group:		System/Libraries

%description -n %{libname}
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%package -n %{devname}
Summary:	Header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
cp -r docs installed-docs
cd installed-docs
rm -rf tools Makefile* *.in graphics/Makefile*

%check
make check

%files -n %{libname}
%doc README NEWS TODO AUTHORS
%{_libdir}/libbabl-%{api}.so.%{major}*
%dir %{_libdir}/babl-%{api}/
%{_libdir}/babl-%{api}/gggl.so*
%{_libdir}/babl-%{api}/naive-CMYK.so*
%{_libdir}/babl-%{api}/gimp-8bit.so*
%{_libdir}/babl-%{api}/CIE.so*
%{_libdir}/babl-%{api}/gegl-fixups.so*
%{_libdir}/babl-%{api}/gggl-lies.so*
%{_libdir}/babl-%{api}/cairo.so*
%{_libdir}/babl-%{api}/fast-float.so*
%{_libdir}/babl-%{api}/float.so*
%{_libdir}/babl-%{api}/HSL.so*
%{_libdir}/babl-%{api}/HSV.so*
%{_libdir}/babl-%{api}/grey.so*
%{_libdir}/babl-%{api}/simple.so*
%{_libdir}/babl-%{api}/sse2-float.so*
%{_libdir}/babl-%{api}/sse2-int16.so*
%{_libdir}/babl-%{api}/sse2-int8.so*
%{_libdir}/babl-%{api}/two-table.so*
%{_libdir}/babl-%{api}/ycbcr.so*

%files -n %{devname}
%doc installed-docs/*
%{_libdir}/libbabl-%{api}.so
%{_libdir}/pkgconfig/babl.pc
%dir %{_includedir}/babl-%{api}/babl
%{_includedir}/babl-%{api}/babl/*

