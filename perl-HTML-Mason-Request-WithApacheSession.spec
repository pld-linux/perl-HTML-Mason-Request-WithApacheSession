%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Mason-Request-WithApacheSession
Summary:	Add a session to the Mason Request object
Summary(pl):	Dodanie sesji do obiektu Mason::Request
Name:		perl-HTML-Mason-Request-WithApacheSession
Version:	0.05
Release:	2
License:	GPL/Artistic
URL:		http://www.masonhq.com/
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRequires:	perl-Apache-Session
BuildRequires:	perl-HTML-Mason
BuildRequires:	perl-Params-Validate
BuildRequires:	perl-libapreq
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
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/HTML/Mason/Request
%{_mandir}/man3/*
