from wtforms.widgets import Input
from wtforms import Field, DateTimeField, widgets

class TagListField(Field):
    widget = widgets.TextInput()

    def __init__(self, label=None, validators=None, **kwargs):
        super(TagListField, self).__init__(label, validators, **kwargs)

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []

class DateTimeInput(Input):
    input_type = 'datetime-local'

class HTML5DateTimeField(DateTimeField):
    widget = DateTimeInput()
