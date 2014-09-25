Name:		oma-welcome
Version:	1.0.5
Release:	4
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/panahbiru/oma-welcome
Source0:	http://code.emka.web.id/demo/omv/%{name}/%{name}-%{version}.tar.xz
#Patch0:		oma-welcome-1.0.3-fix-makefile.patch
#Patch1:		oma-welcome-1.0.3-use-by-default-s-c-p.patch
#Patch2:		oma-welcome-1.0.3-fix-desktop-file.patch
#Patch3:		oma-welcome-1.0.3-add-32bit-medias.patch
#Patch4:		oma-welcome-1.0.3-fix-various-software-versions.patch
BuildArch:	noarch
Requires:	python-qt4-webkit
Requires:	python-qt4
Requires:	python-webpy

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
