Name:           discord-rpc
Version:        3.4.0
%define shver	3_4_0
Release:        1
Summary:        Discord rich presence library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/discordapp/discord-rpc
Source:         https://github.com/discordapp/%{name}/archive/v%{version}.tar.gz
Patch1:         0001-Add-some-library-versioning.patch
BuildRequires:  cmake
#BuildRequires:  rapidjson-devel

%description
This is a library for interfacing your game with a locally running Discord
desktop client.

%package -n libdiscord-rpc%{shver}
Summary:        Discord RPC library
Group:          System/Libraries
Recommends:     discord

%description -n libdiscord-rpc%{shver}
This is a library for interfacing your game with a locally running Discord
desktop client.

%package devel
Summary:        Development files for libdiscord-rpc
Requires:       libdiscord-rpc%{shver} = %{version}-%{release}

%description devel
Header files for the discord-rpc library.

%prep
%autosetup -p1
perl -i -lpe 's{\@PACKAGE_VERSION\@}{%version}g' src/CMakeLists.txt

%build
%cmake

%make_build

%install
%make_install -C build

%files devel
%license LICENSE
%doc README.md
%{_includedir}/discord_register.h
%{_includedir}/discord_rpc.h
%{_libdir}/libdiscord-rpc.so

%files -n libdiscord-rpc%{shver}
%{_libdir}/libdiscord-rpc.so.%{version}
