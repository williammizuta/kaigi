from wtforms.ext.appengine.db import ModelConverter
from wtforms import validators, fields as f

class I18nConverter(ModelConverter):
    def __init__(self, locale_obj):
        self.locale_obj = locale_obj
        super(I18nConverter, self).__init__()

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

