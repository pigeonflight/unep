#!/bin/sh
#
# Shell script to manage .po files.
#
# http://docs.plone.org/develop/plone/i18n/internationalisation.html#managing-po-files
#

# Assume the product name is the current folder name
CURRENT_PATH=`pwd`
CATALOGNAME="unep"

# List of languages
LANGUAGES="en es fr"

# Create locales folder structure for languages
install -d locales
for lang in $LANGUAGES; do
    install -d locales/$lang/LC_MESSAGES
done

# Assume i18ndude is installed with buildout
I18NDUDE=../../bin/i18ndude


# Compile po files
for lang in $(find locales -mindepth 1 -maxdepth 1 -type d); do

    if test -d $lang/LC_MESSAGES; then

        PO=$lang/LC_MESSAGES/${CATALOGNAME}.po

        # Create po file if not exists
        touch $PO

        # Sync po file
        echo "Syncing $PO"
        $I18NDUDE sync --pot locales/$CATALOGNAME.pot $PO

    fi
done
