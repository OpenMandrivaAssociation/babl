%define major 0
%define api 0.1
%define libname %mklibname %name %{api}_%{major}
%define develname %mklibname -d %{name} %{api} 

Name:		babl
Epoch:		1
Version:	0.1.10
Release:	1
Summary:	Babl - dynamic, any to any, pixel format conversion library	
Group:		System/Libraries
License:	LGPLv3+
URL:		http://www.gegl.org/babl
Source0:	ftp://ftp.gimp.org/pub/babl/0.1/%{name}-%{version}.tar.bz2
BuildRequires:	librsvg

%description
Babl is a dynamic, any to any, pixel format conversion library. 
It provides conversions between the myriad of buffer types images 
can be stored in. Babl doesn't only help with existing pixel formats, 
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as 
conversions between them.

%package -n %{libname}
Summary:	A library for %name
Group:		System/Libraries
Provides: 	%libname = %{version}-%{release}

%description -n %{libname}
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%package -n     %{develname}
Summary:        Header files for %name 
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%prep
%setup -q 

%build
%configure2_5x \
	--disable-static 

%make

%install
rm -fr %buildroot installed-docs
%makeinstall
cp -r docs installed-docs
cd installed-docs
rm -rf tools Makefile* *.in graphics/Makefile*
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';' 

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
%{_libdir}/babl-%{api}/sse-fixups.so*
%{_libdir}/babl-%{api}/cairo.so*
%{_libdir}/babl-%{api}/fast-float.so*
%{_libdir}/babl-%{api}/float.so*

%files -n %{develname}
%doc ChangeLog installed-docs/*
%{_libdir}/libbabl-%{api}.so
%{_libdir}/pkgconfig/babl.pc
%dir %{_includedir}/babl-%{api}/babl
%{_includedir}/babl-%{api}/babl/*

