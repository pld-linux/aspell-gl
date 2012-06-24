Summary:	Galician dictionary for aspell
Summary(gl):	Dicion�rio galego (normativa de m�nimos) para o Aspell
Summary(pl):	S�ownik galicyjski dla aspella
Name:		aspell-gl
Version:	0.50
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/gl/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	0cd3c4e3e325e080689657f03eff8e8e
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Galician dictionary (i.e. word list) for aspell.

%description -l gl
Dicion�rio galego (normativa de m�nimos) para o Aspell.

%description -l pl
S�ownik galicyjski (lista s��w) dla aspella.

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
