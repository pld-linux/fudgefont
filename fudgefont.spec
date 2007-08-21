# TODO:
# - build examples and add them to main package
# - add pl description and summary

Summary:	Fudges TTF fonts into Allegro
Summary(pl.UTF-8):	-
Name:		fudgefont
Version:	1.2
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/fudgefont/%{name}-%{version}-src.7z
# Source0-md5:	57bbe9b92d4f25210f803db481eb0939
Patch0:		%{name}-paths.patch
URL:		http://fudgefont.sourceforge.net/
BuildRequires:	allegro-devel
BuildRequires:	freetype-devel
BuildRequires:	p7zip
BuildRequires:	scons
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet another TTF addon for Allegro - but smaller than all others and
with full Unicode and AllegroGL support.

%description -l pl.UTF-8

%package devel
Summary:	Header files for fudgefont library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki fudgefont
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for fudgefont library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki fudgefont.

%prep
rm -rf fudgefont-1.2-src
7z x ../SOURCES/%{name}-%{version}-src.7z
cd %{name}-%{version}-src
%patch0 -p1

%build
cd %{name}-%{version}-src
scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cd %{name}-%{version}-src
install libfudgefont.so $RPM_BUILD_ROOT%{_libdir}
install src/fudgefont.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfudgefont.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/fudgefont.h
