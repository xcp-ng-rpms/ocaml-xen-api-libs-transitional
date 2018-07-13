%global debug_package %{nil}

Name:           ocaml-xen-api-libs-transitional
Version:        2.4.0
Release:        1%{?dist}
Summary:        Deprecated standard library extension for OCaml
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/xen-api-libs-transitional
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xen-api-libs-transitional/archive?at=v%{version}&format=tar.gz&prefix=xen-api-libs-transitional-%{version}#/xen-api-libs-transitional-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xen-api-libs-transitional/archive?at=v2.4.0&format=tar.gz&prefix=xen-api-libs-transitional-2.4.0#/xen-api-libs-transitional-2.4.0.tar.gz) = 13b952f7b871597e906f5ece839c5ad79501b95a
BuildRequires:  xs-opam-repo
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-camlp4-devel
BuildRequires:  xen-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-libs-devel
BuildRequires:  ocaml-xcp-idl-devel
Requires:       xen-libs
Requires:       xen-dom0-libs

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
A deprecated standard library extension for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:  xs-opam-repo
Requires:  forkexecd-devel
Requires:  ocaml-camlp4-devel
Requires:  xen-devel
Requires:  xen-dom0-libs-devel
Requires:  xen-libs-devel
Requires:  ocaml-xcp-idl-devel
Requires:  xen-libs
Requires:  xen-dom0-libs


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir    /usr/lib/opamroot/system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc
%global build_ocaml_dir %{buildroot}%{ocaml_dir}
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}
%global build_ocaml_docdir %{buildroot}%{ocaml_docdir}

%prep
%autosetup -p1 -n xen-api-libs-transitional-%{version}

%build
make

%install
mkdir -p %{build_ocaml_libdir}
mkdir -p %{build_ocaml_docdir}
make install OPAM_PREFIX=%{build_ocaml_dir} OPAM_LIBDIR=%{build_ocaml_libdir}

# this is to make opam happy
mkdir -p %{build_ocaml_libdir}/xapi-libs-transitional
touch %{build_ocaml_libdir}/xapi-libs-transitional/opam.config

%files
%doc ChangeLog
%doc LICENSE
%doc README.md
%exclude  %{ocaml_docdir}

