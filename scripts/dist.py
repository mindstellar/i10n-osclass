'''
This script is used to create a list of all translations in the
src/translations/ directory.
'''
# Imports
import os
import json

# Variables
translations_dir = '../src/translations/'

# Functions
def get_translations():
    '''
    This function search all directories in the translations_dir for locale.json files.
    Read each locale.json and create data list of all translations.
    Example locale.json file:
    {
        "locale_code": "en_US",
        "name": "English (US)",
        "short_name": "English",
        "description": "American english translation",
        "version": "1.0.0",
        "author_name": "navjottomer",
        "author_url": "https:\/\/github.com\/navjottomer",
        "currency_format": "{NUMBER} {CURRENCY}",
        "date_format": "m\/d\/Y",
        "direction": "ltr",
        "stop_words": ""
    }
    '''
    translations = []
    for dir in os.listdir(translations_dir):
        if os.path.isdir(translations_dir + dir):
            if os.path.isfile(translations_dir + dir + '/locale.json'):
                # Now check if this directory has all the required files
                # If not, skip it
                # Required files:
                #   locale.json,theme.mo,theme.po,core.mo,core.po,messages.po,messages.mo,mail.json
                # Check Required Files
                required_files = ['locale.json', 'theme.mo', 'theme.po', 'core.mo', 'core.po', 'messages.mo', 'messages.po', 'mail.json']
                for file in required_files:
                    if not os.path.isfile(translations_dir + dir + '/' + file):
                        print('Skipping ' + dir + ' because it is missing ' + file)
                        break
                else:
                    # All required files are present
                    # Read locale.json
                    with open(translations_dir + dir + '/locale.json') as f:
                        translation = json.load(f)
                        # Add maile.json path to translation
                        translation['mail_json'] = translations_dir + dir + '/mail.json'
                    # Add translation to list
                    translations.append(translation)
                    # Now create dist zip file with all .mo, .po and .json files in  root dist
                    print('Creating dist zip file for ' + dir)
                    # Create dist directory if it does not exist
                    if not os.path.isdir('dist'):
                        os.mkdir('dist')
                    # if it has a zip file, remove it
                    if os.path.isfile('dist/' + dir + '.zip'):
                        os.remove('dist/' + dir + '.zip')
                    # Create zip file
                    os.system('zip -r dist/' + dir + '.zip ' + translations_dir + dir)
    # Return list of translations                
    return translations

# Remove old locale_list.json if it exists
if os.path.isfile('locale_list.json'):
    os.remove('locale_list.json')
# Sort the list by name, remove duplicates and save it as locale_list.json
print('Saving locale_list.json...')
with open('locale_list.json', 'w') as f:
    json.dump(sorted(get_translations(), key=lambda k: k['name']), f, indent=4)
print('Done!')

# Print success message
print('Successfully created locale_list.json')