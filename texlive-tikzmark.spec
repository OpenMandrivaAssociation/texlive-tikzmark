Name:		texlive-tikzmark
Version:	1.6
Release:	1
Summary:	Use TikZ's method of remembering a position on a page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzmark
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzmark.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzmark.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzmark.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tikzmark package defines a command to "remember" a position
on a page for later (or earlier) use, primarily (but not
exclusively) with TikZ.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzmark
%doc %{_texmfdistdir}/doc/latex/tikzmark
#- source
%doc %{_texmfdistdir}/source/latex/tikzmark

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
