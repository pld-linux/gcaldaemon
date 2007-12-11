# TODO
# - daemon and startup script
# - external packages:
#   /usr/share/gcaldaemon/license/g4j-license.txt
#   /usr/share/gcaldaemon/license/gcaldaemon-license.txt
#   /usr/share/gcaldaemon/license/google-license.txt
#   /usr/share/gcaldaemon/license/ical4j-license.txt
#   /usr/share/gcaldaemon/license/jdom-license.txt
#   /usr/share/gcaldaemon/license/rome-license.txt
#   /usr/share/gcaldaemon/license/shared-asn1-license.txt
#   /usr/share/gcaldaemon/license/shared-ldap-license.txt
#   /usr/share/gcaldaemon/license/wrapper-license.txt
%include	/usr/lib/rpm/macros.java
Summary:	gcaldaemon
Name:		gcaldaemon
Version:	1.0
Release:	0.4
License:	LGPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/gcaldaemon/%{name}-linux-%{version}-beta14.zip
# Source0-md5:	3df598920e0283eb60b38536e06ee94f
URL:		http://gcaldaemon.sourceforge.net/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jaf
Requires:	jakarta-commons-codec
Requires:	jakarta-commons-collections
Requires:	jakarta-commons-httpclient
Requires:	jakarta-commons-io
Requires:	jakarta-commons-lang
Requires:	jakarta-commons-logging
Requires:	javamail
Requires:	logging-log4j
Requires:	servlet
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
GCALDaemon is an OS-independent Java program that offers two-way
synchronization between Google Calendar and various iCalendar
compatible calendar applications. GCALDaemon is primarily designed as
a calendar synchronizer but it can also be used as a Gmail notifier,
Address Book importer, Gmail terminal and RSS feed converter.

%prep
%setup -qc
cd GCALDaemon

%{__sed} -i -e 's,\r$,,' bin/reload-calendar.scpt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir}}
cd GCALDaemon
cp -a bin conf lang lib log work $RPM_BUILD_ROOT%{_appdir}
ln -nfs %{_javadir}/jaf.jar  $RPM_BUILD_ROOT%{_appdir}/lib/activation.jar
ln -nfs %{_javadir}/mail.jar  $RPM_BUILD_ROOT%{_appdir}/lib/mail.jar
ln -nfs %{_javadir}/servlet.jar  $RPM_BUILD_ROOT%{_appdir}/lib/servlet-api.jar
ln -nfs %{_javadir}/commons-codec.jar  $RPM_BUILD_ROOT%{_appdir}/lib/commons-codec.jar
ln -nfs %{_javadir}/commons-collections.jar  $RPM_BUILD_ROOT%{_appdir}/lib/commons-collections.jar
ln -nfs %{_javadir}/commons-httpclient.jar  $RPM_BUILD_ROOT%{_appdir}/lib/commons-httpclient.jar
ln -nfs %{_javadir}/commons-io.jar  $RPM_BUILD_ROOT%{_appdir}/lib/commons-io.jar
ln -nfs %{_javadir}/commons-lang.jar  $RPM_BUILD_ROOT%{_appdir}/lib/commons-lang.jar
ln -nfs %{_javadir}/commons-logging.jar  $RPM_BUILD_ROOT%{_appdir}/lib/commons-logging.jar
ln -nfs %{_javadir}/log4j.jar  $RPM_BUILD_ROOT%{_appdir}/lib/logger.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc GCALDaemon/docs/*
%dir %{_appdir}
%{_appdir}/bin
%{_appdir}/conf
%{_appdir}/lang
%{_appdir}/lib
%{_appdir}/log
%{_appdir}/work
