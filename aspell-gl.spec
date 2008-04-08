Summary:	Galician dictionary for aspell
Summary(gl.UTF-8):	Dicionário galego (normativa de mínimos) para o Aspell
Summary(pl.UTF-8):	Słownik galicyjski dla aspella
Name:		aspell-gl
Version:	0.50
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/gl/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	0cd3c4e3e325e080689657f03eff8e8e
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Galician dictionary (i.e. word list) for aspell.

%description -l gl.UTF-8
Dicionário galego (normativa de mínimos) para o Aspell.

%description -l pl.UTF-8
Słownik galicyjski (lista słów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

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
%doc Copyright README
%lang(gl) %doc doc/{leme.txt,normas.txt}
%{_libdir}/aspell/*
%{_datadir}/aspell/*
