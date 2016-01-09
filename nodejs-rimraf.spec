#
# Conditional build:
%bcond_without	tests		# build without tests

%define		pkg	rimraf
Summary:	A deep deletion module for node.js
Name:		nodejs-%{pkg}
Version:	2.2.8
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	dcae224924ec7cbcb4844f8ba0cfea2d
URL:		https://github.com/isaacs/rimraf
%if %{with tests}
BuildRequires:	bash
BuildRequires:	nodejs
%endif
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A deep deletion module for node.js (like "rm -rf").

%prep
%setup -qc
mv package/* .

%build
%if %{with tests}
cd test
bash run.sh
%endif

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%{nodejs_libdir}/%{pkg}
