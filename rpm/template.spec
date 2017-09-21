Name:           ros-lunar-dynpick-driver
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS dynpick_driver package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/dynpick_driver
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-robot-state-publisher
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rviz
Requires:       ros-lunar-std-srvs
Requires:       ros-lunar-tf
Requires:       ros-lunar-xacro
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-std-srvs

%description
Driver package for Wacohtech dynpick force sensor. This contains ROS-compatible
linux driver, as well as a communication test tool. As of Oct 2016, it's tested
with the following models of dynpick: wdf-6m200-3 WEF-6A200 (confirmed here)

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Fri Sep 22 2017 TORK <dev@opensource-robotics.tokyo.jp> - 0.2.0-0
- Autogenerated by Bloom

