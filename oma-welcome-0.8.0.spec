Name: oma-welcome
Version: 0.8.0
Release: 1
Summary: OpenMandriva Lx Welcome Page
License: GPLv2
Group: System/Configuration/Other
Source0: http://code.emka.web.id/demo/omv/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python-qt4-webkit
Requires: python-qt4
Requires: python-webpy
URL: https://github.com/panahbiru/oma-welcome

%description
Introduce new users to the OpenMandriva

%prep

%setup -c -n %{name}-%{version}

%build

%install
[ -d ${RPM_BUILD_ROOT} ] && rm -rf ${RPM_BUILD_ROOT}
/bin/mkdir -p ${RPM_BUILD_ROOT}
/bin/cp -axv ${RPM_BUILD_DIR}/%{name}-%{version}/* ${RPM_BUILD_ROOT}/


%files
%defattr(-,root,root)
%{_sysconfdir}/skel/om-welcome.desktop
%{_bindir}/om-welcome
%{_datadir}/%{name}/*
%{_datadir}/locale/*
