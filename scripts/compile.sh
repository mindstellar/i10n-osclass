#!/bin/bash
# compile po files to mo files
# Find all .po files and compile them
echo "Compiling .po files to .mo files"
find src/translations/* -name \*.po \
    -print -execdir sh -c 'msgfmt -f -o "$(basename "$0" .po).mo" "$0"' '{}' \;
echo "Done"
# Path: scripts/compile.sh
