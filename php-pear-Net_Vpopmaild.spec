%define		_class		Net
%define		_subclass	Vpopmaild
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.2
Release:	%mkrel 2
Summary:	Class for accessing Vpopmail's vpopmaild daemon
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_Vpopmaild/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Supports all vpopmaild commands, such as adding/removing domains, users, robots
(autoresponders), and ezmlm lists (todo), as well as modifying domain limits,
ip maps, etc

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-2mdv2012.0
+ Revision: 742169
- fix major breakage by careless packager

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-1
+ Revision: 741266
- 0.3.2

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-6
+ Revision: 679545
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-5mdv2011.0
+ Revision: 613742
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-4mdv2010.1
+ Revision: 468727
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-3mdv2010.0
+ Revision: 441496
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-2mdv2009.1
+ Revision: 322505
- rebuild

* Wed Sep 03 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdv2009.0
+ Revision: 279772
- import php-pear-Net_Vpopmaild


* Wed Sep 03 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-1mdv2009.0
- initial Mandriva package
