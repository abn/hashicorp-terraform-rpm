%define debug_package %{nil}
%define go_path %{_builddir}/go
%define go_package github.com/hashicorp/terraform
%define go_package_src %{go_path}/src/%{go_package}

Name:           terraform
Version:        0.6.0
Release:        1%{?dist}
Summary:        Terraform is a tool for building, changing, and combining infrastructure safely and efficiently.

Group:          Development/Libraries
License:        MPLv2.0
URL:            https://www.terraform.io/
Source0:        https://%{go_package}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Use-version-release-and-arch-from-specfile.patch

BuildRequires:  golang git make hg

%description
Terraform is a tool for building, changing, and combining infrastructure safely 
and efficiently.

%prep
%autosetup -p1

mkdir -p %{go_package_src}
cp -R * %{go_package_src}/.

%build
export GOPATH=%{go_path}
cd %{go_package_src}
export RPM_VERSION=%{version}
export RPM_RELEASE=%{release}
export PATH=${PATH}:%{go_path}/bin
make updatedeps
make dev

%install
install -d %{buildroot}/%{_bindir}
find %{go_path}/bin -name "%{name}*" -exec install {} %{buildroot}/%{_bindir} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}*
%doc CHANGELOG.md README.md LICENSE

%changelog
* Fri Jul 03 2015 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.6.0-1
- Initial RPM release (v0.6.0)