%{ocaml_libdir}/gzip
%exclude %{ocaml_libdir}/gzip/*.a
%exclude %{ocaml_libdir}/gzip/*.cmxa
%exclude %{ocaml_libdir}/gzip/*.cmxs
%exclude %{ocaml_libdir}/gzip/*.cmx
%exclude %{ocaml_libdir}/gzip/*.mli

%{ocaml_libdir}/http-svr
%exclude %{ocaml_libdir}/http-svr/*.a
%exclude %{ocaml_libdir}/http-svr/*.cmxa
%exclude %{ocaml_libdir}/http-svr/*.cmxs
%exclude %{ocaml_libdir}/http-svr/*.cmx
%exclude %{ocaml_libdir}/http-svr/*.mli

%{ocaml_libdir}/pciutil
%exclude %{ocaml_libdir}/pciutil/*.a
%exclude %{ocaml_libdir}/pciutil/*.cmxa
%exclude %{ocaml_libdir}/pciutil/*.cmxs
%exclude %{ocaml_libdir}/pciutil/*.cmx
%exclude %{ocaml_libdir}/pciutil/*.mli

%{ocaml_libdir}/sexpr
%exclude %{ocaml_libdir}/sexpr/*.a
%exclude %{ocaml_libdir}/sexpr/*.cmxa
%exclude %{ocaml_libdir}/sexpr/*.cmxs
%exclude %{ocaml_libdir}/sexpr/*.cmx
%exclude %{ocaml_libdir}/sexpr/*.mli

%{ocaml_libdir}/sha1
%exclude %{ocaml_libdir}/sha1/*.a
%exclude %{ocaml_libdir}/sha1/*.cmxa
%exclude %{ocaml_libdir}/sha1/*.cmxs
%exclude %{ocaml_libdir}/sha1/*.cmx
%exclude %{ocaml_libdir}/sha1/*.mli

%{ocaml_libdir}/stunnel
%exclude %{ocaml_libdir}/stunnel/*.a
%exclude %{ocaml_libdir}/stunnel/*.cmxa
%exclude %{ocaml_libdir}/stunnel/*.cmxs
%exclude %{ocaml_libdir}/stunnel/*.cmx
%exclude %{ocaml_libdir}/stunnel/*.mli

%{ocaml_libdir}/uuid
%exclude %{ocaml_libdir}/uuid/*.a
%exclude %{ocaml_libdir}/uuid/*.cmxa
%exclude %{ocaml_libdir}/uuid/*.cmxs
%exclude %{ocaml_libdir}/uuid/*.cmx
%exclude %{ocaml_libdir}/uuid/*.mli

%{ocaml_libdir}/xenctrlext
%exclude %{ocaml_libdir}/xenctrlext/*.a
%exclude %{ocaml_libdir}/xenctrlext/*.cmxa
%exclude %{ocaml_libdir}/xenctrlext/*.cmxs
%exclude %{ocaml_libdir}/xenctrlext/*.cmx
%exclude %{ocaml_libdir}/xenctrlext/*.mli
%{ocaml_libdir}/stublibs/dllxenctrlext_stubs.so

%{ocaml_libdir}/xml-light2
%exclude %{ocaml_libdir}/xml-light2/*.a
%exclude %{ocaml_libdir}/xml-light2/*.cmxa
%exclude %{ocaml_libdir}/xml-light2/*.cmxs
%exclude %{ocaml_libdir}/xml-light2/*.cmx
%exclude %{ocaml_libdir}/xml-light2/*.mli


%files devel
%{ocaml_libdir}/gzip/*.a
%{ocaml_libdir}/gzip/*.cmxa
%{ocaml_libdir}/gzip/*.cmxs
%{ocaml_libdir}/gzip/*.cmx
%{ocaml_libdir}/gzip/*.mli

%{ocaml_libdir}/http-svr/*.a
%{ocaml_libdir}/http-svr/*.cmxa
%{ocaml_libdir}/http-svr/*.cmxs
%{ocaml_libdir}/http-svr/*.cmx
%{ocaml_libdir}/http-svr/*.mli

%{ocaml_libdir}/pciutil/*.a
%{ocaml_libdir}/pciutil/*.cmxa
%{ocaml_libdir}/pciutil/*.cmxs
%{ocaml_libdir}/pciutil/*.cmx
%{ocaml_libdir}/pciutil/*.mli

%{ocaml_libdir}/sexpr/*.a
%{ocaml_libdir}/sexpr/*.cmxa
%{ocaml_libdir}/sexpr/*.cmxs
%{ocaml_libdir}/sexpr/*.cmx
%{ocaml_libdir}/sexpr/*.mli

%{ocaml_libdir}/sha1/*.a
%{ocaml_libdir}/sha1/*.cmxa
%{ocaml_libdir}/sha1/*.cmxs
%{ocaml_libdir}/sha1/*.cmx
%{ocaml_libdir}/sha1/*.mli

%{ocaml_libdir}/stunnel/*.a
%{ocaml_libdir}/stunnel/*.cmxa
%{ocaml_libdir}/stunnel/*.cmxs
%{ocaml_libdir}/stunnel/*.cmx
%{ocaml_libdir}/stunnel/*.mli

%{ocaml_libdir}/uuid/*.a
%{ocaml_libdir}/uuid/*.cmxa
%{ocaml_libdir}/uuid/*.cmxs
%{ocaml_libdir}/uuid/*.cmx
%{ocaml_libdir}/uuid/*.mli

%{ocaml_libdir}/xenctrlext/*.a
%{ocaml_libdir}/xenctrlext/*.cmxa
%{ocaml_libdir}/xenctrlext/*.cmxs
%{ocaml_libdir}/xenctrlext/*.cmx
%{ocaml_libdir}/xenctrlext/*.mli

%{ocaml_libdir}/xml-light2/*.a
%{ocaml_libdir}/xml-light2/*.cmxa
%{ocaml_libdir}/xml-light2/*.cmxs
%{ocaml_libdir}/xml-light2/*.cmx
%{ocaml_libdir}/xml-light2/*.mli

%{ocaml_libdir}/xapi-libs-transitional

%changelog
* Mon Apr 09 2018 Christian Lindig <christian.lindig@citrix.com> - 2.4.0-1
- CA-285840: Make sure stunnel doesn't hang talking to dead hosts

* Wed Mar 21 2018 Christian Lindig <christian.lindig@citrix.com> - 2.3.0-1
- make code compatible with safe-string compiler flag

* Fri Feb 23 2018 Christian Lindig <christian.lindig@citrix.com> - 2.2.0-1
- xapi-libs-transitional: run all tests
- CP-26298: Increase the max_stunnel in xapi

* Thu Jan 11 2018 Marcello Seri <marcello.seri@citrix.com> - 2.1.0-1
- Port to jbuilder and dependencies cleanup

* Fri Dec 01 2017 Marcello Seri <marcello.seri@citrix.com> - 2.0.0-1
- Remove xenstore-compat
- http-svr: add 500 Internal Server Error HTTP status code

* Mon Mar 20 2017 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.1-1
- CA-245559: Bugfix for http_svr handling pipelined requests
- Fix dependencies in uuid

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.0-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Thu Jun 23 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.0-1
- Stable release

* Tue Apr 26 2016 Euan Harris <euan.harris@citrix.com> - 0.9.10-1 
- Add support for configuring stunnel's cipher suites

* Fri Dec 11 2015 Euan Harris <euan.harris@citrix.com> - 0.9.9-1 
- Remove cpuid
- Remove xen-utils

* Mon Jun 29 2015 Thomas Sanders <thomas.sanders@citrix.com> - 0.9.8-1
- Stunnel uses a new and switchable config for outgoing connections.
- Removed Oasis autogenerated files (create them in build).
- Added opam and travis support.

* Thu Sep 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.6-2
- Remove xen-missing-headers dependency

* Wed Jun 4 2014 Jon Ludlam <jonathan.ludlam@citrix.com> - 0.9.6-1
- Update to 0.9.6 release

* Mon Jun 2 2014 Euan Harris <euan.harris@citrix.com> - 0.9.3-2
- Split files correctly between base and devel packages

* Wed Sep 25 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.3-1
- Update to 0.9.3

* Tue Sep 10 2013 David Scott <dave.scott@eu.citrix.com>
- Update to 0.9.2

* Wed Jun  5 2013 David Scott <dave.scott@eu.citrix.com>
- Initial package

