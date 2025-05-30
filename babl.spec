%define url_ver %(echo %{version}|cut -d. -f1,2)

%global optflags %{optflags} -O3

%define major	0
%define api	0.1
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname -d %{name} %{api}
%define girname %mklibname %{name}-gir %{api}

Summary:	Dynamic, any to any, pixel format conversion library
Name:		babl
Epoch:		1
Version:	0.1.114
Release:	1
Group:		System/Libraries
License:	LGPLv3+
Url:		https://www.gegl.org/babl
Source0:	https://download.gimp.org/pub/babl/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	meson
BuildRequires:	cmake
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)
# for rsvg-convert
BuildRequires:  librsvg
#to do
#w3m

Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}


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
Requires:	%{name} = %{EVRD}

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
Requires:	%{girname} = %{EVRD}
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
cp -r docs installed-docs
cd installed-docs
rm -rf tools Makefile* *.in graphics/Makefile*

%files
%{_bindir}/babl

%files -n %{libname}
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
%{_libdir}/babl-%{api}/u16.so*
%{_libdir}/babl-%{api}/u32.so*
%{_libdir}/babl-%{api}/half.so*
%{_libdir}/babl-%{api}/double.so*
%{_libdir}/babl-%{api}/HSL.so*
%{_libdir}/babl-%{api}/HSV.so*
%{_libdir}/babl-%{api}/grey.so*
%{_libdir}/babl-%{api}/simple.so*
%{_libdir}/babl-%{api}/two-table.so*
%{_libdir}/babl-%{api}/ycbcr.so*
%{_libdir}/babl-%{api}/HCY.so
%{_libdir}/babl-%{api}/oklab.so*
%{_libdir}/babl-%{api}/gggl-table-lies.so
%{_libdir}/babl-%{api}/gggl-table.so
%{_libdir}/babl-0.1/formats.so
%optional %{_libdir}/babl-%{api}/sse2-float.so*
%optional %{_libdir}/babl-%{api}/sse2-int16.so*
%optional %{_libdir}/babl-%{api}/sse2-int8.so*
%optional %{_libdir}/babl-%{api}/sse-half.so
%optional %{_libdir}/babl-%{api}/sse4-int8.so
%optional %{_libdir}/babl-%{api}/avx2-int8.so
%optional %{_libdir}/babl-%{api}/x86-64-v*

%files -n %{devname}
%doc NEWS TODO AUTHORS
%doc installed-docs/*
%doc %{_datadir}/doc/babl-0.1/
%{_libdir}/libbabl-%{api}.so
%{_libdir}/pkgconfig/babl-%{api}.pc
%dir %{_includedir}/babl-%{api}/babl
%{_includedir}/babl-%{api}/babl/*
%{_datadir}/gir-1.0/Babl-0.1.gir
%{_datadir}/vala/vapi/babl-0.1.deps
%{_datadir}/vala/vapi/babl-0.1.vapi

%files -n %{girname}
%{_libdir}/girepository-1.0/Babl-%{api}.typelib
