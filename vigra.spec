Summary:	Generic Programming for Computer Vision
Name:		vigra
Version:	1.2.0
Release:	0.2
License:	The VIGRA Artistic License
Group:		Libraries
Source0:	http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/%{name}%{version}.tar.gz
# Source0-md5:	fbb385e93d4b40469b04af4bc7079734
URL:		http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	zlib-devel, libjpeg-devel, libpng-devel, libtiff-devel, fftw-devel

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel
computer vision library that puts its main emphasize on customizable
algorithms and data structures. By using template techniques similar
to those in the C++ Standard Template Library, you can easily adapt
any VIGRA component to the needs of your application, without thereby
giving up execution speed.

%package devel
Summary:        vigra - header files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files needed to compile programs with vigra.

%package static
Summary:        vigra - static library
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static version of vigra..

%prep
%setup -q -c

%build
cd %{name}%{version}

./configure \
        LDFLAGS="${LDFLAGS:-%rpmldflags}" \
	CFLAGS="${CFLAGS:-%rpmcflags}" \
	CXXFLAGS="${CXXFLAGS:-%rpmcflags}" \
	FFLAGS="${FFLAGS:-%rpmcflags}" \
	CPPFLAGS="${CPPFLAGS:-}" \
	%{?__cc:CC="%{__cc}"} \
	%{?__cxx:CXX="%{__cxx}"} \
	--build=%{_target_platform} \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
    --with-tiff \
    --with-jpeg \
    --with-png \
    --with-zlib \
    --with-fftw \
    --enable-shared=yes \
    --docdir=%{buildroot}%{_datadir}/doc/%{name}-%{version}


%{__make}


%install
rm -rf $RPM_BUILD_ROOT
cd %{name}%{version}
%{__make} \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec-prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}/LICENSE
%{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_docdir}
%attr(755,root,root) %{_bindir}
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
