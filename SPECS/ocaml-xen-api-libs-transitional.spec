%global debug_package %{nil}

Name:           ocaml-xen-api-libs-transitional
Version:        2.25.3
Release:        2%{?dist}
Summary:        Deprecated standard library extension for OCaml
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/xen-api-libs-transitional

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xen-api-libs-transitional/archive?at=v2.25.3&format=tar.gz&prefix=ocaml-xen-api-libs-transitional-2.25.3#/xen-api-libs-transitional-2.25.3.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xen-api-libs-transitional/archive?at=v2.25.3&format=tar.gz&prefix=ocaml-xen-api-libs-transitional-2.25.3#/xen-api-libs-transitional-2.25.3.tar.gz) = a1b06d28038122b299d9d17928ae0d1e1d307b65

BuildRequires:  xs-opam-repo
BuildRequires:  forkexecd-devel
BuildRequires:  xen-devel
BuildRequires:  xen-dom0-libs-devel
BuildRequires:  xen-libs-devel
BuildRequires:  ocaml-xcp-idl-devel
Requires:       xen-libs
Requires:       xen-dom0-libs
Requires:       stunnel >= 5.55

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
A deprecated standard library extension for OCaml.

%package        devel
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xen-api-libs-transitional/archive?at=v2.25.3&format=tar.gz&prefix=ocaml-xen-api-libs-transitional-2.25.3#/xen-api-libs-transitional-2.25.3.tar.gz) = a1b06d28038122b299d9d17928ae0d1e1d307b65
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:  xs-opam-repo
Requires:  forkexecd-devel
Requires:  xen-devel
Requires:  xen-dom0-libs-devel
Requires:  xen-libs-devel
Requires:  ocaml-xcp-idl-devel
Requires:  xen-libs
Requires:  xen-dom0-libs


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir    %{_opamroot}/ocaml-system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc
%global build_ocaml_dir %{buildroot}%{ocaml_dir}
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}
%global build_ocaml_docdir %{buildroot}%{ocaml_docdir}

%prep
%autosetup -p1

%build
make

%check
make test

%install
make install DESTDIR=%{buildroot}

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

