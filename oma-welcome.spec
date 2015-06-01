Name:		oma-welcome
Version:	1.0.5.2
Release:	1
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/cris-b/oma-welcome
#  git archive --format=tar --prefix=oma-welcome-%{version}/ master | xz >oma-welcome-%{version}.tar.xz
Source0:	%{name}-%{version}.tar.xz
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
