#!/usr/bin/env sh

DOWNLOAD_DIR=svg-sets

mkdir -p "$DOWNLOAD_DIR"

# noto-emoji
wget https://github.com/googlefonts/noto-emoji/archive/refs/heads/main.zip -O "$DOWNLOAD_DIR/noto-emoji-main.zip"

# twemoji
wget https://github.com/eosrei/twemoji-color-font/archive/refs/heads/master.zip -O "$DOWNLOAD_DIR/twemoji-color-font-master.zip"

# openmoji
wget https://github.com/hfg-gmuend/openmoji/releases/latest/download/openmoji-svg-color.zip  -P "$DOWNLOAD_DIR"
