import wtforms
from wtforms import validators

from forms import BaseForm

class Setup(BaseForm):
    name = wtforms.TextField('Name', validators=[validators.required])
    description = wtforms.TextField('Description')
