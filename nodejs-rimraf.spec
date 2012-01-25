#
# Conditional build:
%bcond_without	tests		# build without tests

%define		git_hash 5022381
%define		pkg	rimraf
Summary:	A deep deletion module for node.js
Name:		nodejs-%{pkg}
Version:	1.0.9
Release:	2
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/%{pkg}
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	230542bf0c1b317b460e66f5e55a6409
BuildRequires:	bash
BuildRequires:	nodejs
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
cp -p %{pkg}.js fiber.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%{nodejs_libdir}/%{pkg}
