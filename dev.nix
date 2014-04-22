{ }:

let
  pkgs = import <nixpkgs> { };
in

with pkgs;

buildEnv {
  name = "plone-coredev";
  paths = [
    python27
    python27Packages.recursivePthLoader
    python27Packages.virtualenv
    python27Packages.zc_buildout_nix
    python27Packages.pillow
    python27Packages."lxml-2.3.6"
  ] ++ lib.attrValues python27.modules;
}
