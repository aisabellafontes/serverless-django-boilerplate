#!/usr/bin/env python
import os
import sys

def handler(event, context):
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(['manage.py', 'shell', '-c', "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')"])

    return { 
        'Request ID:': context.aws_request_id,
    } 