# i18n
## =========================================================================
```python
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
```
### ------------------------------------------------------------------------
You can setup the supported languages for your application using the
BABEL_LANGUAGES configuration setting. 

```python
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'de', 'fr', 'pt', 'it']
```

To load the translations for your application, you need to create a directory. The translations are 
stored in .po or .mo files. Flask babel automatically loads the translations folder in your
application root directory. 

say you have french, spanish and english.
you would have a:
    - translations/
        - fr/
            - LC_MESSAGES/
                - messages.po

        - es/
            - LC_MESSAGES/
                - messages.po

        - en/
            - LC_MESSAGES/
                - messages.po

To generate these translation files, you can use the pybabel command line tool.

To translate the text i your application.
In your templates or views, you can use the _() function to mark translatable text.

This is how to use it in a template:
```html
<h1>{{ _('Hello World!') }}</h1>
```
### ------------------------------------------------------------------------
## Locale Inference

Since we now have flask_babel setup we need to infer the correct locale for the user.
Wr can do this based on URL parameter, user settings, request headers, cookies, etc.

### URL parameters
you can setup routes with language codes in the URLs to allow users to switch between languages.

```python
from flask import Flask

@app.route('/<lang_code>/')
def index(lang_code):
    # set the current language based on the url parameter
    babel.locale_selector_func = lambda: lang_code
    return render_template('index.html')
```

### User settings
if you habe user authentication in your application, you can store the preferred language in the user settings and then use it to set the locale

```python
from flask_login import current_user

@babel.localeselector
def get_locale():
    if current_user.is_authenticated:
        # Get the user's preferred language from the profile/settings
        return current_user.language
    else:
        # If the user is not logged in, use the Accept-Language header
        return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])
```

### Request headers
You can also use the Accept-Language header to infer the user's preferred language.

```python
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

```