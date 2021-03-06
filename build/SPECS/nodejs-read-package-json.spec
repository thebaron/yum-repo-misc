%{?scl:%scl_package nodejs-read-package-json}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:           %{?scl_prefix}nodejs-read-package-json
Version:        0.3.0
Release:        4%{?dist}
Summary:        npm's package.json parser
BuildArch:      noarch

Group:          System Environment/Libraries
License:        BSD
URL:            https://github.com/isaacs/read-package-json
Source0:        http://registry.npmjs.org/read-package-json/-/read-package-json-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

Patch1: 	Fix-error-meassage-for-missing-README.md.patch	
%description
The thing npm uses to read package.json files, with semantics, defaults and
validation.

%prep
%setup -q -n package
%patch1 -p1
%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/read-package-json
cp -pr package.json read-json.js %{buildroot}%{nodejs_sitelib}/read-package-json

%nodejs_symlink_deps

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/read-package-json
%doc LICENSE README.md

%changelog
* Thu Jun 20 2013 Tomas Hrcka <thrcka@redhat.com> - 0.3.0-4
- added patch to fix RHBZ#965469 

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.0-3
- Add support for software collections

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-2
- drop outdated dependency fix

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-1
- new upstream release 0.3.0

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.2-1
- new upstream release 0.2.2

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- new upstream release 0.2.0

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.13-1
- new upstream release 0.1.13

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.12-1
- initial package generated by npm2rpm
