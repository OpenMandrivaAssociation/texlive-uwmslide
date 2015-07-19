# revision 27354
# category Package
# catalog-ctan /macros/latex/contrib/uwmslide
# catalog-date 2012-02-24 11:11:42 +0100
# catalog-license artistic
# catalog-version undef
Name:		texlive-uwmslide
Version:	20120224
Release:	9
Summary:	Slides with a simple Power Point like appearance
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uwmslide
License:	ARTISTIC
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwmslide.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwmslide.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A slide format which produces slides with a simple Power Point
like appearance. Several useful features include: use of
standard titlepage to produce title slide; several slide
environments including plain (page with a title), double slide
(two column page with slide title), item slide (item list with
title), left item slide, and right item slide. Logos are placed
in the upper left corner of each slide if the logo file
logo.eps is present. Preconfigured in landscape mode by default
and uses Times Roman by default (originally, it was claimed,
for simple conversion to PDF format).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uwmslide/uwmslide.cls
%doc %{_texmfdistdir}/doc/latex/uwmslide/README
%doc %{_texmfdistdir}/doc/latex/uwmslide/logo.eps
%doc %{_texmfdistdir}/doc/latex/uwmslide/test.tex
%doc %{_texmfdistdir}/doc/latex/uwmslide/vaux.eps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Aug 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120224-1
+ Revision: 814517
- Import texlive-uwmslide
- Import texlive-uwmslide

