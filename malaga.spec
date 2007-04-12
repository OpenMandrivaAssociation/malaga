
%define name	malaga
%define version	7.9
%define rel	2

%define major	7
%define libname	%mklibname %name %major

Summary:	A grammar development environment for natural languages
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	GPL
Group:		Text tools
URL:		http://home.arcor.de/bjoern-beutel/malaga/
Source:		http://home.arcor.de/bjoern-beutel/malaga/%name-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	readline-devel
BuildRequires:	gtk+2-devel
BuildRequires:	glib2-devel
Requires(post):	info-install
Requires(preun): info-install

%description
Malaga is a software package for the development and application of
grammars that are used for the analysis of words and sentences of
natural languages. It contains a programming language for the
modelling of morphology and syntax grammars.

%package -n %libname
Summary:	Malaga shared library
Group:		System/Libraries
Provides:	lib%name = %version-%release

%description -n %libname
Malaga is a software package for the development and application of
grammars that are used for the analysis of words and sentences of
natural languages. It contains a programming language for the
modelling of morphology and syntax grammars.

This package contains the library needed to run programs dynamically
linked with Malaga.

%package -n %libname-devel
Summary:	Headers and static libraries for Malaga development
Group:		Development/C
Requires:	%libname = %version
Provides:	lib%name-devel = %version-%release
Provides:	%name-devel = %version-%release

%description -n %libname-devel
Malaga is a software package for the development and application of
grammars that are used for the analysis of words and sentences of
natural languages. It contains a programming language for the
modelling of morphology and syntax grammars.

This package contains the headers and static library that
programmers will need to develop applications which will use Malaga.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall INSTALL_INFO=true

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%post
%_install_info %name

%preun
%_remove_install_info %name

%files
%defattr(-,root,root)
%doc CHANGES.txt README.txt
%{_bindir}/mal*
%{_datadir}/%{name}
%{_infodir}/%{name}*
%{_mandir}/man1/mal*

%files -n %libname
%doc README.txt
%{_libdir}/lib%{name}.so.%{major}*

%files -n %libname-devel
%doc README.txt
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.la
%{_libdir}/lib%{name}.so
%{_includedir}/malaga.h


