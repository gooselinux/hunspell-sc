Name: hunspell-sc
Summary: Sardinian hunspell dictionaries
%define upstreamid 20081101
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/1446/2/Dict_sc_IT03.oxt
URL: http://extensions.services.openoffice.org/project/Dict_sc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: AGPLv3
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Sardinian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-sc

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc registration/agpl3-en.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20081101-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081101-3
- drop unneeded buildrequires

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081101-1
- latest version

* Wed Oct 29 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081027-1
- initial version
