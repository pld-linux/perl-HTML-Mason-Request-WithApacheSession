#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Mason-Request-WithApacheSession
Summary:	HTML::Mason::Request::WithApacheSession - add a session to the Mason Request object
Summary(pl):	HTML::Mason::Request::WithApacheSession - dodanie sesji do obiektu Mason::Request
Name:		perl-HTML-Mason-Request-WithApacheSession
Version:	0.07
Release:	3
# same as perl
License:	GPL v1+ or Artistic
URL:		http://www.masonhq.com/
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	adcf211e6f5bfac48714a4d490c7ec1b
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Apache-Session >= 1.54
BuildRequires:	perl-HTML-Mason >= 1.12
# for proper dependency resolving:
BuildRequires:	perl-libapreq
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/HTML/Mason/Request
%{_mandir}/man3/*
