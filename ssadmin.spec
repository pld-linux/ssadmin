Summary:	InfiniBand SSA administration utility
Summary(pl.UTF-8):	Narzędzie administracyjne InfiniBand SSA
Name:		ssadmin
Version:	0.0.9
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	https://www.openfabrics.org/downloads/management/ssa/%{name}-%{version}.tar.gz
# Source0-md5:	6d17e8b3bd31cdda6d6cef928ce7f32a
URL:		https://www.openfabrics.org/
BuildRequires:	libibumad-devel >= 1.3.10
BuildRequires:	libibverbs-devel >= 1.1.8
BuildRequires:	librdmacm-devel >= 1.0.21
BuildRequires:	pkgconfig
Requires:	libibumad >= 1.3.10
Requires:	libibverbs >= 1.1.8
Requires:	librdmacm >= 1.0.21
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SSA administration utility is a client application used for local
and remote monitoring and management of SSA services.

%description -l pl.UTF-8
Narzędzie administracyjne SSA to aplikacja kliencka służąca do
lokalnego oraz zdalnego monitorowania oraz zarządzania usługami SSA.

%prep
%setup -q

%build
%configure \
	rdmascript=rdma \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_sbindir}/ssadmin
%{_mandir}/man1/ssadmin.1*
