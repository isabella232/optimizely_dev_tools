#!/usr/bin/env sh

if [ ! -f ~/.nvm/nvm.sh ]; then
  curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.0/install.sh | bash
fi
. ~/.nvm/nvm.sh
nvm use
npm install
grunt test --path=$1
