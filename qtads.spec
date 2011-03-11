%define name    qtads
%define version 2.1.1
%define release %mkrel 1

Name:           %{name} 
Summary:        GUI multimedia interpreter for TADS games
Version:        %{version} 
Release:        %{release} 
Source0:	http://downloads.sourceforge.net/project/qtads/qtads-2.x/%{version}/%{name}-%{version}.tar.bz2
URL:            http://qtads.sourceforge.net/
License:        GPLv2+

Group:          Games/Other
BuildRequires:  qt4-devel SDL-devel SDL_mixer-devel SDL_sound-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot
Suggests:	timidity-instruments

%description
QTads is a cross-platform multimedia interpreter for Tads (Text Adventure 
Development System) games. Both Tads versions in use today (Tads 2 and Tads 3)
are supported. MIDI, Ogg Vorbis, MP3, and WAV sound formats are supported.

TADS is a programming language written by Michael J. Roberts, designed to 
implement text-adventure games (Interactive Fiction), similar to those 
developed by Infocom in 1980-1990, as well as other companies (like Legend 
Entertainment, Level 9, etc). If you liked games like "Zork", "Adventure", 
"Trinity", or "Eric the Unready", you'll feel right at home.

%files
%defattr(-,root,root,0755)
%doc AUTHORS BUGS COPYING INSTALL NEWS README HTML_TADS_LICENSE
%{_mandir}/man6/*
%{_bindir}/qtads
#%{_datadir}/qtads/charmaps/* #no more needed ?
#%{_datadir}/qtads/i18n/* #no more needed ?
%{_datadir}/applications/mandriva-%{name}.desktop

#--------------------------------------------------------------------

%prep
%setup -q

%build 
%qmake_qt4 \
    BIN_INSTALL=%{buildroot}%{_bindir} \
    DOC_INSTALL=%{buildroot}%{_datadir}/doc \
    DATA_INSTALL=%{buildroot}%{_datadir} \
    CFLAGS="$RPM_OPT_FLAGS" \
    CXXFLAGS="$RPM_OPT_FLAGS"

%make

%install
rm -rf %{buildroot}
#%makeinstall #there is no make install option at the moment, must be done manually
mkdir -p %{buildroot}%{_bindir}
cp qtads  %{buildroot}%{_bindir}/qtads
mkdir -p %{buildroot}%{_mandir}/man6
cp -f %{name}.6 %{buildroot}%{_mandir}/man6

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=GUI multimedia interpreter for TADS games
Exec=%{name}
Icon=other_amusement
Terminal=false
Type=Application
Categories=Game;AdventureGame;RolePlaying;
EOF


%clean
rm -rf %{buildroot}

