%define name stickers
%define	version 0.1.3
%define	release %mkrel 1

Summary: Stickers game
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Toys
Source: %name-%version.tar.bz2
Source1: stickers.desktop
Source3: stickers.menu
Source4: stickers32x32.png
Source5: stickers16x16.png
Source6: stickers48x48.png
URL: http://users.powernet.co.uk/kienzle/stickers
BuildRoot: %{_tmppath}/%{name}-root

%description
Sticker Book is a program which lets you place images on a background
scene. Every parent surely knows how much fun kids have with
these. Indeed, they are a must for any long plane or car ride. Our
program is even better than the paper version (assuming you have a
laptop) since you can resize, recolour and reorient the stickers that
you use, and since you never need run out of stickers. You can even
paint with them!

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make DEFS="$RPM_OPT_FLAGS" 

%install
make DESTDIR=%{buildroot} install 
mkdir -p %{buildroot}%{_datadir}/applnk/Amusements/Toys
mkdir -p %{buildroot}%{_datadir}/icons/mini
mkdir -p %{buildroot}%{_datadir}/icons/large
mkdir -p %{buildroot}%{_libdir}//menu
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applnk/Amusements/Toys/stickers.desktop
install -m 0644 %{SOURCE3} %{buildroot}%{_libdir}/menu/stickers
install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/icons/stickers.png
install -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/icons/mini/stickers.png
install -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/icons/large/stickers.png
rm -f %{buildroot}%{_datadir}/stickers/scenes/Makefile

%post
%update_menus

%postun
%update_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/stickers
%{_datadir}/stickers
%{_datadir}/applnk/Amusements/Toys/stickers.desktop
%{_datadir}/icons/stickers.png
%{_datadir}/icons/mini/stickers.png
%{_datadir}/icons/large/stickers.png
%{_libdir}/menu/stickers
%doc README TODO INSTALL ChangeLog

