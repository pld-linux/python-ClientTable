%define 	module ClientTable

Summary:	Python package providing a module for parsing HTML tables
Summary(pl):	Pakiet zawieraj±cy modu³ do przetwarzania tabelek HTML
Name:		python-%{module}
Version:	0.0.1a
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://wwwsearch.sourceforge.net/%{module}/src/%{module}-%{version}.tar.gz
# Source0-md5:	b69bb8aa2ab04ba8fe5e22ebade62191
URL:		http://wwwsearch.sourceforge.net/ClientTable/
Requires:       python-modules >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClientTable is a Python module for generic HTML table parsing. It is
most useful when used in conjunction with other parsers (htmllib or
HTMLParser, regular expressions, etc.), to divide up the parsing work
between your own code and ClientTable.

%description -l pl
ClientTable to modu³ Pythona do przetwarzania tabelek HTML. Najlepiej
sprawdza siê w po³±czeniu z innymi narzêdziami (jak htmllib lub
HTMLParser, wyra¿enia regularne itp.).

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm $RPM_BUILD_ROOT/%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{py_sitescriptdir}/*.py[co]

%doc ChangeLog COPYING README.html README.txt
