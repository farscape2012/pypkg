#!/usr/bin/env bash
# author : Chengyu Liu

# Exit immediately if a command exits with a non-zero status.
set -euo pipefail

VirtEnv="$1"/.virtualenv/

virtualenv "$VirtEnv"

source "$VirtEnv/bin/activate"
pip --disable-pip-version-check install --upgrade --requirement ./pypa-requirement > pip-install.log

#pip freeze
#exec  python main.py "$@"
#deactivate

