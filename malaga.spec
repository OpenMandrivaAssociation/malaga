%define major	7
%define libname		%mklibname %{name} %{major}
%define develname 	%mklibname %{name} -d
%define debug_package %{nil}

Summary:	A grammar development environment for natural languages
Name:		malaga
Version:	7.12
Release:	8
License:	GPLv2+
Group:		Text tools
URL:		http://home.arcor.de/bjoern-beutel/malaga/
Source:		http://home.arcor.de/bjoern-beutel/malaga/%{name}-%{version}.tgz
# Fix map_file symbol conflict with samba. Upstream can be considered
# inactive but as libvoikko >= 2.2 doesn't use libmalaga anymore, these kind
# of problems won't probably come up.
Patch0:		malaga-rename-map_file.diff

Patch1:		malaga-malshow-lm.patch

BuildRequires:	readline-devel
BuildRequires:	gtk+2-devel
BuildRequires:	glib2-devel
BuildRequires:	chrpath

%description
Malaga is a software package for the development and application of
grammars that are used for the analysis of words and sentences of
natural languages. It contains a programming language for the
modelling of morphology and syntax grammars.

%package -n %{libname}
Summary:	Malaga shared library
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
Malaga is a software package for the development and application of
grammars that are used for the analysis of words and sentences of
natural languages. It contains a programming language for the
modelling of morphology and syntax grammars.

This package contains the library needed to run programs dynamically
linked with Malaga.

%package -n %{develname}
Summary:	Headers and static libraries for Malaga development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}malaga7-devel

%description -n %{develname}
Malaga is a software package for the development and application of
grammars that are used for the analysis of words and sentences of
natural languages. It contains a programming language for the
modelling of morphology and syntax grammars.

This package contains the headers and development symlink to library that
programmers will need to develop applications which will use Malaga.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x \
	--disable-rpath \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_INFO=true
chrpath -d %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/*.so

%files
%doc CHANGES.txt README.txt
%{_bindir}/mal*
%{_datadir}/%{name}
%{_infodir}/%{name}*
%{_mandir}/man1/mal*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%{_libdir}/lib%{name}.so
%{_includedir}/malaga.h



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 7.12-6mdv2011.0
+ Revision: 666362
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 7.12-5mdv2011.0
+ Revision: 606624
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 7.12-4mdv2010.1
+ Revision: 520166
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 7.12-3mdv2010.0
+ Revision: 426070
- rebuild

* Wed Feb 25 2009 Thierry Vignaud <tv@mandriva.org> 7.12-2mdv2009.1
+ Revision: 344818
- rebuild for new libreadline

* Mon Jun 09 2008 Pixel <pixel@mandriva.com> 7.12-1mdv2009.0
+ Revision: 217193
- do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Mar 03 2008 Anssi Hannula <anssi@mandriva.org> 7.12-1mdv2008.1
+ Revision: 178193
- new version
- drop rpaths

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 7.11-1mdv2008.1
+ Revision: 140944
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 09 2007 Anssi Hannula <anssi@mandriva.org> 7.11-1mdv2008.0
+ Revision: 50739
- 7.11
- apply new devel policy


* Sun Oct 29 2006 Anssi Hannula <anssi@mandriva.org> 7.9-2mdv2007.0
+ Revision: 73660
- add man pages
- 7.9
- Import malaga

* Sun Aug 13 2006 Anssi Hannula <anssi@mandriva.org> 7.5-1mdv2007.0
- initial Mandriva release

