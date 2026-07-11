%global tl_name duerer
%global tl_revision 20741

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Computer Duerer fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/duerer
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These fonts are designed for titling use, and consist of capital roman
letters only. Together with the normal set of base shapes, the family
also offers an informal shape. The distribution is as Metafont source.
LaTeX support is available in the duerer-latex bundle.

