#
# Conditional build:
%bcond_with	tests	# do perform tests (broken in 4.2.15)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	isort
Summary:	Python utility / library to sort imports alphabetically
Name:		python-%{module}
Version:	4.2.15
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/i/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	34915a2ce60e6fe3dbcbf5982deef9b4
URL:		https://github.com/timothycrosley/isort
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
isort is a Python utility / library to sort imports alphabetically,
and automatically separated into sections. It provides a command line
utility, Python library and plugins for various editors to quickly
sort all your imports. It currently cleanly supports Python 2.7 - 3.6
without any dependencies.

%package -n python3-%{module}
Summary:	Python utility / library to sort imports alphabetically
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
isort is a Python utility / library to sort imports alphabetically,
and automatically separated into sections. It provides a command line
utility, Python library and plugins for various editors to quickly
sort all your imports. It currently cleanly supports Python 2.7 - 3.6
without any dependencies.

%package -n isort
Summary:	Python utility / library to sort imports alphabetically
Group:		Development/Tools
%if %{with python3}
Requires:	python3-%{module} = %{version}-%{release}
%else
Requires:	python-%{module} = %{version}-%{release}
%endif

%description -n isort
isort is a Python utility / library to sort imports alphabetically,
and automatically separated into sections. It provides a command line
utility, Python library and plugins for various editors to quickly
sort all your imports. It currently cleanly supports Python 2.7 - 3.6
without any dependencies.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS.md CHANGELOG.md README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS.md CHANGELOG.md README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%files -n isort
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isort
