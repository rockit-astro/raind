Name:      onemetre-rain-server
Version:   1.0
Release:   0
Url:       https://github.com/warwick-one-metre/raind
Summary:   Rain detector daemon for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-pyserial, python3-warwickobservatory, onemetre-obslog-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

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

%pre
%service_add_pre raind.service

%post
%service_add_post raind.service

%preun
%stop_on_removal raind.service
%service_del_preun raind.service

%postun
%restart_on_update raind.service
%service_del_postun raind.service

%files
%defattr(0755,root,root,-)
%{_bindir}/raind
%{_udevrulesdir}/10-onemetre-rain.rules
%defattr(-,root,root,-)
%{_unitdir}/raind.service

%changelog
