import wtforms as forms
from wtforms import validators

from forms.forms import BaseForm

class Setup(BaseForm):
	name = forms.TextField('Name', validators=[validators.required])
	description = form.TextField('Description')
