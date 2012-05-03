from wtforms.ext.appengine.db import model_form
from models.meeting import Meeting
from base_form import BaseForm
from i18n_converter import I18nConverter

def new_meeting_form(handler):
    # TODO make it show the date and the tags
    return model_form(Meeting, exclude=('minute'), base_class=BaseForm, converter=I18nConverter(handler.locale), field_args={
                'day': {
                    'label': handler.locale.translate('When?')
                }
            })(handler=handler)
