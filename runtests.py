#!/usr/bin/env python
import sys

try:
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="interests.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "popolo",
            "interests",
        ],
        SITE_ID=1,
        NOSE_ARGS=['-s'],
        MIDDLEWARE_CLASSES=(),
        #LOGGING
        LOGGING = {'version': 1,
                   'disable_existing_loggers': True,
                   'formatters': {'simple': {'format': '%(asctime)s %(levelname)s %(message)s'}},
                   'handlers': {'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'},
                                'null': {'level': 'DEBUG',
                                         'class': 'logging.NullHandler',
                                         },
                                },
                   'loggers': {'django.db.backends': {'level': 'DEBUG', 'handlers': ['null'], 'propagate': False}}
                   },
        #END LOGGING
    )

    try:
        import django
        setup = django.setup
    except AttributeError:
        pass
    else:
        setup()

    from django_nose import NoseTestSuiteRunner
except ImportError:
    import traceback
    traceback.print_exc()
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    test_runner = NoseTestSuiteRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    run_tests(*sys.argv[1:])
