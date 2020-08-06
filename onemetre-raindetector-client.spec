Name:      onemetre-raindetector-client
Version:   2.2.1
Release:   0
Url:       https://github.com/warwick-one-metre/raind
Summary:   Rain detector client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common

%description
Part of the observatory software for the Warwick one-meter telescope.

rain is a commandline utility that prints the latest measurement in a human-readable form.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/rain %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/rain %{buildroot}/etc/bash_completion.d/rain

%files
%defattr(0755,root,root,-)
%{_bindir}/rain
/etc/bash_completion.d/rain

%changelog
