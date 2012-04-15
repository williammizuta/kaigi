from wtforms.ext.appengine.db import model_form
from models.meeting import Meeting
from base_form import BaseForm
from i18n_converter import I18nConverter

def meeting_form(handler):
    # TODO make it show the date and the tags
    return model_form(Meeting, base_class=BaseForm, converter=I18nConverter(handler.locale))(handler=handler)
