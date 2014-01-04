Summary:	ID3 tag editor
Name:		easytag
Version:	2.1.9
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://download.gnome.org/sources/easytag/2.1/%{name}-%{version}.tar.xz
# Source0-md5:	789c1e6d3f653374a916b7f503ee1977
URL:		http://easytag.sourceforge.net/
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	id3lib-devel
BuildRequires:	id3lib-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkg-config
BuildRequires:	speex-devel
BuildRequires:	taglib-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EasyTAG is an utility for viewing, editing and writing tags of your
MP3, MP2, FLAC, Ogg, MusePack and Monkey's Audio files. Its simple
and nice GTK+ interface makes tagging easier.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules	\
	--with-gtk3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT%{_desktopdir}/easytag.desktop

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog HACKING README TODO THANKS
%attr(755,root,root) %{_bindir}/easytag
%{_desktopdir}/easytag.desktop
%{_iconsdir}/hicolor/*/apps/easytag.*
%{_mandir}/man1/easytag.1*

