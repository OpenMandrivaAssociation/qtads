%define name    qtads
%define version 2.1.2
%define release 2

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



%changelog
* Sun Mar 04 2012 Samuel Verschelde <stormi@mandriva.org> 2.1.2-1mdv2011.0
+ Revision: 782098
- update to new version 2.1.2

* Fri Mar 11 2011 Samuel Verschelde <stormi@mandriva.org> 2.1.1-1
+ Revision: 643807
- version 2.1.1

* Sun Oct 24 2010 Samuel Verschelde <stormi@mandriva.org> 2.0.1-3mdv2011.0
+ Revision: 589203
- suggests timidity-instruments for MIDI playback

* Sun Oct 24 2010 Samuel Verschelde <stormi@mandriva.org> 2.0.1-2mdv2011.0
+ Revision: 588939
- bump release
- do not gzip man page

* Sun Oct 24 2010 Samuel Verschelde <stormi@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 588683
- new version 2.0.1, uses QT4 now, and becomes multimedia (images/sounds/music)

* Sat Jul 11 2009 Samuel Verschelde <stormi@mandriva.org> 1.9-2mdv2010.0
+ Revision: 394361
+ rebuild (emptylog)

* Sat Jul 11 2009 Samuel Verschelde <stormi@mandriva.org> 1.9-1mdv2010.0
+ Revision: 394352
- update to new version 1.9

* Sat May 30 2009 Samuel Verschelde <stormi@mandriva.org> 1.8-2mdv2010.0
+ Revision: 381529
- added desktop file
- modified summary

* Fri May 29 2009 Samuel Verschelde <stormi@mandriva.org> 1.8-1mdv2010.0
+ Revision: 381141
- new version 1.8

* Thu May 21 2009 Samuel Verschelde <stormi@mandriva.org> 1.7-2mdv2010.0
+ Revision: 378341
- rebuild for gcc 4.4

* Tue Mar 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.7-1mdv2009.1
+ Revision: 356597
- import qtads


* Mon Mar 31 2008 Samuel Verschelde <specialspam@laposte.net> 1.7-1mdv2008.1
- first package 
