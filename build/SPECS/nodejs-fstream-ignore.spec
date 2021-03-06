%{?scl:%scl_package nodejs-fstream-ignore}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-fstream-ignore
Version:    0.0.6
Release:    3%{?dist}
Summary:    A file stream object that can ignore files by globs
# a copy of the BSD license will be included in the next upstream release
# https://github.com/isaacs/fstream-ignore/commit/f5b9b1d981ff98ce1c92d4eac2b1aa91a142e421
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/fstream-ignore
Source0:    http://registry.npmjs.org/fstream-ignore/-/fstream-ignore-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/fstream-ignore
cp -pr ignore.js package.json %{buildroot}%{nodejs_sitelib}/fstream-ignore

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/fstream-ignore
%doc README.md example LICENSE

%changelog
* Wed May 22 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.6-3
- Add LICENSE file to the package

* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.6-2
- Add support for software collections

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-1
- new upstream release 0.0.6

* Tue Jan 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-4
- fix License tag

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-3
- add missing build section
- write better summary

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-2
- clean up for submission

* Wed Mar 28 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-1
- initial package
