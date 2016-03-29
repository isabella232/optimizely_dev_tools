#!/usr/bin/env sh

# must be run from root of repo
. ~/.nvm/nvm.sh
nvm use
npm install
grunt test --path=$1
