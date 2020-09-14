#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thedirectory.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
# ALLOWED_HOSTS='127.0.0.1:8000,localhost,.herokuapp.com'

# CLOUDINARY_URL=cloudinary://917812857873495:uhUhM4nnLbD-87cede7FPEeH798@dhs0sdngt

# CLOUD_NAME = dhs0sdngt
# API_KEY = 917812857873495
# API_SECRET = uhUhM4nnLbD-87cede7FPEeH798
# CLOUDINARY_URL=cloudinary://917812857873495:uhUhM4nnLbD-87cede7FPEeH798@dhs0sdngt