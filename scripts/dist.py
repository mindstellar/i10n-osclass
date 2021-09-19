'''
This script is used to create a list of all translations in the
src/translations/ directory.
'''
# Imports
import os
import json

# current working directory
cwd = os.getcwd()
# Variables
translations_dir = cwd + '/src/translations/'

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
    # Create empty list
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
                        # mail.json relative path
                        translation['mail_json'] = dir + '/mail.json'
                    # Add translation to list
                    translations.append(translation)

                    # Check if md5sum.txt file exists, if exists, read it and get the md5sum
                    if os.path.isfile(translations_dir + dir + '/.md5sum'):
                        with open(translations_dir + dir + '/.md5sum', 'r') as f:
                            md5sum_file = f.read().strip()
                    else:
                        md5sum_file = ''
                    # Calculate the md5sum of all required files
                    md5sum_new = ''
                    for file in required_files:
                        md5sum_new += str(os.path.getsize(translations_dir + dir + '/' + file))
                    # Check if md5sum_file is same as md5sum_new
                    if md5sum_file == md5sum_new:
                        # Skip Zip file creation
                        print('Skipping ' + dir + ' because md5sum is same')
                        continue
                    # Save md5sum_new to md5sum.txt and unset md5sum_new, md5sum_file
                    with open(translations_dir + dir + '/.md5sum', 'w') as f:
                        f.write(md5sum_new)
                        md5sum_new = ''
                        md5sum_file = ''

                    # Now create dist zip file with all .mo, .po and .json files in  root dist
                    print('Creating dist zip file for ' + dir)
                    # Create dist directory if it does not exist
                    if not os.path.isdir('dist'):
                        os.mkdir('dist')
                    # if it has a zip file, remove it
                    if os.path.isfile('dist/' + dir + '.zip'):
                        os.remove('dist/' + dir + '.zip')
                    # Create zip file
                    os.system('zip -r -j dist/' + dir + '.zip ' + translations_dir + dir)
    # Return list of translations                
    return translations
# 
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