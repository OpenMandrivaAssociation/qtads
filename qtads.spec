%define name    qtads
%define version 1.7
%define release %mkrel 2

Name:           %{name} 
Summary:        QTads is a GUI interpreter for Tads games
Version:        %{version} 
Release:        %{release} 
Source0:        %{name}-%{version}.tar.bz2
URL:            http://qtads.sourceforge.net/
License:        GPLv2

Group:          Games/Other
BuildRequires:  qt3-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
QTads is a TADS interpreter. TADS is a programming language written by Michael
J. Roberts, designed to implement text-adventure games (Interactive Fiction),
similar to those developed by Infocom in 1980-1990, as well as other companies
(like Legend Entertainment, Level 9, etc). If you liked games like "Zork",
"Adventure", "Trinity", or "Eric the Unready", you'll feel right at home. 

This version of QTads Supports both TADS versions in use today; traditional
TADS 2 as well as the new TADS 3 format. Although it's a non-multimedia
interpreter, it can run games that take advantage of the HTML extensions for
TADS, and supports more HTML-tags than any other non-multimedia interpreter.
It runs on every Unix system for which the Qt library is available, including
Mac OS X.

%files
%defattr(-,root,root,0755)
%doc AUTHORS BUGS COPYING CREDITS NEWS PORTABILITY README TIPS TODO
%{_mandir}/man6/*
%{_bindir}/qtads
%{_datadir}/qtads/charmaps/*
%{_datadir}/qtads/i18n/*

#--------------------------------------------------------------------

%prep
%setup -q

%build 
%qmake_qt3 \
    BIN_INSTALL=%{buildroot}%{_bindir} \
    DOC_INSTALL=%{buildroot}%{_datadir}/doc \
    DATA_INSTALL=%{buildroot}%{_datadir} \
    CFLAGS="$RPM_OPT_FLAGS" \
    CXXFLAGS="$RPM_OPT_FLAGS"

%make

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}%{_mandir}/man6
cp -f %{name}.6.gz %{buildroot}%{_mandir}/man6

%clean
rm -rf %{buildroot}

