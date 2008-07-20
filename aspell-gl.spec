Summary:	Galician dictionary for aspell
Summary(gl.UTF-8):	Dicionário galego (normativa de mínimos) para o Aspell
Summary(pl.UTF-8):	Słownik galicyjski dla aspella
Name:		aspell-gl
Version:	0.5a
%define	subv	2
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/gl/aspell6-gl-%{version}-%{subv}.tar.bz2
# Source0-md5:	7502e37bf2a1c4a0a05f9a6e755e7c21
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Galician dictionary (i.e. word list) for aspell.

%description -l gl.UTF-8
Dicionário galego (normativa de mínimos) para o Aspell.

%description -l pl.UTF-8
Słownik galicyjski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-gl-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/README.minimos
%lang(gl) %doc doc/normas.txt
%{_libdir}/aspell/*
%{_datadir}/aspell/*
