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
# Avoid pulling in python2
sed -Ei 's_#! ?/usr/bin/python_#!/usr/bin/python3_' scripts/*

%py3_build

%install
rm -rf %{buildroot}
%py3_install
# Suse uses /usr/lib as _libexecdir
mv %{buildroot}/usr/libexec/* %{buildroot}%{_libexecdir}/



%files
%defattr(-,root,root,-)
%license LICENSE
%doc README
%doc /usr/share/doc/urlgrabber-4.1.0
%{python3_sitelib}/*
%{_libexecdir}/*
%{_bindir}/urlgrabber
