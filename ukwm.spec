%define debug_package %{nil}

Name:           ukwm
Version:        1.2.1
Release:        3
Summary:        lightweight GTK+ window manager
License:        GPL-2+ LGPL-2+ MIT~OldStyle+LegalDisclaimer Expat SGI-B-2.0 
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz
Patch0:         0001-Bump-dependency-on-gsettings-desktop-schemas-3.31.0.patch
Patch1:         0002-update-copyright.patch 
#BuildRequires: dh-sequence-gir is in gobject-introspection
BuildRequires: gobject-introspection
#BuildRequires: gnome-pkg-tools >= 0.10  debian package tool
BuildRequires: gtk-doc >= 1.15
BuildRequires: gtk3-devel >= 3.19.8
BuildRequires: glib2-devel >= 2.53.2
BuildRequires: libcanberra-devel
BuildRequires: gobject-introspection >= 1.41.3
BuildRequires: gsettings-desktop-schemas-devel >= 3.21.4
#BuildRequires: libgireposityuory1.0-dev >= 0.9.12
BuildRequires: gobject-introspection-devel
BuildRequires: json-glib-devel >= 0.13.2-1~
BuildRequires: mesa-libgbm-devel >= 10.3
BuildRequires: pango-devel >= 1.2.0
BuildRequires: cairo-devel >= 1.10.0
BuildRequires: mesa-libGL-devel >= 7.1~rc3-1~
BuildRequires: libdrm-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: gnome-desktop3-devel >= 3.21.2
BuildRequires: libgudev-devel >= 232
BuildRequires: libinput-devel
BuildRequires: startup-notification-devel >= 0.7
BuildRequires: systemd-devel >= 212
BuildRequires: upower-devel >= 0.99.0
BuildRequires: libwacom-devel >= 0.13

#BuildRequires: libxcb-randr0-dev
#BuildRequires: libxcb-res0-dev
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-renderutil-devel

#libXcomposite-devel curent version:0.44 ,have no version 1.0.2
BuildRequires: libXcomposite-devel
#libXi-devel curent version:1.7.9 ,have no version 2.1.6
BuildRequires: libXi-devel
BuildRequires: libxkbfile-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbcommon-devel >= 0.4.3
#BuildRequires: libx11-xcb-dev
BuildRequires: libXfixes-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcursor-devel
BuildRequires: libXt-devel
BuildRequires: libX11-devel
BuildRequires: libXinerama-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
BuildRequires: libXrender-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: pam-devel
BuildRequires: wayland-devel >= 1.13.0
BuildRequires: wayland-protocols-devel >= 1.9

#BuildRequires: xkb-data
BuildRequires: xkeyboard-config

#BuildRequires: xvfb
BuildRequires: xorg-x11-server-Xvfb

BuildRequires: xauth
BuildRequires: intltool
Requires: clutter
%description
 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the core binaries.
 
%package -n libukwm-1-0
Summary:     window manager library from the Ukwm window manager
License:     LGPLv2+
Requires: ukwm-common, gsettings-desktop-schemas >= 3.15.92

%description -n libukwm-1-0
 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the window manager shared library, used by ukwm
 itself, and gnome-shell.


%package common
Summary:     shared files for the Ukwm window manager
License:     LGPLv2+

%description common
 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the shared files.

%package -n libukwm-1-dev
Summary:     Development files for the Ukwm window manager
License:     LGPLv2+
Requires: libukwm-1-0, gir1.2-ukwm-1, atk-devel, libgudev-devel, gdk-pixbuf2-devel

%description -n libukwm-1-dev
 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the development files.
 
%package -n gir1.2-ukwm-1
Summary:     GObject introspection data for Ukwm
License:     LGPLv2+
Requires: libukwm-1-0

%description -n gir1.2-ukwm-1
Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the GObject introspection data which may be
 used to generate dynamic bindings.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%build
./autogen.sh

%define gettext_version %(dnf info gettext |grep Version |awk '{print $3}'| awk -F "." 'BEGIN {OFS = FS} {print $1,$2}')
sed -i "/GETTEXT_MACRO_VERSION/s/0.19/%{gettext_version}/g" po/Makefile.in.in

make

%install
rm -rf $RPM_BUILD_ROOT 
#make INSTALL_ROOT=/root/rpmbuild/BUILDROOT install
make DESTDIR=$RPM_BUILD_ROOT install

cp -rf %{buildroot}/usr/local/bin  %{buildroot}/usr/bin
rm -rf %{buildroot}/usr/local/bin

cp -rf %{buildroot}/usr/local/share  %{buildroot}/usr/share
rm -rf %{buildroot}/usr/local/share

cp -rf %{buildroot}/usr/local/include  %{buildroot}/usr/include
rm -rf %{buildroot}/usr/local/include


mkdir -p %{buildroot}/usr/lib/ukwm
cp -rf %{buildroot}/usr/local/libexec/ukwm-restart-helper  %{buildroot}/usr/lib/ukwm/ukwm-restart-helper
rm -rf %{buildroot}/usr/local/libexec



%clean
rm -rf $RPM_BUILD_ROOT

%preun
update-alternatives --remove x-window-manager \
        /usr/bin/ukwm
        
%post
update-alternatives --install /usr/bin/x-window-manager \
  x-window-manager /usr/bin/ukwm 60 \
  --slave /usr/share/man/man1/x-window-manager.1.gz \
  x-window-manager.1.gz /usr/share/man/man1/ukwm.1.gz
        
%files 
%{_bindir}/*
%{_prefix}/lib//ukwm/ukwm-restart-helper
%{_prefix}/local/lib/ukwm/plugins/
%{_datadir}/applications/
%{_datadir}/ukui/plugin/org.ukui.ukwm.UkwmPlugin.xml

%files -n libukwm-1-0
%{_prefix}/local/lib/libukwm-1.so.*
%{_prefix}/local/lib/ukwm/*.so

%files common
%doc debian/copyright debian/changelog
%{_datadir}/GConf
%{_datadir}/glib-2.0
%{_datadir}/locale
%{_datadir}/man
%{_datadir}/gnome-control-center

%files -n libukwm-1-dev
%{_prefix}/include
%{_prefix}/local/lib/lib*.so
%{_prefix}/local/lib/pkgconfig/*.pc
%{_prefix}/local/lib/ukwm/*.gir

%files -n gir1.2-ukwm-1
%{_prefix}/local/lib/ukwm/*.typelib

%exclude %{_prefix}/local/lib/libukwm-1.la
%exclude %{_prefix}/local/lib/ukwm/*.la
%exclude %{_datadir}/ukui

%changelog
* Thu Dec 23 2021 pei-jiankang <peijiankang@kylinos.cn> - 1.2.1-3
- update copyright

* Thu Dec 23 2021 pei-jiankang <peijiankang@kylinos.cn> - 1.2.1-2
- Bump dependency on gsettings desktop schemas 3.31.0

* Mon Oct 26 2020 douyan <douyan@kylinos.cn> - 1.2.1-1
- update to upstream version 1.2.1

* Thu Jul 9 2020 douyan <douyan@kylinos.cn> - 1.2.0-1
- Init package for openEuler

