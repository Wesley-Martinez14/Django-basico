from jinja2 import Environment as BaseEnvironment
from django.templatetags.static import static
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage

class Environment(BaseEnvironment):
    def __init__(self, **kwargs):
        kwargs['extensions'] = ['jinja2.ext.i18n']
        super().__init__(**kwargs)
        self.globals.update({
            'static': static,
            'url': reverse,
        })