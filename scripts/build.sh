#!/bin/bash
# ------------------------------------------------------------------
## Author = Navjot Tomer
##
## Description
## Basic script for generating Osclass translations template
##
## Usage:
## ./build.sh
##
# Delete any previous tmp directory if exists and print message
if [ -d "tmp" ]; then
  rm -rf tmp
  echo "Deleted previous tmp directory"
fi
# save root directory to variable ROOT_DIR

ROOT_DIR="../."
# Change directory to root directory
cd $ROOT_DIR
###  Make directory in ROOT_DIR
mkdir tmp
# clone the git@github.com:mindstellar/osclass repo and change directory to it
# get the current branch name
branch=$(git rev-parse --abbrev-ref HEAD)
# change directory to tmp
cd tmp || exit
# clone git@github.com:mindstellar/osclass and checkout same branch name in tmp directory
git clone --branch "$branch" git@github.com:mindstellar/Osclass.git
cd Osclass || exit
#Create Fresh gettext pot file for core
# shellcheck disable=SC2038
find ./oc-admin/ ./oc-includes/osclass/ -type f -name '*.php' |
  xargs xgettext \
    --keyword=__ -k=_e -k=_n:1,2 \
    --language=PHP \
    --output-dir="$ROOT_DIR"/src/templates/ \
    --output=core.pot \
    --from-code=utf-8 \
    --msgid-bugs-address=translations@mindstellar.com
echo 'core.pot is created in /src/templates directory'
#Create Fresh gettext pot file for messages
# shellcheck disable=SC2038
find ./oc-admin/ ./oc-includes/osclass/ -type f -name '*.php' |
  xargs xgettext \
    --keyword=_m -k=_mn:1,2 \
    --language=PHP \
    --output-dir="$ROOT_DIR"/src/templates/ \
    --output=messages.pot \
    --from-code=utf-8 \
    --msgid-bugs-address=translations@mindstellar.com
echo 'messages.pot is created in /src/templates directory'
# clean up Osclass directory safely
cd ..
rm -rf Osclass
# Now clone https://github.com/mindstellar/theme-bender repo and change directory to it
git clone git@github.com:mindstellar/theme-bender.git
cd theme-bender || exit
#Create Fresh gettext pot file for theme-bender
# shellcheck disable=SC2038
find . -type f -name '*.php' |
  xargs xgettext \
    --keyword=__ -k=_e -k=_m -k=_mn:1,2 \
    --language=PHP \
    --output-dir="$ROOT_DIR"/src/templates/ \
    --output=theme.pot \
    --from-code=utf-8 \
    --msgid-bugs-address=translations@mindstellar.com
echo 'theme.pot is created in /src/templates directory'
# clean up theme-bender directory
echo 'Cleaning temporary files'
cd ..
rm -rf theme-bender
# Copy mail.json and locale.json to src/templates directory
echo 'Copying mail.json and locale.json to /src/templates directory'
cp "$ROOT_DIR"/src/locale.json "$ROOT_DIR"/src/templates/
cp "$ROOT_DIR"/src/mail.json "$ROOT_DIR"/src/templates/
# Clean up tmp directory
echo 'Cleaning temporary files'
cd ..
rm -rf tmp
echo 'Done'
# ------------------------------------------------------------------