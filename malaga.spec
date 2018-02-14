%define debug_package %{nil}
%define major	7
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

%define _disable_lto 1

Summary:	A grammar development environment for natural languages
Name:		malaga
Version:	7.12
Release:	19
License:	GPLv2+
Group:		Text tools
Url:		http://home.arcor.de/bjoern-beutel/malaga/
Source0:	http://home.arcor.de/bjoern-beutel/malaga/%{name}-%{version}.tgz
# Fix map_file symbol conflict with samba. Upstream can be considered
# inactive but as libvoikko >= 2.2 doesn't use libmalaga anymore, these kind
# of problems won't probably come up.
Patch0:	malaga-rename-map_file.diff
Patch1:	malaga-malshow-lm.patch

BuildRequires:	chrpath
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)

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
This package contains the library needed to run programs dynamically
linked with Malaga.

%package -n %{devname}
Summary:	Headers and development libraries for Malaga development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the headers and development symlink to library that
programmers will need to develop applications which will use Malaga.

%prep
%setup -q
%apply_patches

%build
%configure
%make

%install
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

%files -n %{devname}
%{_libdir}/lib%{name}.so
%{_includedir}/malaga.h
