Name:		oma-welcome
Version:	0.8.0
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

%install
/bin/mkdir -p %{buildroot}
/bin/cp -axv %{buildroot}/%{name}-%{version}/* %{buildroot}/


%files
%{_sysconfdir}/skel/om-welcome.desktop
%{_bindir}/om-welcome
%{_datadir}/%{name}/*
%{_datadir}/locale/*
