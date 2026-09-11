[app]
title = Economicon
package.name = economicon
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
p4a.branch = master
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
