Name:		oma-welcome
Version:	1.0.2
Release:	1
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/panahbiru/oma-welcome
Source0:	http://code.emka.web.id/demo/omv/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	python-qt4-webkit
Requires:	python-qt4
Requires:	python-webpy

%description
Introduce new users to the OpenMandriva Lx.

%prep
%setup -c -n %{name}-%{version}

%build
#nothing to do

%install
mkdir -p  %{buildroot}
cp -axv ${RPM_BUILD_DIR}/%{name}-%{version}/* %{buildroot}/
mkdir -p %{buildroot}/%{_sysconfdir}/xdg/autostart
cp om-welcome.desktop %{buildroot}/%{_sysconfdir}/xdg/autostart
rm -f %{buildroot}//om-welcome.desktop
# desktop menu entry
mkdir -p %{buildroot}/%{_datadir}/applications
cp ./%{_sysconfdir}/skel/om-welcome.desktop %{buildroot}/%{_datadir}/applications


%files
%{_sysconfdir}/skel/om-welcome.desktop
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_datadir}/applications/om-welcome.desktop
%{_localedir}/*/LC_MESSAGES/om-welcome.po
%{_localedir}/*/LC_MESSAGES/om-welcome.mo
