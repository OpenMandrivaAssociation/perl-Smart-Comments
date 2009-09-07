%define upstream_name	 Smart-Comments
%define upstream_version 1.0.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Comments that do more than just sit there
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(version)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Smart comments provide an easy way to insert debugging and tracking code into a
program. They can report the value of a variable, track the progress of a loop,
and verify that particular assertions are true.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
