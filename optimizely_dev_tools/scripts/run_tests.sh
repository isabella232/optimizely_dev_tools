#!/usr/bin/env sh

. ~/.nvm/nvm.sh
nvm use
npm install
grunt test --path=$1
