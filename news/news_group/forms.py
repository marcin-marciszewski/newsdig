from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[DataRequired()])
    submit_comment = SubmitField('Submit')


class LikesForm(FlaskForm):
    submit_like = SubmitField('Like')


class DislikesForm(FlaskForm):
    submit_dislike = SubmitField('Dislike')
