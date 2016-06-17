Name:		oma-welcome
Version:	2.0
Release:	1
Summary:	OpenMandriva Lx Welcome Page
License:	GPLv2
Group:		System/Configuration/Other
URL:		https://github.com/OpenMandrivaAssociation/oma-welcome
Source0:	%{name}-%{version}.tar.xz
Requires:	kdialog
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5WebEngineWidgets)

%description
Introduce new users to the OpenMandriva Lx.

%prep
%setup -q
%apply_patches

%build
cd launcher
CXXFLAGS="%{optflags}" LDFLAGS="%{optflags}" cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -G Ninja
ninja

%install
%makeinstall_std

%find_lang om-welcome

%files -f om-welcome.lang
%{_sysconfdir}/xdg/autostart/om-welcome.desktop
%{_bindir}/om-welcome
%{_bindir}/om-welcome-launcher
%{_datadir}/%{name}/*
%{_datadir}/applications/om-welcome.desktop
