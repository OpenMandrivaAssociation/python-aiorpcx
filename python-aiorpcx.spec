%global pypi_name aiorpcX
%global srcname aiorpcx
%global _description \
Transport, protocol and framing-independent async RPC client\
and server implementation.

Name:           python-%{srcname}
Version:        0.18.4
Release:        5%{?dist}1
Summary:        Generic async RPC implementation

# https://github.com/kyuupichan/aiorpcX/issues/11
# aiorpcx/curio.py is BSD, rest is MIT
License:        MIT and BSD
URL:            https://pypi.org/project/aiorpcX/
Source0:	https://files.pythonhosted.org/packages/62/90/0c181e61238d2ab58679f34f351fee98c965716884ccd9f84fedc7d3d0e1/aiorpcX-0.18.4.tar.gz

BuildArch:      noarch

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/
