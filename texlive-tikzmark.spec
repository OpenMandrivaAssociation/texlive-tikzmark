# revision 29999
# category Package
# catalog-ctan /graphics/pgf/contrib/tikzmark
# catalog-date 2013-04-17 11:11:14 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-tikzmark
Version:	1.0
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
%{_texmfdistdir}/tex/latex/tikzmark/tikzlibrarytikzmark.code.tex
%{_texmfdistdir}/tex/latex/tikzmark/tikzmarklibrarylistings.code.tex
%doc %{_texmfdistdir}/doc/latex/tikzmark/README.txt
%doc %{_texmfdistdir}/doc/latex/tikzmark/tikzmark.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tikzmark/tikzmark.dtx
%doc %{_texmfdistdir}/source/latex/tikzmark/tikzmark.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
