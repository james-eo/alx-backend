# 0x02. i18n

## Project Overview
This project focuses on internationalization (i18n) in Flask applications. It demonstrates how to configure Flask for multiple languages, handle locale inference, and display localized timestamps.

## Learning Objectives
- Parametrize Flask templates to display different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- A `README.md` file at the root of the project is mandatory.
- Code should follow the pycodestyle (version 2.5) style.
- The first line of all files should be `#!/usr/bin/env python3`.
- All `.py` files should be executable.
- All modules, classes, functions, and methods should have proper documentation.
- All functions and coroutines must be type-annotated.

## Installation and Setup
1. **Install Flask and Flask-Babel**:
    ```sh
    $ pip3 install flask flask_babel==2.0.0
    ```

2. **Project Structure**:
    ```
    alx-backend
    └── 0x02-i18n
        ├── 0-app.py
        ├── 1-app.py
        ├── 2-app.py
        ├── 3-app.py
        ├── 4-app.py
        ├── 5-app.py
        ├── 6-app.py
        ├── 7-app.py
        ├── templates
        │   ├── 0-index.html
        │   ├── 1-index.html
        │   ├── 2-index.html
        │   ├── 3-index.html
        │   ├── 4-index.html
        │   ├── 5-index.html
        │   ├── 6-index.html
        │   └── 7-index.html
        ├── translations
        │   ├── en
        │   │   └── LC_MESSAGES
        │   │       ├── messages.po
        │   │       └── messages.mo
        │   ├── fr
        │   │   └── LC_MESSAGES
        │   │       ├── messages.po
        │   │       └── messages.mo
        └── babel.cfg
    ```

## Tasks

### Task 0: Basic Flask App
Create a basic Flask app (`0-app.py`) with a single `/` route and an `index.html` template displaying "Welcome to Holberton" as the page title and "Hello world" as the header.

**Files**:
- `0-app.py`
- `templates/0-index.html`

### Task 1: Basic Babel Setup
Install Flask-Babel and configure it with a `Config` class to support English and French. Set default locale to English and timezone to UTC.

**Files**:
- `1-app.py`
- `templates/1-index.html`

### Task 2: Get Locale from Request
Create a `get_locale` function to determine the best match with supported languages using `request.accept_languages`.

**Files**:
- `2-app.py`
- `templates/2-index.html`

### Task 3: Parametrize Templates
Use `_` or `gettext` to parametrize templates. Create `babel.cfg`, extract messages, initialize translations, and compile dictionaries.

**Files**:
- `3-app.py`
- `babel.cfg`
- `templates/3-index.html`
- `translations/en/LC_MESSAGES/messages.po`
- `translations/fr/LC_MESSAGES/messages.po`

### Task 4: Force Locale with URL Parameter
Modify `get_locale` to detect and use `locale` URL parameter if present and supported.

**Files**:
- `4-app.py`
- `templates/4-index.html`

### Task 5: Mock Logging In
Mock a user login system with a user table and `get_user` function. Use `before_request` to set the user globally and display appropriate messages in templates.

**Files**:
- `5-app.py`
- `templates/5-index.html`

### Task 6: Use User Locale
Update `get_locale` to prioritize locale from URL parameters, user settings, and request headers, in that order.

**Files**:
- `6-app.py`
- `templates/6-index.html`

### Task 7: Infer Appropriate Timezone
Define a `get_timezone` function to determine the appropriate timezone from URL parameters, user settings, or default to UTC. Validate the timezone using `pytz`.

**Files**:
- `7-app.py`
- `templates/7-index.html`

### Task 8: Display the Current Time
Display the current time on the home page based on the inferred timezone.

**Files**:
- `app.py`
- `templates/index.html`
- `translations/en/LC_MESSAGES/messages.po`
- `translations/fr/LC_MESSAGES/messages.po`

## License
This project is licensed under the ALX License.

## Authors
- ALX School

## Acknowledgments
- Flask-Babel documentation
- Flask i18n tutorial
- pytz documentation

