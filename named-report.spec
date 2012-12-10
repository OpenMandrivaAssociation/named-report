Summary:	ISC BIND 9 named log message summary and report tool
Name:		named-report
Version:	1.4
Release:	%mkrel 7
License:	GPL
Group:		System/Servers
URL:		http://aharp.ittns.northwestern.edu/software/
Source:		http://aharp.ittns.northwestern.edu/software/named-report-1.4.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
ISC BIND 9 named log message summary and report tool.

%prep

%setup -q

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 %{name}.pl %{buildroot}%{_bindir}/%{name}.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}.pl




%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-7mdv2011.0
+ Revision: 620475
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.4-6mdv2010.0
+ Revision: 430152
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.4-5mdv2009.0
+ Revision: 253567
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4-3mdv2008.1
+ Revision: 136618
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-3mdv2007.0
+ Revision: 113808
- Import named-report

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-3mdv2007.1
- use the mkrel macro

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4-2mdk
- rebuild

* Tue Nov 23 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.4-1mdk
- initial mandrake package

