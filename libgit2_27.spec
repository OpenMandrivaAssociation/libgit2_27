%define major 27
%define libname %mklibname git2 %{major}

Name: libgit2_27
Version: 0.27.8
Release: 2
Source0: https://github.com/libgit2/libgit2/archive/v%{version}/libgit2-%{version}.tar.gz
Summary: Old version of the libgit library
URL: https://libgit2.github.com
License: GPLv2 with linking exception
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: python2
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(zlib)

%description
Git core methods provided as a re-entrant linkable library

This is an old version of libgit2, provided for compatibility
with legacy applications only.

%if "%{libname}" != "%{name}"
%package -n %{libname}
Summary: Old version of libgit2
Group: System/Libraries

%description -n %{libname}
Git core methods provided as a re-entrant linkable library

This is an old version of libgit2, provided for compatibility
with legacy applications only.
%endif

%prep
%setup -n libgit2-%{version}
%cmake -G Ninja \
	-DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/python2

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build

# No -devel files for compat packages
rm -rf	%{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/*.so \
	%{buildroot}%{_libdir}/pkgconfig

%if "%{libname}" != "%{name}"
%files -n %{libname}
%else
%files
%endif
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.0*
