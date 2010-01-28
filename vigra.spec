Summary:	Generic Programming for Computer Vision
Summary(pl.UTF-8):	Ogólne programowanie obrazu komputerowego
Name:		vigra
Version:	1.6.0
Release:	4
License:	MIT
Group:		Libraries
Source0:	http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/%{name}%{version}.tar.gz
# Source0-md5:	d62650a6f908e85643e557a236ea989c
Patch0:		%{name}-ac.patch
Patch1:		%{name}-libpng.patch
URL:		http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw3-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
#BuildRequires:	python
#BuildRequires:	python-devel
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
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libstdc++-devel
Requires:	libtiff-devel

%description devel
Header files needed to compile programs with vigra.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania programów używających
biblioteki vigra.

%package static
Summary:	vigra - static library
Summary(pl.UTF-8):	Statyczna biblioteka vigra
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of vigra library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki vigra.

%package doc
Summary:	Development documentation for vigra library
Summary(pl.UTF-8):	Dokumentacja programisty do biblioteki vigra
Group:		Documentation

%description doc
Development documentation for vigra library.

%description doc -l pl.UTF-8
Dokumentacja programisty do biblioteki vigra.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1

tail -n +510 config/acinclude.m4 > acinclude.m4
ln -sf config/configure.in .

%build
cp -f /usr/share/automake/config.* config
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--with-fftw \
	--with-jpeg \
	--with-png \
	--with-tiff \
	--with-zlib

#	--with-python requires src/pythonbindings (missing in sources)

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec-prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir} \
	docdir=`pwd`/docs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%attr(755,root,root) %{_libdir}/libvigraimpex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvigraimpex.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vigra-config
%attr(755,root,root) %{_libdir}/libvigraimpex.so
%{_libdir}/libvigraimpex.la
%{_includedir}/vigra

%files static
%defattr(644,root,root,755)
%{_libdir}/libvigraimpex.a

%files doc
%defattr(644,root,root,755)
%doc docs/[!L]*
