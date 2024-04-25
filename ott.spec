Name:           ott
Version:        0.33
Release:        %autorelease
Summary:        The Ott tool for writing definitions of programming languages and calculi

License:        Ott
URL:            https://github.com/ott-lang/ott
Source0:        https://github.com/ott-lang/ott/archive/%{version}/ott-%{version}.tar.gz

BuildRequires:  coq
BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-ocamlgraph-devel

%global debug_package %{nil}

%description
Ott is a tool for writing definitions of programming languages and calculi. It takes as input a definition of a language syntax and semantics, in a concise and readable ASCII notation that is close to what one would write in informal mathematics.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ott-%{version} -p1

%build
make
%dune_build

%install
%dune_install
mkdir -p %{buildroot}/usr/bin
cp bin/ott %{buildroot}/usr/bin/ott

%check
%dune_check

%files -f .ofiles
%doc README.md
%{_bindir}/ott

%files devel -f .ofiles-devel

%changelog
%autochangelog
