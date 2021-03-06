%{?scl:%scl_package nodejs-archy}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-archy
Version:    0.0.2
Release:    7%{?dist}
Summary:    Renders nested hierarchies with unicode pipes
License:    MIT
Group:      System Environment/Libraries
URL:        https://github.com/substack/node-archy
Source0:    http://registry.npmjs.org/archy/-/archy-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Render nested hierarchies with unicode pipes, `npm ls` style.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/archy
cp -p index.js package.json %{buildroot}%{nodejs_sitelib}/archy

%nodejs_symlink_deps

# tests disabled until tap is packaged
#%%check
#%%tap test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/archy
%doc README.markdown examples

%changelog
* Thu Apr 11 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.0.2-7
- Add support for software collections

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-5
- fix URL

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-4
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-3
- clean up for submission

* Fri Apr 27 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-2
- fix BuildRequires not present on <F17

* Thu Mar 29 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.2-1
- initial package