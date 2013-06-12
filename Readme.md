Install
---

    $ pip install django-make

Configure settings
---

```

  # settings.py

  MIDDLEWARE_CLASSES = (
    ...
    'django_make.Make'
  )

```

Use
---

    $ STAGE=development ./manage.py runserver

  optionally, redefine your `settings.STAGE` setting

  ``` STAGE_ENV_VAR = 'ENV' ```

  and then boot app as,

    $ ENV=development ./manage.py runserver

Licence
---

MIT