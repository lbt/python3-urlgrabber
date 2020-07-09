Name:       python3-urlgrabber
Summary:    A high-level cross-protocol url-grabber
Version:    4.1
Release:    1
License:    LGPL v2.1
URL:        http://pyurlgrabber.org/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Provides:       PyURLGRABBER

%description
The rpm urlgrabber module is used by yum 

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%py3_build

%install
rm -rf %{buildroot}
%py3_install

%files
%defattr(-,root,root,-)
%license LICENSE
%doc README examples
%{python3_sitearch}/*
