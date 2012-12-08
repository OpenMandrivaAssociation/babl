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
Summary:	A library for %{name}
Group:		System/Libraries

%description -n %{libname}
Babl is a dynamic, any to any, pixel format conversion library.
It provides conversions between the myriad of buffer types images
can be stored in. Babl doesn't only help with existing pixel formats,
but also facilitates creation of new and uncommon ones.

GEGL uses babl both for enumeration of pixel formats as well as
conversions between them.

%package -n %{develname}
Summary:	Header files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

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



%changelog
* Wed Apr 18 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:0.1.10-1
+ Revision: 791675
- version update 0.1.10

* Fri Dec 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:0.1.6-1
+ Revision: 744657
- new version 0.1.6
- cleaned up spec

* Wed Apr 20 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:0.1.4-1
+ Revision: 656276
- new version 0.1.4

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.1.2-2mdv2011.0
+ Revision: 603754
- rebuild

* Sat Feb 13 2010 Emmanuel Andry <eandry@mandriva.org> 1:0.1.2-1mdv2010.1
+ Revision: 505542
- New version 0.1.2
- use api major
- drop patch (now useless)
- remove static
- enable check
- update files list

* Tue Jul 07 2009 Götz Waschk <waschk@mandriva.org> 1:0.1.0-1mdv2010.0
+ Revision: 393147
- new version
- source URL
- update file list
- fix installation

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 1:0.0.22-1mdv2009.1
+ Revision: 364695
- fix str fmt

* Tue Jun 24 2008 Götz Waschk <waschk@mandriva.org> 1:0.0.22-1mdv2009.0
+ Revision: 228534
- new version
- fix spec file mess
- move modules to the library package
- add documentation

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 16 2008 Emmanuel Andry <eandry@mandriva.org> 1:0.0.20-3mdv2009.0
+ Revision: 194643
- Add needed provides

* Wed Apr 16 2008 Emmanuel Andry <eandry@mandriva.org> 1:0.0.20-2mdv2009.0
+ Revision: 194610
- Fix devel package
- obsolete wrong majors

* Fri Apr 11 2008 Emmanuel Andry <eandry@mandriva.org> 1:0.0.20-1mdv2009.0
+ Revision: 192590
- New version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix %%major (tks misc)

* Wed Jun 13 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.0.14-1mdv2008.0
+ Revision: 38582
- Import babl

