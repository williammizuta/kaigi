from wtforms import *
from wtforms.validators import *

from django.utils.datastructures import MultiValueDict


class TornadoWTFTranslator:
    def __init__(self, locale_obj):
        self.locale_obj = locale_obj

    def gettext(self, string):
        return self.locale_obj.translate(string)

    def ngettext(self, singular, plural, n):
        return self.locale_obj.translate(singular,
                plural_message=plural, count=n)


class BaseForm(Form):
    def __init__(self, handler=None, obj=None, prefix='', formdata=None, **kwargs):
        if handler:
            self.translate_obj = TornadoWTFTranslator(handler.locale)
            formdata = MultiValueDict()
            for name in handler.request.arguments.keys():
                formdata.setlist(name, handler.get_arguments(name))
        Form.__init__(self, formdata, obj=obj, prefix=prefix, **kwargs)

    def _get_translations(self):
        return self.translate_obj

    def get_data(self):
        return self.data
