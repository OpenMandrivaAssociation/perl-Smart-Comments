%define upstream_name	 Smart-Comments
%define upstream_version 1.000005

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.000005
Release:	3

Summary:	Comments that do more than just sit there
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/D/DC/DCONWAY/Smart-Comments-1.000005.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(version)

BuildArch:	noarch

%description
Smart comments provide an easy way to insert debugging and tracking code into a
program. They can report the value of a variable, track the progress of a loop,
and verify that particular assertions are true.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Smart/*
%{_mandir}/*/*


%changelog
* Mon Sep 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.0.4-1mdv2010.0
+ Revision: 432340
- update to 1.0.4

* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-3mdv2010.0
+ Revision: 430536
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-2mdv2009.0
+ Revision: 268722
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.3-1mdv2009.0
+ Revision: 195127
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 23911
- rebuild


* Mon Mar 20 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.2-1mdk
- New release 1.0.2

* Thu Oct 06 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.0.1-1mdk
- Initial MDV release.


