Summary:	Generic Programming for Computer Vision
Summary(pl):	Ogólne programowanie obrazu komputerowego
Name:		vigra
Version:	1.2.0
Release:	1
License:	The VIGRA Artistic License
Group:		Libraries
Source0:	http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/%{name}%{version}.tar.gz
# Source0-md5:	fbb385e93d4b40469b04af4bc7079734
Patch0:		%{name}-ac.patch
URL:		http://kogs-www.informatik.uni-hamburg.de/~koethe/vigra/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fftw-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VIGRA stands for "Vision with Generic Algorithms". It's a novel
computer vision library that puts its main emphasize on customizable
algorithms and data structures. By using template techniques similar
to those in the C++ Standard Template Library, you can easily adapt
any VIGRA component to the needs of your application, without thereby
giving up execution speed.

%description -l pl
VIGRA to skrót od "Vision with Generic Algorithms" (widok z ogólnymi
algorytmami). Jest to nowa biblioteka do obrazu komputerowego k³ad±ca
g³ówny nacisk na algorytmy i struktury danych z mo¿liwo¶ci±
dostosowania do w³asnych potrzeb. Poprzez u¿ycie technik szablonów
podobnych do tych w standardowej bibliotece szablonów C++ (STL) mo¿na
³atwo zaadaptowaæ dowolny komponent VIGRA do potrzeb w³asnej aplikacji
bez po¶wiêcania szybko¶ci wykonywania.

%package devel
Summary:        Header files for vigra library
Summary(pl):	Pliki nag³ówkowe biblioteki vigra
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libstdc++-devel
Requires:	libtiff-devel

%description devel
Header files needed to compile programs with vigra.

%description devel -l pl
Pliki nag³ówkowe potrzebne do budowania programów u¿ywaj±cych
biblioteki vigra.

%package static
Summary:        vigra - static library
Summary(pl):	Statyczna biblioteka vigra
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static version of vigra library.

%description static -l pl
Statyczna wersja biblioteki vigra.

%package doc
Summary:	Development documentation for vigra library
Summary(pl):	Dokumentacja programisty do biblioteki vigra
Group:		Documentation

%description doc
Development documentation for vigra library.

%description doc -l pl
Dokumentacja programisty do biblioteki vigra.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

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

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec-prefix=$RPM_BUILD_ROOT%{_exec_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	includedir=$RPM_BUILD_ROOT%{_includedir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vigra-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/vigra

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files doc
%defattr(644,root,root,755)
%doc @docdir@/[!L]*
