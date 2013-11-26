%define		packname	annotate

Summary:	Graphics related functions for Bioconductor
Name:		R-%{packname}
Version:	1.40.0
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	3bad7d1d9e213064f23c54d0b60eb82c
URL:		http://bioconductor.org/packages/release/bioc/html/annotate.html
BuildRequires:	R
BuildRequires:	R-AnnotationDbi
BuildRequires:	R-cran-xtable
BuildRequires:	R-cran-XML
BuildRequires:	R-cran-DBI
BuildRequires:	R-Biobase
BuildRequires:	R-BiocGenerics
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-AnnotationDbi
Requires:	R-cran-xtable
Requires:	R-cran-XML
Requires:	R-cran-DBI
Requires:	R-Biobase
Requires:	R-BiocGenerics
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Some basic functions for plotting genetic data.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/misc
%{_libdir}/R/library/%{packname}/unitTests
