# Osclass localization project 
[![Crowdin](https://badges.crowdin.net/osclass-v2/localized.svg)](https://crowdin.com/project/osclass-v2)
 
##i10n-osclass
___
## Contributing

### Translations

Template files are generated using osclass the latest release and maintained in this repository
and used as default for English(US) language, for other language translations we use 
[Crowdin](https://crowdin.com/). 

If you would like to contribute to one of the translations you can invite yourself to the Crowdin
Project [here](https://translate.mindstellar.com/project/osclass-v2/invite).

Changes made on osclass repository will be used to generate template files `src/templates` sent 
to Crowdin which will notify translators of any changes. When translations are completed, they will be
built and sent back to this repository. There's a short delay, but if any part of this
process does not happen, please open an issue.

Once you set up your account on Crowdin you should be taken to
[this page](https://translate.mindstellar.com/project/osclass-v2).

Click on the language you would like to contribute
There you'll see core.po, messages.po,theme.po,local.json and mail.json
 
* `core.po` file includes translations strings for osclass core 
* `messages.po` file includes alert messages translations.
* `theme.po` file includes translations for default frontend theme.
* `mail.json` file includes translations for email templates.
* `local.json` file include important information about current language i.e. locale_code, name, date_format, 
  currency format, version etc. example content is like below json data.
```json 
"locale_code": "en_US",
    "name": "English (US)",
    "short_name": "English",
    "description": "American english translation",
    "version": "1.0.0",
    "author_name": "navjottomer",
    "author_url": "https:\/\/github.com\/navjottomer",
    "currency_format": "{NUMBER} {CURRENCY}",
    "date_format": "m\/d\/Y",
    "stop_words": "i,a,about,an,are,as,at,be,by,com,for,from,how,in,is,it,of,on,or,that,the,this,to,was,what,when,where,who,will,with,the"
 ```
* local.json doesn't need translations, you can change date_format or currency_format if you like.
 
Click any of them, and you will be taken to the translation editor.

Please visit [this page](https://support.crowdin.com/online-editor/) for full crowding online editor documentation

If you ignore the formatting of original string editor will warn you about this, just check your formatting and 
  all good.

## Request new language:
You can make a request by opening a new issue, make sure you provide necessary information like 
language,name, currency_format, date_format, and we will add that language. Once added translators can work on that 
language.
## Building or updating template files with latest Osclass release

Run this command in your bash aware terminal

//TODO//
A workflow to automatically manage this.
```
sh ./.build.sh
```
