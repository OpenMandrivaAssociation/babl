%define major 0
%define api 0.1
%define libname %mklibname %name %{api}_%{major}
%define develname %mklibname -d %{name} %{api} 

Name:		babl
Version:	0.1.4
Release:	%mkrel 1
Epoch:		1
Summary:	Babl - dynamic, any to any, pixel format conversion library	
Group:		System/Libraries
License:	LGPLv3+
URL:		http://www.gegl.org/babl
Source0:	ftp://ftp.gimp.org/pub/babl/0.1/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	librsvg

%description
Babl is a dynamic, any to any, pixel format conversion library. 
It provides conversions between the myriad of buffer types images 
can be stored in. Babl doesn't only help with existing pixel formats, 
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as 
conversions between them.

%package -n     %{libname}
Summary:        A library for %name
Group:          System/Libraries
Provides: 	%libname = %{version}-%{release}
Obsoletes:	%{_lib}babel14

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
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}babel14-devel
Obsoletes:	%{libname}-devel
Obsoletes:	%{_lib}%{name}-devel

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
%configure2_5x --disable-static 
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

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
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
#%{_libdir}/babl-%{api}/*.la

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog installed-docs/*
#%{_libdir}/libbabl-%{api}.la
%{_libdir}/libbabl-%{api}.so
%{_libdir}/pkgconfig/babl.pc
%dir %{_includedir}/babl-%{api}/babl
%{_includedir}/babl-%{api}/babl/*

