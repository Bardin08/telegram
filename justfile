_default:
  @just --list

build:
  whiskers templates/android.tera
  whiskers templates/desktop.tera
  whiskers templates/ios.tera
  whiskers templates/macos.tera

check:
  whiskers templates/android.tera --check
  whiskers templates/desktop.tera --check
  whiskers templates/ios.tera --check
  whiskers templates/macos.tera --check
