#!/bin/bash
# ------------------------------------------------------------------
## Author = Navjot Tomer
##
## Description
## Basic script for generating Osclass translations template
##
##

# Delete any previous tmp directory
if [ -d ./tmp ]; then
    ### An existing directory exists delete it ###
    echo 'removing existing tmp directory'
    rm -r ./tmp
fi
###  Make directory ###
mkdir tmp
mkdir tmp/osclass

# Download latest Osclass release from repository
echo 'Downloading latest osclass theme'
(
    cd tmp && curl -s https://api.github.com/repos/mindstellar/Osclass/releases/latest |
        grep 'browser_download_url' |
        head -1 |
        cut -d '"' -f 4 |
        wget -qi - && unzip -qq osclass*.zip -d .
)

#Create Fresh gettext pot file for core
# shellcheck disable=SC2038
find tmp/osclass/oc-admin/ tmp/osclass/oc-includes/osclass/ -type f -name '*.php' |
    xargs xgettext \
        --keyword=__ -k=_e -k=_n:1,2 \
        --language=PHP \
        --output-dir=src/templates \
        --output=core.pot \
        --from-code=utf-8 \
        --msgid-bugs-address=translations@mindstellar.com

echo 'core.pot is created in /src/templates directory'

#Create Fresh gettext pot file for messages
# shellcheck disable=SC2038
find tmp/osclass/oc-admin/ tmp/osclass/oc-includes/osclass/ -type f -name '*.php' |
    xargs xgettext \
        --keyword=_m -k=_mn:1,2 \
        --language=PHP \
        --output-dir=src/templates \
        --output=messages.pot \
        --from-code=utf-8 \
        --msgid-bugs-address=translations@mindstellar.com

echo 'messages.pot is created in /src/templates directory'

#Create Fresh gettext pot file messages
# shellcheck disable=SC2038
find tmp/osclass/oc-content/themes/bender -type f -name '*.php' |
    xargs xgettext \
        --keyword=__ -k=_e -k=_m -k=_mn:1,2 \
        --language=PHP \
        --output-dir=src/templates \
        --output=theme.pot \
        --from-code=utf-8 \
        --msgid-bugs-address=translations@mindstellar.com

echo 'theme.pot is created in /src/templates directory'
echo 'Cleaning temporary files'
cp src/mail.sql src/templates/mail.sql
# Remove temporary files
rm -r ./tmp

echo 'Done'
