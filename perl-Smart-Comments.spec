%define module	Smart-Comments
%define name	perl-%{module}
%define version 1.0.3
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Comments that do more than just sit there
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/%{module}-v%{version}.tar.gz
BuildRequires:	perl-version
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Smart comments provide an easy way to insert debugging and tracking code into a
program. They can report the value of a variable, track the progress of a loop,
and verify that particular assertions are true.

%prep
%setup -q -n %{module}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Smart/*
%{_mandir}/*/*

