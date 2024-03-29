from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Email, DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()] )
    message = TextAreaField('Message', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

