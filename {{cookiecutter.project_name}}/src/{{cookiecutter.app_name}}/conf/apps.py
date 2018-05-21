#!/usr/bin/python
# -*- coding: utf-8 -*-   
#
#  apps.py
#  
#
#  Created by {{ cookiecutter.full_name }} using cookiecutter.
#  Copyright (c) {{ cookiecutter.project_name }}. All rights reserved.
#

from __future__ import absolute_import

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MyAppConfig(AppConfig):
    name = '{{ cookiecutter.app_name }}'
    verbose_name = _("{{ cookiecutter.app_name }} service")