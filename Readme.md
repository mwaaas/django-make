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

  optionally, define your `settings.STAGE` environment

  ``` STAGE_ENV_VAR = 'ENV' ```

  and then run as,

    $ ENV=development ./manage.py runserver

Licence
---

MIT