#
Summary:	Implementation of the EAP-IKEv2 authentication method
Summary(pl.UTF-8):	Implementacja metody uwierzytelnienia EAP-IKEv2
Name:		libeap-ikev2
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/eap-ikev2/%{name}-%{version}.tar.gz
# Source0-md5:	e8c4900ff9f2825e189be66c61d146f2
URL:		http://eap-ikev2.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EAP-IKEv2 is an EAP authentication method based on the Internet Key
Exchange Protocol version 2 (IKEv2). It provides mutual authentication
and session key establishment between an EAP peer and an EAP server.
It supports authentication techniques that are based on asymmetric key
pairs, symmetric keys and passwords.

%description -l pl.UTF-8
EAP-IKEv2 jest protołem uwierzytelnienia pozwalającym na bezpieczne
uwierzytelnienie i wymianę kluczy sesji pomiędzy serwerem i klientem
EAP. Metoda ta bazuje na kluczach kryptograficznych i hasłach.

%package devel
Summary:	Header files for libeap-ikev2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libeap-ikev2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libeap-ikev2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libeap-ikev2.

%package static
Summary:	Static libeap-ikev2 library
Summary(pl.UTF-8):	Statyczna biblioteka libeap-ikev2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libeap-ikev2 library.

%description static -l pl.UTF-8
Statyczna biblioteka libeap-ikev2.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeap-ikev2.so.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libeap-ikev2.so
%{_libdir}/libeap-ikev2.la
%{_includedir}/EAPIKEv2

%files static
%defattr(644,root,root,755)
%{_libdir}/libeap-ikev2.a
