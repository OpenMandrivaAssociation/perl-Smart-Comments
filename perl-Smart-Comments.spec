%define module	Smart-Comments
%define name	perl-%{module}
%define version 1.0.2
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Comments that do more than just sit there
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Smart/%{module}-v%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl
BuildRequires:	perl-devel
BuildRequires:	perl-version

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

