import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def validate_contact(value):
    # RegexValidator(regex=r'08[0-9]{9,10}$', message='Phone number must be entered in the format: 08xx xxxx xxxx. 11 to 12 digits allowed.')
    __validate = re.compile(r'08[0-9]{9,10}$')
    if not __validate.match(value):
        raise ValidationError('Phone numbers must be entered in the format: 08xx xxxx xxxx. up to 11 or 12 digits allowed.')