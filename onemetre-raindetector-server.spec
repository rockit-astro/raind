Name:      onemetre-raindetector-server
Version:   2.3
Release:   0
Url:       https://github.com/warwick-one-metre/raind
Summary:   Rain detector daemon for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-pyserial, python36-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick one-meter telescope.

raind recieves data from a custom rain detector board and
makes the latest measurement available for other services via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/raind %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/raind.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/10-onemetre-rain.rules %{buildroot}%{_udevrulesdir}

%post
%systemd_post raind.service

%preun
%systemd_preun raind.service

%postun
%systemd_postun_with_restart raind.service

%files
%defattr(0755,root,root,-)
%{_bindir}/raind
%{_udevrulesdir}/10-onemetre-rain.rules
%defattr(-,root,root,-)
%{_unitdir}/raind.service

%changelog
