#sbs-git:slp/pkgs/l/lsb lsb 3.2 1eb8dfd6cc0768fd81b1d604eddd82287099af01

Name:       lsb
Summary:    LSB support for SLP
Version:    3.2
Release:    3
Group:      System/Base
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz
Source1001:	%{name}.manifest
Source1002:     %{name}
Provides:   /lib/lsb/init-functions

%description
Linux Standard Base 3.2

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
rm -rf %{buildroot}
install -d %{buildroot}/lib/lsb
cp -p init-functions %{buildroot}/lib/lsb

mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
cp %{SOURCE1002} $RPM_BUILD_ROOT%{_datadir}/license

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_datadir}/license/%{name}
/lib/lsb/init-functions
