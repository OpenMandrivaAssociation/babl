%define major 0
%define libname %mklibname %name %{major}
%define develname %mklibname -d %{name}

Name:		babl
Version:	0.0.22
Release:	%mkrel 1
Epoch:		1
Summary:        Babl - dynamic, any to any, pixel format conversion library	
Group:		System/Libraries
License:	LGPLv3+
URL:		http://www.gegl.org/babl
Source0:	%{name}-%{version}.tar.bz2
Patch0:		babl-0.0.22-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%description -n %{develname}
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%prep
%setup -q 
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -fr %buildroot installed-docs
%makeinstall_std
cp -r docs installed-docs
cd installed-docs
rm -rf tools Makefile* *.in graphics/Makefile*

%clean
rm -fr %buildroot

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc README NEWS TODO AUTHORS
%{_libdir}/libbabl-0.0.so.%{major}*
%dir %{_libdir}/babl-0.0/
%{_libdir}/babl-0.0/gggl.so
%{_libdir}/babl-0.0/naive-CMYK.so
%{_libdir}/babl-0.0/gimp-8bit.so
%{_libdir}/babl-0.0/CIE-Lab.so
%{_libdir}/babl-0.0/gegl-fixups.so
%{_libdir}/babl-0.0/gggl-lies.so
%{_libdir}/babl-0.0/sse-fixups.so

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog installed-docs/*
%{_libdir}/libbabl-0.0.la
%{_libdir}/libbabl-0.0.so
%{_libdir}/pkgconfig/babl.pc
%dir %{_includedir}/babl-0.0/babl
%{_includedir}/babl-0.0/babl/*

