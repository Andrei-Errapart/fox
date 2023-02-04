%define name fox
%define version 1.7.81
%define release 1

%global debug_package %{nil}

Summary: The FOX toolkit.
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPL+Addendum
Group: System Environment/Libraries
Source: ftp://ftp.fox-toolkit.org/pub/fox-1.7.81.tar.gz
URL: http://www.fox-toolkit.org
Packager: Jeroen van der Zijp <jeroen@fox-toolkit.net>
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
FOX is a C++-based library for graphical user interface development
FOX supports modern GUI features, such as drag-and-drop, tooltips, tab
books, tree lists, icons, multiple document interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics. Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

%package devel
Summary: Development files and documentation for the FOX GUI toolkit.
Group: Development/Libraries

%description devel
The fox-devel package contains the files necessary to develop applications
using the FOX GUI toolkit: the header files, the reswrap resource compiler,
manual pages, and HTML documentation.

%package static
Summary: A version of the FOX GUI toolkit for static linking.
Group: Development/Libraries

%description static
The fox-static package contains the files necessary to link applications
to the FOX GUI toolkit statically (rather than dynamically). Statically
linked applications do not require the library to be installed on the system
running the application.

%package -n adie
Summary: Adie Programmer's Text Editor
Group: X11/Applications
Version: 3.0.0

%description -n adie
Adie is an extremely fast and convenient programming text editor written using the FOX Toolkit.

%package -n calculator
Summary: FOX-based Calculator Applet
Group: X11/Applications
Version: 2.0.0

%description -n calculator
The FOX calculator is a simple desktop calculator geared towards the programmer.
It supports not only a full complement of scientific functions, but also common
operations that programmers need, such as bitwise operations, bitwise shifting,
and base-2 logarithm and exponents, and numeric conversion between hexadecimal,
octal, binary, and decimal.
The FOX Calculator implements correct operator precedences, so expressions like
2+3*5 yield the correct result, which is 17, and not 25.
Also featured is a constant memory, which permanently stores its value even if
you exit the calculator and restart it later.

%package -n pathfinder
Summary: PathFinder File Browser
Group: X11/Applications
Version: 1.0.0

%description -n pathfinder
PathFinder is a file browser application written using the FOX Toolkit.

%package -n shutterbug
Summary: Shutterbug Screenshot Utility
Group: X11/Applications
Version: 2.0.0

%description -n shutterbug
Shutterbug is a FOX-based screenshot utility.

%package -n controlpanel
Summary: ControlPanel Utility
Group: X11/Applications
Version: 1.0.0

%description -n controlpanel
ControlPanel is an application to edit colors, file associations, and
various other parameters common between all FOX applications.

%prep
%setup -q

%build
CPPFLAGS="$RPM_OPT_FLAGS -frtti" CFLAGS="$RPM_OPT_FLAGS -frtti" LDFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure --enable-release
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall

rm -f doc/Makefile.am doc/Makefile.in doc/Makefile
rm -r doc/art/Makefile.am doc/art/Makefile.in doc/art/Makefile
rm -f doc/screenshots/Makefile.am doc/screenshots/Makefile.in doc/screenshots/Makefile

# remove docs as they are supplied by rpm
rm -rf ${RPM_BUILD_ROOT}/%{_datadir}/doc/fox-1.7
rm -rf ${RPM_BUILD_ROOT}/usr/fox

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/libFOX-1.7.so
%{_libdir}/libFOX-1.7.so.0
%{_libdir}/libFOX-1.7.so.0.0.81
%{_libdir}/libCHART-1.7.so
%{_libdir}/libCHART-1.7.so.0
%{_libdir}/libCHART-1.7.so.0.0.81
%{_libdir}/pkgconfig/fox17.pc

%doc doc
%doc ADDITIONS AUTHORS INSTALL LICENSE README TRACING index.html

%files devel
%defattr(-,root,root)
%{_bindir}/reswrap
%{_bindir}/fox-config
%{_mandir}/man1/reswrap.1*
%{_includedir}/fox-1.7
%{_libdir}/libFOX-1.7.la
%{_libdir}/libCHART-1.7.la

%files static
%defattr(-,root,root)
%{_libdir}/libFOX-1.7.a
%{_libdir}/libCHART-1.7.a

%files -n adie
%defattr(-,root,root)
%{_bindir}/adie
%{_bindir}/Adie.stx
%{_mandir}/man1/adie.1*

%files -n calculator
%defattr(-,root,root)
%{_bindir}/calculator
%{_mandir}/man1/calculator.1*

%files -n pathfinder
%defattr(-,root,root)
%{_bindir}/PathFinder
%{_mandir}/man1/PathFinder.1*

%files -n shutterbug
%defattr(-,root,root)
%{_bindir}/shutterbug
%{_mandir}/man1/shutterbug.1*

%files -n controlpanel
%defattr(-,root,root)
%{_bindir}/ControlPanel
%{_mandir}/man1/ControlPanel.1*

%changelog
* Sat Wed 9 2011 Jeroen van der Zijp <jeroen@fox-toolkit.net>
- Added Control Panel application.
- Added package config to installed.
- Deleted very old stuff in change log.
