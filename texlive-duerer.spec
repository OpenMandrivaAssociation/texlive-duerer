# revision 20741
# category Package
# catalog-ctan /fonts/duerer
# catalog-date 2010-12-14 12:03:20 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-duerer
Version:	20101214
Release:	1
Summary:	Computer Duerer fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/duerer
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/duerer.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
These fonts are designed for titling use, and consist of
capital roman letters only. Together with the normal set of
base shapes, the family also offers an informal shape. LaTeX
support is available in the duerer-latex bundle.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/duerer/cdb10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdi10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdr10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdsl10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdss10.mf
%{_texmfdistdir}/fonts/source/public/duerer/cdtt10.mf
%{_texmfdistdir}/fonts/source/public/duerer/dromani.mf
%{_texmfdistdir}/fonts/source/public/duerer/dromanu.mf
%{_texmfdistdir}/fonts/source/public/duerer/dtitle.mf
%{_texmfdistdir}/fonts/tfm/public/duerer/cdb10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdi10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdr10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdss10.tfm
%{_texmfdistdir}/fonts/tfm/public/duerer/cdtt10.tfm
%doc %{_texmfdistdir}/doc/fonts/duerer/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
