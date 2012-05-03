from wtforms.ext.appengine.db import ModelConverter
from wtforms import validators, fields as f

from forms.custom_fields import HTML5DateTimeField, TagListField

def convert_DateTimeProperty_with_html5(model, prop, kwargs):
    return HTML5DateTimeField(**kwargs)

def convert_ListProperty(model, prop, kwargs):
    return TagListField(**kwargs)

class I18nConverter(ModelConverter):
    def __init__(self, locale_obj):
        self.locale_obj = locale_obj
        super(I18nConverter, self).__init__()
        self.converters['DateTimeProperty'] = convert_DateTimeProperty_with_html5
        self.converters['ListProperty'] = convert_ListProperty

    def convert(self, model, prop, field_args):
        prop_type_name = type(prop).__name__
        kwargs = {
                'label': self.locale_obj.translate(prop.name.replace('_', ' ').title()),
                'default': prop.default_value(),
                'validators': [],
                }
        if field_args:
            kwargs.update(field_args)

        if prop.required and prop_type_name not in self.NO_AUTO_REQUIRED:
            kwargs['validators'].append(validators.required())

        if prop.choices:
            # Use choices in a select field.
            kwargs['choices'] = [(v, v) for v in prop.choices]
            return f.SelectField(**kwargs)
        else:
            converter = self.converters.get(prop_type_name, None)
            if converter is not None:
                return converter(model, prop, kwargs)

