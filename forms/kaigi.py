from wtforms.ext.appengine.db import model_form
from models.kaigi import Kaigi
from base_form import BaseForm

KaigiForm = model_form(Kaigi, base_class=BaseForm)
