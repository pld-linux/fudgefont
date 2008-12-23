# TODO:
# - build examples and add them to main package

Summary:	Fudges TTF fonts into Allegro
Summary(pl.UTF-8):	Umieszczanie fontów TTF w Allegro
Name:		fudgefont
Version:	1.4
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://dl.sourceforge.net/fudgefont/%{name}-%{version}-src.7z
# Source0-md5:	4eb0eec8f430a39b4941cebea512c263
URL:		http://sourceforge.net/projects/fudgefont/
BuildRequires:	allegro-devel
BuildRequires:	freetype-devel
BuildRequires:	p7zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet another TTF addon for Allegro - but smaller than all others and
with full Unicode and AllegroGL support.

%description -l pl.UTF-8
Jeszcze jeden dodatek TTF dla Allegro - ale mniejszy od innych i z
pełną obsługą Unikodu i AllegroGL.

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
%setup -q -c -T -n %{name}-%{version}-src
7z x -o.. %{SOURCE0}

%build
%{__cc} %{rpmcflags} -o fudgefont.os -c -fPIC `freetype-config --cflags` src/fudgefont.c
%{__cc} %{rpmcflags} -o kerning.os -c -fPIC `freetype-config --cflags` src/kerning.c
%{__cc} %{rpmcflags} %{rpmldflags}-o libfudgefont.so -shared fudgefont.os kerning.os `freetype-config --libs` `allegro-config --libs`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

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
