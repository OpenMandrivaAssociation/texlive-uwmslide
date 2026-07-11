%global tl_name uwmslide
%global tl_revision 27354

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Slides with a simple Power Point like appearance
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uwmslide
License:	artistic
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwmslide.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwmslide.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A slide format which produces slides with a simple Power Point like
appearance. Several useful features include: use of standard titlepage
to produce title slide; several slide environments including plain (page
with a title), double slide (two column page with slide title), item
slide (item list with title), left item slide, and right item slide.
Logos are placed in the upper left corner of each slide if the logo file
logo.eps is present. Preconfigured in landscape mode by default and uses
Times Roman by default (originally, it was claimed, for simple
conversion to PDF format).

