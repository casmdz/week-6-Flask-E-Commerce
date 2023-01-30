from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class AddToCartForm(FlaskForm):
    quantity = IntegerField('Quantity')
    submit = SubmitField('Add to Cart')

class RemoveFromCartForm(FlaskForm):
    submit = SubmitField('Remove from Cart')

# class PostForm(FlaskForm):
#     title = StringField("Title", validators = [DataRequired()])
#     img_url = StringField("Image URL", validators = [DataRequired()])
#     caption = StringField("Caption", validators = [])
    
#     submit = SubmitField()

# class SearchForm(FlaskForm):
#     shoha = StringField('ANYTHING CAN GO HERE', validators=[DataRequired()])