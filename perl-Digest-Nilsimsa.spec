#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	Nilsimsa
Summary:	Digest::Nilsimsa - Perl version of nilsimsa code
Summary(pl):	Digest::Nilsimsa - werja perlowa kodu nilsimsa
Name:		perl-Digest-Nilsimsa
Version:	0.06
Release:	3
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	08e940bd7f5d1167ef3fd1aa7ce234d7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A nilsimsa signature is a statistic of n-gram occurance in a piece of
text. It is a 256 bit value usually represented in hex. This module is
a wrapper around nilsimsa implementation in C by cmeclax.

%description -l pl
Sygnatura nilsimsa to statystyka wystêpowania n-gramów w danym
tek¶cie. Jest to 256-bitowa liczba, przewa¿nie reprezentowana
szesnastkowo. Modu³ jest nak³adk± na implementacjê w C, której
autorem jest cmeclax.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/%{pdir}/*.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.so
%{perl_vendorarch}/auto/%{pdir}/%{pnam}/*.bs
%{_mandir}/man3/*
