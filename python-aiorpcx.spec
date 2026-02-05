%define module aiorpcx

Name:		python-aiorpcx
Version:	0.25.0
Release:	1
Summary:	Generic async RPC implementation
License:	MIT
URL:	https://github.com/kyuupichan/aiorpcX
Source0:	https://github.com/kyuupichan/aiorpcX/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# Optional dependency
BuildRequires:	python%{pyver}dist(websockets)

# Replace python3 named package
%rename python3-aiorpcx

%description
Transport, protocol and framing-independent async RPC client\
and server implementation.

%files
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info
