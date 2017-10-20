Name:      onemetre-raindetector-server
Version:   2.0
Release:   0
Url:       https://github.com/warwick-one-metre/raind
Summary:   Rain detector daemon for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-pyserial, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-pyserial, python34-warwick-observatory-common, observatory-log-client, %{?systemd_requires}
%endif

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
%if 0%{?suse_version}
%service_add_pre raind.service
%endif

%post
%if 0%{?suse_version}
%service_add_post raind.service
%endif
%if 0%{?centos_ver}
%systemd_post raind.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal raind.service
%service_del_preun raind.service
%endif
%if 0%{?centos_ver}
%systemd_preun raind.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update raind.service
%service_del_postun raind.service
%endif
%if 0%{?centos_ver}
%systemd_postun_with_restart raind.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/raind
%{_udevrulesdir}/10-onemetre-rain.rules
%defattr(-,root,root,-)
%{_unitdir}/raind.service

%changelog
