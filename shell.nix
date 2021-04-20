with import <nixpkgs> {};
with pkgs.python3Packages;

let
  my-python-packages = python-packages: [
    python-packages.discordpy
    python-packages.python-dotenv
    python-packages.pytz
  ];
  pythonEnv = python3.withPackages my-python-packages;
in
  pkgs.stdenv.mkDerivation {
    name = "chezbot";
    src = null;
    buildInputs = [
      pythonEnv
    ];
  }

