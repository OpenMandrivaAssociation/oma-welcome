Name:		oma-welcome
Version:	2.4.14
Release:	1
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaAssociation/oma-welcome
Source0:	https://github.com/OpenMandrivaSoftware/oma-welcome/archive/%{version}.tar.gz
Requires:	kdialog
Requires:	htmlscript >= 1.0.1
BuildRequires:	make
BuildArch:	noarch

%description
Introduce new users to the OpenMandriva Lx.

%prep
%autosetup -p1

%build
# Nothing to do here...

%install
%make_install

%find_lang om-welcome

%files -f om-welcome.lang
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_bindir}/enable-repo
%{_bindir}/disable-repo
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-welcome.desktop
