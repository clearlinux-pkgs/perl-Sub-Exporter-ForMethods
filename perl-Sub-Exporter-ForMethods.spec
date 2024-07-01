#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v2
# autospec commit: e661f3a625d7
#
Name     : perl-Sub-Exporter-ForMethods
Version  : 0.100055
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-ForMethods-0.100055.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-ForMethods-0.100055.tar.gz
Summary  : 'helper routines for using Sub::Exporter to build methods'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sub-Exporter-ForMethods-license = %{version}-%{release}
Requires: perl-Sub-Exporter-ForMethods-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(namespace::autoclean)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Sub-Exporter-ForMethods,
version 0.100055:

%package dev
Summary: dev components for the perl-Sub-Exporter-ForMethods package.
Group: Development
Provides: perl-Sub-Exporter-ForMethods-devel = %{version}-%{release}
Requires: perl-Sub-Exporter-ForMethods = %{version}-%{release}

%description dev
dev components for the perl-Sub-Exporter-ForMethods package.


%package license
Summary: license components for the perl-Sub-Exporter-ForMethods package.
Group: Default

%description license
license components for the perl-Sub-Exporter-ForMethods package.


%package perl
Summary: perl components for the perl-Sub-Exporter-ForMethods package.
Group: Default
Requires: perl-Sub-Exporter-ForMethods = %{version}-%{release}

%description perl
perl components for the perl-Sub-Exporter-ForMethods package.


%prep
%setup -q -n Sub-Exporter-ForMethods-0.100055
cd %{_builddir}/Sub-Exporter-ForMethods-0.100055

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sub-Exporter-ForMethods
cp %{_builddir}/Sub-Exporter-ForMethods-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Sub-Exporter-ForMethods/3e73778dd67b448bcec87b917e2e0cd2d13fbe9d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sub::Exporter::ForMethods.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sub-Exporter-ForMethods/3e73778dd67b448bcec87b917e2e0cd2d13fbe9d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
