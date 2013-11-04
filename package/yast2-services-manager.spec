#
# spec file for package yast2-services-manager
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


######################################################################
#
# IMPORTANT: Please do not change spec file in build service directly
#            Use https://github.com/yast/yast-services-manager repo
#
######################################################################

Name:           yast2-services-manager
Version:        0.0.11
Release:        0
BuildArch:      noarch

BuildRoot:      %{_tmppath}/%{name}-build
Source0:        %{name}.tar.bz2

Requires:       ruby >= 2.0
Requires:       yast2 >= 3.0.5
Requires:       yast2-ruby-bindings >= 1.2.0

BuildRequires:  ruby
BuildRequires:  update-desktop-files
BuildRequires:  yast2-ruby-bindings >= 1.2.0
BuildRequires:  yast2 >= 3.0.5
# Backward compatibility fix for opensuse-13.1
%if 0%{?suse_version} > 1310
BuildRequires:  rubygem-rspec
%endif

Summary:        YaST2 - Services Manager
Group:          System/YaST
License:        GPL-2.0+
Url:            https://github.com/yast/yast-services-manager

%description
Provides user interface and libraries to configure systemd
services and targets.

%prep
%setup -n yast2-services-manager

%check
# opensuse-13.1 does not contain rspec in default repositories
%if 0%{?suse_version} > 1310
rspec test/*_test.rb
%endif

%install
rake install DESTDIR="%{buildroot}"
%suse_update_desktop_file services-manager

%define yast_dir %{_prefix}/share/YaST2

%files
%defattr(-,root,root)
%{yast_dir}/clients/*.rb
%{yast_dir}/modules/*.rb
%{yast_dir}/schema/autoyast/rnc/*.rnc
%{yast_dir}/lib/services-manager/*.rb
%dir %{yast_dir}/lib/
%{yast_dir}/lib/services-manager/
%{_prefix}/share/applications/YaST2/services-manager.desktop

%dir %_docdir/
%_docdir/%name/
%_docdir/%name/COPYING
