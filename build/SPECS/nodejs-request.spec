%{?scl:%scl_package nodejs-request}
%{!?scl:%global pkg_name %{name}}


%{?scl:
%define _use_internal_dependency_generator 0
%define __find_requires %{_rpmconfigdir}/%{scl_prefix}require.sh
%define __find_provides %{_rpmconfigdir}/%{scl_prefix}provide.sh}

Name:       %{?scl_prefix}nodejs-request
Version:    2.16.6
Release:    3%{?dist}
Summary:    Simplified HTTP request client
License:    ASL 2.0
Group:      Development/Libraries
URL:        https://github.com/mikeal/request
Source0:    http://registry.npmjs.org/request/-/request-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Request is designed to be the simplest way possible to make HTTP calls. It
supports HTTPS and follows redirects by default.

You can stream any response to a file stream. You can also stream a file to a
PUT or POST request.  It also supports a few simple server and proxy functions.

%prep
%setup -q -n package

#remove bundled modules
rm -rf node_modules

%nodejs_fixdep hawk '~0.12.1'
%nodejs_fixdep json-stringify-safe 4.x

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/request
cp -pr *.js package.json %{buildroot}%{nodejs_sitelib}/request

%nodejs_symlink_deps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/request
%doc README.md LICENSE

%changelog
* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.16.6-3
- Add support for software collections

* Wed Apr 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-2
- fix versions for newly added dependencies

* Wed Apr 03 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.16.6-1
- new upstream release 2.16.6
- cookie library now unbundled upstream

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.14.0-1
- new upstream release 2.14.0

* Tue Jan 29 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-5
- actually make patch work
- fix typo

* Mon Jan 28 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-4
- actually apply patch
- manually create dependency link to private module tobi-cookie

* Thu Jan 24 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-3
- unbundle cookie stuff

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-2
- add missing build section
- improve description

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.12.0-1
- new upstream release 2.12.0
- clean up for submission

* Wed Apr 18 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.202-1
- New upstream release 2.9.202

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.153-1
- new upstream release 2.9.153

* Sat Feb 25 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.151-1
- new upstream release 2.9.151

* Sat Jan 21 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.9.100-1
- new upstream release 2.9.100

* Thu Dec 22 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.9-1
- new upstream release 2.2.9

* Mon Nov 07 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 2.2.0-1
- new upstream release 2.2.0
- adds node v0.6 support

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-2.20110928.646c80dgit
- npm needs a newer git snapshot (apparently upstream moved to rolling release anyway)

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.2.0-1
- initial package