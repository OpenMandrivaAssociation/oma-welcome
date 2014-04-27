Name:		oma-welcome
Version:	1.0.3
Release:	4
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/panahbiru/oma-welcome
Source0:	http://code.emka.web.id/demo/omv/%{name}/%{name}-%{version}.tar.xz
BuildArch:	noarch
Requires:	python-qt4-webkit
Requires:	python-qt4
Requires:	python-webpy

%description
Introduce new users to the OpenMandriva Lx.

%prep
%setup -q

%build
#nothing to do

%install
mkdir -p %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_localedir}

cp -avx usr/bin/* %{buildroot}%{_bindir}
cp -avx om-welcome.desktop %{buildroot}%{_sysconfdir}/xdg/autostart
cp -avx om-welcome.desktop %{buildroot}%{_datadir}/applications
cp -avx usr/share/oma-welcome %{buildroot}%{_datadir}
for i in en fr id it pt_BR tr; do
mkdir -p %{buildroot}%{_localedir}/$i/LC_MESSAGES
cp -avx locale/$i/* %{buildroot}%{_localedir}/$i/LC_MESSAGES ;
done

%files
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-welcome.desktop
%{_localedir}/*/LC_MESSAGES/om-welcome.*o
