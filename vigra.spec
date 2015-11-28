# TODO: [lib]lemon, WITH_LEMON
Summary:	Generic Programming for Computer Vision
Summary(pl.UTF-8):	Ogólne programowanie obrazu komputerowego
Name:		vigra
Version:	1.10.0
Release:	10
License:	MIT
Group:		Libraries
#Source0Download: http://ukoethe.github.io/vigra/#download
Source0:	https://github.com/ukoethe/vigra/releases/download/Version-1-10-0/%{name}-%{version}-src-with-docu.tar.gz
# Source0-md5:	85e2968e4ee5f9541b5dd8b3fb9cc433
URL:		http://hci.iwr.uni-heidelberg.de/vigra/
BuildRequires:	OpenEXR-devel
BuildRequires:	boost-python-devel >= 1.40.0
BuildRequires:	cmake >= 2.6.0
BuildRequires:	doxygen
BuildRequires:	fftw3-single-devel
BuildRequires:	hdf5-devel >= 1.8
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 2:1.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel
BuildRequires:	rpmbuild(macros) >= 1.586
BuildRequires:	sphinx-pdg
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel
computer vision library that puts its main emphasize on customizable
algorithms and data structures. By using template techniques similar
to those in the C++ Standard Template Library, you can easily adapt
any VIGRA component to the needs of your application, without thereby
giving up execution speed.

%description -l pl.UTF-8
VIGRA to skrót od "Vision with Generic Algorithms" (widok z ogólnymi
algorytmami). Jest to nowa biblioteka do obrazu komputerowego kładąca
główny nacisk na algorytmy i struktury danych z możliwością
dostosowania do własnych potrzeb. Poprzez użycie technik szablonów
podobnych do tych w standardowej bibliotece szablonów C++ (STL) można
łatwo zaadaptować dowolny komponent VIGRA do potrzeb własnej aplikacji
bez poświęcania szybkości wykonywania.

%package devel
Summary:	Header files for vigra library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki vigra
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	fftw3-single-devel
Requires:	hdf5-devel >= 1.8
Requires:	libjpeg-devel
Requires:	libpng-devel >= 2:1.4.0
Requires:	libstdc++-devel
Requires:	libtiff-devel
Obsoletes:	vigra-static

%description devel
Header files needed to compile programs with vigra.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania programów używających
biblioteki vigra.

%package -n python-vigra
Summary:	VIGRA Python bindings
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki VIGRA
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-numpy
Suggests:	python-PyQt4

%description -n python-vigra
VIGRA Python bindings.

%description -n python-vigra -l pl.UTF-8
Wiązania Pythona do biblioteki VIGRA.

%package -n python-vigra-devel
Summary:	Development file for VIGRA Python bindings
Summary(pl.UTF-8):	Plik programistyczny wiązań Pythona do biblioteki VIGRA
Group:		Development/Libraries
Requires:	cmake
Requires:	python-vigra = %{version}-%{release}

%description -n python-vigra-devel
Development (cmake config) file for VIGRA Python bindings.

%description -n python-vigra-devel -l pl.UTF-8
Plik programistyczny (konfiguracja cmake'a) dla wiązań Pythona do
biblioteki VIGRA.

%package doc
Summary:	Development documentation for vigra library
Summary(pl.UTF-8):	Dokumentacja programisty do biblioteki vigra
Group:		Documentation

%description doc
Development documentation for vigra library.

%description doc -l pl.UTF-8
Dokumentacja programisty do biblioteki vigra.

%prep
%setup -q

%build
%cmake . \
	-DCMAKE_CXX_FLAGS_RELEASE="-DNDEBUG" \
	-DWITH_BOOST_GRAPH=ON \
	-DWITH_OPENEXR=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/vigra
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/vigra
%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/vigra*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%attr(755,root,root) %{_libdir}/libvigraimpex.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libvigraimpex.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vigra-config
%attr(755,root,root) %{_libdir}/libvigraimpex.so
%{_includedir}/vigra
%dir %{_libdir}/vigra
%{_libdir}/vigra/VigraConfig*.cmake
%{_libdir}/vigra/vigra-targets*.cmake

%files -n python-vigra
%defattr(644,root,root,755)
%dir %{py_sitedir}/vigra
%attr(755,root,root) %{py_sitedir}/vigra/*.so
%{py_sitedir}/vigra/*.py[co]
%dir %{py_sitedir}/vigra/pyqt
%{py_sitedir}/vigra/pyqt/*.py[co]

%files -n python-vigra-devel
%defattr(644,root,root,755)
%dir %{_libdir}/vigranumpy
%{_libdir}/vigranumpy/VigranumpyConfig.cmake

%files doc
%defattr(644,root,root,755)
%doc doc/{vigra,vigranumpy}
