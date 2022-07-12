%define api 0
%define libname %mklibname discord-rpc %{api}
%define devname %mklibname discord-rpc -d

Name:           discord-rpc
Version:        3.4.0
%define shver	3_4_0
Release:        1
Summary:        Discord rich presence library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/discordapp/discord-rpc
Source:         https://github.com/discordapp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Add-some-library-versioning.patch
BuildRequires:  cmake
BuildRequires:  rapidjson

%description
This is a library for interfacing your game with a locally running Discord
desktop client.

%package -n %{libname}
Summary:        Discord RPC library
Group:          System/Libraries
Recommends:     discord
Provides:       discord-rpc

%description -n %{libname}
This is a library for interfacing your game with a locally running Discord
desktop client.

%package -n %{devname}
Summary:        Development files for libdiscord-rpc
Requires:	%{libname} = %{version}-%{release}
Provides: discord-rpc-devel

%description -n	%{devname}
Header files for the discord-rpc library.

%prep
%autosetup -p1
perl -i -lpe 's{\@PACKAGE_VERSION\@}{%version}g' src/CMakeLists.txt

%build
%cmake

%make_build

%install
%make_install -C build

%files -n %{devname}
%license LICENSE
%doc README.md
%{_includedir}/discord_register.h
%{_includedir}/discord_rpc.h
%{_libdir}/libdiscord-rpc.so

%files -n %{libname}
%{_libdir}/libdiscord-rpc.so.%{version}
