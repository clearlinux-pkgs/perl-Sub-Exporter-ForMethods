#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Sub-Exporter-ForMethods
Version  : 0.100052
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-ForMethods-0.100052.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-ForMethods-0.100052.tar.gz
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
BuildRequires : perl(Sub::Name)
BuildRequires : perl(namespace::autoclean)

%description
This archive contains the distribution Sub-Exporter-ForMethods,
version 0.100052:

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
%setup -q -n Sub-Exporter-ForMethods-0.100052
cd %{_builddir}/Sub-Exporter-ForMethods-0.100052

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
cp %{_builddir}/Sub-Exporter-ForMethods-0.100052/LICENSE %{buildroot}/usr/share/package-licenses/perl-Sub-Exporter-ForMethods/cf95e5660adc2b1a96d7bc21aeb14979f8b21ddf
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
/usr/share/package-licenses/perl-Sub-Exporter-ForMethods/cf95e5660adc2b1a96d7bc21aeb14979f8b21ddf

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.1/Sub/Exporter/ForMethods.pm
