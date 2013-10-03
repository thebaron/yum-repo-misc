%{?scl:%scl_package nodejs-combined-stream}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:           %{?scl_prefix}nodejs-combined-stream
Version:        0.0.4
Release:        2%{?dist}
Summary:        A stream that emits multiple other streams one after another
BuildArch:      noarch

Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/felixge/node-combined-stream
Source0:        http://registry.npmjs.org/combined-stream/-/combined-stream-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
A stream that emits multiple other streams one after another.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{nodejs_sitelib}/combined-stream
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/combined-stream

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/combined-stream
%doc License Readme.md

%changelog
* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.4-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- new upstream release 0.0.4

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.3-1
- initial package generated by npm2rpm