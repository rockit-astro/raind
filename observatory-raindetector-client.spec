Name:      observatory-raindetector-client
Version:   20220722
Release:   0
Url:       https://github.com/warwick-one-metre/raind
Summary:   Rain detector client for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common

%description

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
