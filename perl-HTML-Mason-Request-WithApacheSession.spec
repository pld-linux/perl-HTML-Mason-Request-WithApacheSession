#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Mason-Request-WithApacheSession
Summary:	Add a session to the Mason Request object
Summary(pl):	Dodanie sesji do obiektu Mason::Request
Name:		perl-HTML-Mason-Request-WithApacheSession
Version:	0.07
Release:	1
License:	GPL/Artistic
URL:		http://www.masonhq.com/
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Apache-Session >= 1.54
BuildRequires:	perl-HTML-Mason >= 1.12
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module integrates "Apache::Session" into Mason by adding methods
to the Mason Request object available in all Mason components.

%description -l pl
Ten modu³ integruje Apache::Session w Masona poprzez dodanie metod do
obiektu Request, dostêpnego we wszystkich komponentach Masona.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/HTML/Mason/Request
%{_mandir}/man3/*
