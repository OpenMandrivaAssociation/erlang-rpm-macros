%global debug_package %{nil}

Name:		erlang-rpm-macros
Version:	0.2.8
Release:	1
Summary:	Macros for simplifying building of Erlang packages
Group:		Development/Erlang
License:	MIT
URL:		https://github.com/lemenkov/erlang-rpm-macros
Source0:	https://github.com/lemenkov/erlang-rpm-macros/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		back-to-python2-patch
BuildArch:	noarch
Requires:	rpm-build >= 4.11
# Requires for BEAM parsing
#Requires:	python3-pybeam
#This has been backported to python2 as OpenMandrivas python3-rpm does not exist yet.
Requires:	python-rpm

%description
Macros for simplifying building of Erlang packages.

%prep
%setup -q
%apply_patches

%build
# Nothing to build


%install
# rename for our OM convention
mv macros.erlang erlang.macros
# and put it in the OM macros dir
mkdir -p %{buildroot}%{_sys_macros_dir}/
install -d %{buildroot}%{_rpmconfigdir}/fileattrs
install -d %{buildroot}%{_rpmconfigdir}/macros.d
install -p -m 0755 erlang-find-provides.py %{buildroot}%{_rpmconfigdir}/
install -p -m 0755 erlang-find-requires.py %{buildroot}%{_rpmconfigdir}/
install -p -m 0644 erlang.macros %{buildroot}%{_sys_macros_dir}/
install -p -m 0644 erlang.attr %{buildroot}%{_rpmconfigdir}/fileattrs/


%files
%doc README LICENSE
%{_rpmconfigdir}/erlang-find-provides.py
%{_rpmconfigdir}/erlang-find-requires.py
%{_rpmconfigdir}/fileattrs/erlang.attr
%{_sys_macros_dir}/erlang.macros



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 0.2.4-1.mga6
+ Revision: 1067914
- New version 0.2.4
- New version 0.2.3

* Fri Apr 22 2016 neoclust <neoclust> 0.2.2-1.mga6
+ Revision: 1004792
- imported package erlang-rpm-macros

