Name:		example-platform-app
Version:	1.0
Release:	1
Summary:	Example Tizen Platform App

License:	GPL2
URL:		http://rtg.in.ua
Source0:	%{name}-%{version}.tar.gz

%description
Example Tizen Platform Application

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}


%files
%{_bindir}/example-platform-app

%changelog
* Sat Aug 17 2013 Roman Yepishev <roman.yepishev@yandex.ua>
- Initial version
