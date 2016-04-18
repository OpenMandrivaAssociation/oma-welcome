Name:		oma-welcome
Version:	1.2.0.3
Release:	1
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/cris-b/oma-welcome
Source0:	%{name}-%{version}.tar.xz
# still needs python2 as web.py has not been ported to python3
Patch0:         oma-welcome-1.0.5-use-py2.patch
BuildArch:	noarch
Requires:	kdialog
Requires:	python2-qt5-gui
Requires:	python2-qt5-network
Requires:	python2-qt5-webenginewidgets
Requires:	python2-qt5-core
Requires:	python2-qt5-widgets
Requires:	python2-qt5-printsupport
Requires:	python2-webpy
Requires:	python2-sip
Requires:	python2-cherrypy

%description
Introduce new users to the OpenMandriva Lx.

%prep
%setup -q
%apply_patches

%build
#nothing to do

%install
%makeinstall_std

%find_lang om-welcome

%files -f om-welcome.lang
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-welcome.desktop
