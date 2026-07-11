%global tl_name tikzmark
%global tl_revision 79232

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.16
Release:	%{tl_revision}.1
Summary:	Use TikZs method of remembering a position on a page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzmark
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzmark.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzmark.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzmark.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tikzmark package defines a command to "remember" a position on a
page for later (or earlier) use, primarily (but not exclusively) with
TikZ.

