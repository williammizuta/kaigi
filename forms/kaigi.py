from wtforms.ext.appengine.db import model_form
from models.kaigi import Kaigi
from base_form import BaseForm
from i18n_converter import I18nConverter

def kaigi_form(handler):
    return model_form(Kaigi, base_class=BaseForm, converter=I18nConverter(handler.locale))(handler=handler)