%{ocaml_libdir}/zstd
%exclude %{ocaml_libdir}/zstd/*.a
%exclude %{ocaml_libdir}/zstd/*.cmxa
%exclude %{ocaml_libdir}/zstd/*.cmxs
%exclude %{ocaml_libdir}/zstd/*.cmx
%exclude %{ocaml_libdir}/zstd/*.mli

%{ocaml_libdir}/xapi-compression
%exclude %{ocaml_libdir}/xapi-compression/*.a
%exclude %{ocaml_libdir}/xapi-compression/*.cmxa
%exclude %{ocaml_libdir}/xapi-compression/*.cmxs
%exclude %{ocaml_libdir}/xapi-compression/*.cmx
%exclude %{ocaml_libdir}/xapi-compression/*.mli

%{ocaml_libdir}/safe-resources
%exclude %{ocaml_libdir}/safe-resources/*.a
%exclude %{ocaml_libdir}/safe-resources/*.cmxa
%exclude %{ocaml_libdir}/safe-resources/*.cmxs
%exclude %{ocaml_libdir}/safe-resources/*.cmx
%exclude %{ocaml_libdir}/safe-resources/*.mli

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

%{ocaml_libdir}/zstd/*.a
%{ocaml_libdir}/zstd/*.cmxa
%{ocaml_libdir}/zstd/*.cmxs
%{ocaml_libdir}/zstd/*.cmx
%{ocaml_libdir}/zstd/*.mli

%{ocaml_libdir}/xapi-compression/*.a
%{ocaml_libdir}/xapi-compression/*.cmxa
%{ocaml_libdir}/xapi-compression/*.cmxs
%{ocaml_libdir}/xapi-compression/*.cmx
%{ocaml_libdir}/xapi-compression/*.mli

%{ocaml_libdir}/safe-resources/*.a
%{ocaml_libdir}/safe-resources/*.cmxa
%{ocaml_libdir}/safe-resources/*.cmxs
%{ocaml_libdir}/safe-resources/*.cmx
%{ocaml_libdir}/safe-resources/*.mli

%{ocaml_libdir}/xapi-libs-transitional

%changelog
* Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 2.25.3-2
- Bump package after xs-opam update

* Thu Sep 23 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 2.25.3-1
- CA-358583: Fix PROXY metadata to multiple HTTPS requests on a connection

* Fri Jul 16 2021 Ben Anson <ben.anson@citrix.com> - 2.25.2-1
- CP-36872: Backport XSI-989
- Use HTTP/1.1 in 101 response

* Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 2.25.1-2
- bump packages after xs-opam update

* Thu Feb 11 2021 Ben Anson <ben.anson@citrix.com> - 2.25.1-1
- CP-35026 add ability to parse a PROXY header
- CP-35026 add STUNNEL_PROXY additional header
- CA-342856 don't print to stderr, use Debug.error
- fixup! CA-342856 don't print to stderr, use Debug.error

* Mon Jun 01 2020 Christian Lindig <christian.lindig@citrix.com> - 2.25.0-1
- CA-337546: add a xapi_stdext_resources module for safe handling of
	file descriptors
- CA-337546: use Unixfd.t to avoid leaks
- CA-337546: watchdog: replace pipe with scheduler
- CA-337546: convert xapi-compression to use safe pipes
- CA-337546: rename to safe_resources
- CA-337546: print LOC on GC close failure
- CA-337546: use Hashtbl.replace in move_into
- CA-337546: add opam file for new library
- CA-337546: stunnel disconnect: fix Stack overflow
- CA-337546: stunnel: don't loop when wait=false in disconnect
- CA-340493: only call diagnose failure if a logfile exists

* Fri Apr 03 2020 Christian Lindig <christian.lindig@citrix.com> - 2.24.0-1
- CP-32840 drop legacy ssl support
- CP-33058 centralize cipherstrings

* Tue Mar 17 2020 Christian Lindig <christian.lindig@citrix.com> - 2.23.0-1
- CA-336258: http-svr: add JSONRPC_protocol
- Remove sha1 from travis file

* Mon Feb 24 2020 Christian Lindig <christian.lindig@citrix.com> - 2.22.0-1
- CP-27904: nuke sha1 out of orbit

* Wed Feb 12 2020 Christian Lindig <christian.lindig@citrix.com> - 2.21.0-1
- CP-32124: Set fips=yes explicitly
- CP-32124: Add checkHost verify peer hostname against cert
- CP-32124: Check if the CRLpath is an empty directory
- CP-32124: Set the default log facility as 'authpriv'
- CP-32124: Disable TLSv1.3

* Tue Jan 07 2020 Ming Lu <ming.lu@citrix.com> - 2.20.0-2
- CP-32124 Add 'Requires: stunnel >= 5.55' for stunnel update

* Tue Nov 12 2019 Christian Lindig <christian.lindig@citrix.com> - 2.20.0-1
- CA-329836 Improve logging

* Thu Oct 24 2019 Christian Lindig <christian.lindig@citrix.com> - 2.19.0-1
- travis: use xs-opam to set ci env
- opam: add ounit as test dependency

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 2.18.0-2
- bump packages after xs-opam update

* Mon Aug 12 2019 Christian Lindig <christian.lindig@citrix.com> - 2.18.0-1
- Remove debug logging about accepting connection

* Wed Aug 07 2019 Christian Lindig <christian.lindig@citrix.com> - 2.17.0-1
- Mute Dune preprocess warnings
- Use Debian Unstable for Travis
- Fix http-svr.opam: use rpclib
- Travis: use OCAML_VERSION=4.07

* Wed Jun 05 2019 Christian Lindig <christian.lindig@citrix.com> - 2.16.0-1
- maintenance: remove use of xapi-stdext-base64

* Wed Jan 23 2019 Christian Lindig <christian.lindig@citrix.com> - 2.15.0-1
- Prepare for Dune 1.6

* Thu Jan 17 2019 Christian Lindig <christian.lindig@citrix.com> - 2.14.0-1
- Ported last remaining package http-svr to dune.

* Mon Dec 10 2018 Christian Lindig <christian.lindig@citrix.com> - 2.13.0-1
- Add zstd library
- Add xapi-compression library
- Port to Dune

* Thu Nov 01 2018 Christian Lindig <christian.lindig@citrix.com> - 2.12.0-1
- Update opam files for Opam 2, update Travis setup

* Mon Oct 22 2018 Christian Lindig <christian.lindig@citrix.com> - 2.11.0-1
- CP-29687: Remove TLS_RSA_WITH_AES_128_CBC_SHA(AES128-SHA) for CC
- allow_failures cannot be parsed by travis

* Thu Oct 11 2018 Rob Hoes <rob.hoes@citrix.com> - 2.10.0-1
- CP-29196: Enable FIPS mode if existence of cc preparations (#52)
- CP-29696: Change the order of cipher base on latest requirement

* Tue Sep 11 2018 Christian Lindig <christian.lindig@citrix.com> - 2.9.0-1
- CA-296532: mpathalert log spam

* Wed Sep 05 2018 Christian Lindig <christian.lindig@citrix.com> - 2.8.0-1
- CP-29015: Set correct ciphers for stunnel client
- Simplify PPX processing

* Wed Jul 18 2018 Christian Lindig <christian.lindig@citrix.com> - 2.7.0-1
- CA-291012 Added better printing of xml exc

* Thu May 24 2018 Christian Lindig <christian.lindig@citrix.com> - 2.6.0-1
- CA-289145: Close socket if error occurs when connecting
- http-svr: make again safe-string compliant after last PR

* Tue May 01 2018 Christian Lindig <christian.lindig@citrix.com> - 2.5.0-1
- http-svr: reintroduce really_write, whose behaviour has been fixed 
  in xapi-stdext-unix 1.2.0

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

