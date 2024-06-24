Name:           xdg-desktop-portal-xapp
Version:        1.0.7
Release:        1
Summary:        Backend implementation for xdg-desktop-portal using Xapp
Group:          System/Libraries/Cinnamon
License:        LGPL-2.1-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
 
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  meson
BuildRequires:  pkgconfig(xdg-desktop-portal)
 
Requires:       dbus-x11
Requires:       dbus-common
Requires:       xapp
Requires:       xdg-desktop-portal
Requires:       xdg-desktop-portal-gtk
Supplements:    cinnamon
 
%description
Xapp's Cinnamon, MATE and XFCE backends for xdg-desktop-portal.
This allows sandboxed applications to request services and information from
outside the sandbox in the MATE, XFCE and Cinnamon environments.
 
%prep
%autosetup -p1
 
%build
%meson -Dsystemduserunitdir=%{_userunitdir}
%meson_build
 
%install
%meson_install

%post
%systemd_user_post %{name}.service
 
%preun
%systemd_user_preun %{name}.service
 
%files
%license COPYING
%doc README.md
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.xapp.service
%{_datadir}/xdg-desktop-portal/portals/xapp.portal
%{_userunitdir}/xdg-desktop-portal-xapp.service
