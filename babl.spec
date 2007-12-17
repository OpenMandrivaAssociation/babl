%define major 0
%define libname %mklibname %name %{major}

Name:		babl
Version:	0.0.14
Release:	%mkrel 2
Epoch:		1
Summary:        Babl - dynamic, any to any, pixel format conversion library	
Group:		System/Libraries
License:	GPL
URL:		http://www.gegl.org/babl
Source0:	%{name}-%{version}.tar.bz2

%description
Babl is a dynamic, any to any, pixel format conversion library. 
It provides conversions between the myriad of buffer types images 
can be stored in. Babl doesn't only help with existing pixel formats, 
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as 
conversions between them.

%files
%defattr(-,root,root)

#--------------------------------------------------------------------

%package -n     %{libname}
Summary:        A library for %name
Group:          System/Libraries

%description -n %{libname}
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n     %{libname}
%defattr(-,root,root)
%{_libdir}/libbabl-0.0.so.0
%{_libdir}/libbabl-0.0.so.0.%major.0

#--------------------------------------------------------------------
%package -n     %{libname}-devel
Summary:        Header files for %name 
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/babl-0.0/gggl.so
%{_libdir}/babl-0.0/naive-CMYK.so
%{_libdir}/libbabl-0.0.la
%{_libdir}/libbabl-0.0.so
%{_libdir}/pkgconfig/babl.pc
%dir %{_includedir}/babl-0.0/babl
%{_includedir}/babl-0.0/babl/babl-classes.h
%{_includedir}/babl-0.0/babl/babl.h
%{_libdir}/babl-0.0/CIE-Lab.so
%{_libdir}/babl-0.0/gegl-fixups.so
%{_libdir}/babl-0.0/gggl-lies.so

#--------------------------------------------------------------------
%prep

%setup -q 
%build

%configure
%make

%install
%makeinstall

%clean
rm -fr %buildroot
