#
# Conditional build:
%bcond_with	tests	# unit tests (needs more dependencies in PLD)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	isort
Summary:	Python 2 library to sort imports alphabetically
Summary(pl.UTF-8):	Narzędzie Pythona 2 do alfabetycznego sortowania listy importów
Name:		python-%{module}
Version:	4.3.21
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/isort/
Source0:	https://files.pythonhosted.org/packages/source/i/isort/%{module}-%{version}.tar.gz
# Source0-md5:	05d66f2eb7ce2c2d702e86bac24bf9e4
URL:		https://github.com/timothycrosley/isort
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-backports.functools_lru_cache
BuildRequires:	python-futures
BuildRequires:	python-pip-api
BuildRequires:	python-pipreqs
BuildRequires:	python-pytest
BuildRequires:	python-requirementslib
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pip-api
BuildRequires:	python3-pipreqs
BuildRequires:	python3-pytest
BuildRequires:	python3-requirementslib
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
isort is a Python utility / library to sort imports alphabetically,
and automatically separated into sections. It provides a command line
utility, Python library and plugins for various editors to quickly
sort all your imports. It currently cleanly supports Python 2.7 and
3.4+ without any dependencies.

This package contains Python 2 library.

%description -l pl.UTF-8
isort to pythonowe narzędzie/biblioteka do alfabetycznego sortowania
importów i automatycznego dzielenia ich na sekcje. Udostępnia
narzędzie wiersza poleceń, bibliotekę Pythona i wtyczki do różnych
edytorów, pozwalające szybko posortować importy. Obecnie obsługuje
czysto wersje Pythona 2.7 i 3.4+ bez zewnętrznych zależności.

Ten pakiet zawiera bibliotekę Pythona 2.

%package -n python3-%{module}
Summary:	Python 3 library to sort imports alphabetically
Summary(pl.UTF-8):	Biblioteka Pythona 3 do alfabetycznego sortowania listy importów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
isort is a Python utility / library to sort imports alphabetically,
and automatically separated into sections. It provides a command line
utility, Python library and plugins for various editors to quickly
sort all your imports. It currently cleanly supports Python 2.7 and
3.4+ without any dependencies.

This package contains Python 3 library.

%description -n python3-%{module} -l pl.UTF-8
isort to pythonowe narzędzie/biblioteka do alfabetycznego sortowania
importów i automatycznego dzielenia ich na sekcje. Udostępnia
narzędzie wiersza poleceń, bibliotekę Pythona i wtyczki do różnych
edytorów, pozwalające szybko posortować importy. Obecnie obsługuje
czysto wersje Pythona 2.7 i 3.4+ bez zewnętrznych zależności.

Ten pakiet zawiera bibliotekę Pythona 3.

%package -n isort
Summary:	Python utility to sort imports alphabetically
Summary(pl.UTF-8):	Pythonowe narzędzie do alfabetycznego sortowania listy importów
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
sort all your imports. It currently cleanly supports Python 2.7 and
3.4+ without any dependencies.

This package contains command line utility.

%description -n isort -l pl.UTF-8
isort to pythonowe narzędzie/biblioteka do alfabetycznego sortowania
importów i automatycznego dzielenia ich na sekcje. Udostępnia
narzędzie wiersza poleceń, bibliotekę Pythona i wtyczki do różnych
edytorów, pozwalające szybko posortować importy. Obecnie obsługuje
czysto wersje Pythona 2.7 i 3.4+ bez zewnętrznych zależności.

Ten pakiet zawiera narzędzie wiersza poleceń.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest test_isort.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest test_isort.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

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
%doc ACKNOWLEDGEMENTS.md CHANGELOG.md LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc ACKNOWLEDGEMENTS.md CHANGELOG.md LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%files -n isort
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isort
