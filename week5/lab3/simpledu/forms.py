from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required, Regexp
from simpledu.models import db, User
from wtforms import ValidationError


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3, 64), Regexp('^[A-Za-z0-9]*$',0,'Usename must have only letters and numbers')])
    email = StringField('Email', validators=[Required(), Length(3,64), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('Confirm password', validators=[Required(), EqualTo('password', message='Password must match!')])
    submit = SubmitField('Submit')

    def validate_username(self, field):
        if field.data.isalnum():
            raise ValidationError('Username must have only letters and numbers')
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already in use.')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3,64)])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me')

    def validate_username(self, field):
        if field.data and not User.query.filter_by(username=field.data).first():
            raise ValidationError('USERNAME not register')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password error')
    submit = SubmitField('Submit')
