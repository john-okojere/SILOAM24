from django.db import models
from django.core.validators import RegexValidator
import uuid
import barcode
from barcode.writer import ImageWriter


phone_regex = RegexValidator(
    regex=r'^\+234\d{10}$|^0\d{10}$',
    message="Phone number must be entered in the format: '+234XXXXXXXXXX' or '0XXXXXXXXXX'."
)
marital = (
    ('Single','Single'),
    ('Married','Married')
)

ages = (
    ('0 - 18', '0 - 18'),
    ('19 - 25', '19 - 25'),
    ('26 - 30', '26 - 30'),
    ('31 - 40', '31 - 40'),
    ('41 - 50', '41 - 50'),
    ('51 - 60', '51 - 60'),
)

accompanies = (
    ('I am coming alone', 'I am coming alone'),
    ('I am coming with children', 'I am coming with children')

)
accomodation_S = (
    ('Yes', 'Yes'),
    ('No', 'No')
)
class Person(models.Model):
    uid = models.UUIDField( default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, 
                              error_messages={'unique': "This email has been used already"})
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=14,
                                    help_text="Do not use already used email"
                                    )
    address = models.TextField()
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    accomodation = models.CharField(max_length=5, choices=accomodation_S)
    are_you_coming_alone = models.CharField(max_length=255,verbose_name="Are you coming alone?", choices=accompanies)
    marital_status = models.CharField(max_length=50, choices=marital)
    age_group = models.CharField(max_length=50, choices=ages)
    date_created = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=10, null=True)

    def barcode(self):
        barcode_format = 'code128'
        data = str(self.uid) 
        barcode_class = barcode.get_barcode_class(barcode_format)
        barcode_instance = barcode_class(data, writer=ImageWriter())

        options = {
            'module_width': 0.2,
            'module_height': 15.0,
            'quiet_zone': 6.5,
            'font_size': 10,
            'text_distance': 5.0,
            'background': 'white',
            'foreground': 'black',
            'write_text': True
        }

        # Save the barcode to a file
        barcode_instance.save(f'media/BARCODE/{self.first_name}_{self.id}',  options=options)

        return f'media/BARCODE/{self.first_name}_{self.id}.png'
    
    def save(self, *args, **kwargs):
        self.barcode()
        if self.accomodation.title() == "Yes":
            self.role = "Camper"
        else:
            self.role = 'Participant'
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
