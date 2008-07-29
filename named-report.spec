Summary:	ISC BIND 9 named log message summary and report tool
Name:		named-report
Version:	1.4
Release:	%mkrel 5
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


