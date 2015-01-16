Name:		oma-welcome
Version:	1.0.5
Release:	6
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/panahbiru/oma-welcome
Source0:	http://code.emka.web.id/demo/omv/%{name}/%{name}-%{version}.tar.xz
BuildArch:	noarch
Requires:	python2-qt4-webkit
Requires:	python2-qt4-core
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

%files
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-welcome.desktop
%{_localedir}/*/LC_MESSAGES/om-welcome.*o
