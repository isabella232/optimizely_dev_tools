#!/usr/bin/env sh

. ~/.nvm/nvm.sh
nvm install 0.12.5
npm install
grunt test --path=$1
