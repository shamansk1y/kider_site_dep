from django.db import models
from .utils import get_file_name


class Team(models.Model):
    """
    A model representing a team member.

    Fields:
        - name (CharField): The full name of the team member.
        - profession (TextField): The job title or profession of the team member.
        - position (SmallIntegerField): The unique position of the team member within the team.
        - is_visible (BooleanField): Whether the team member should be visible on the website or not.
        - image (ImageField): An optional image of the team member.
        - desc (TextField): A brief description or bio of the team member.
        - image_clas (ImageField): An optional image of the team member's class.
        - twi_url (URLField): The team member's Twitter profile URL.
        - fb_url (URLField): The team member's Facebook profile URL.
        - in_url (URLField): The team member's Instagram profile URL.

    Methods:
        - __str__: Returns the full name of the team member.

    Meta:
        - ordering: Specifies the default ordering for the model's objects.
        - verbose_name_plural: A human-readable plural name for the model in the admin interface.
    """

    name = models.CharField(max_length=50, verbose_name="Повне ім'я")
    profession = models.TextField(max_length=50, verbose_name="Посада")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    desc = models.TextField(max_length=500, verbose_name="Посада", blank=True)
    image_clas = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото клас")
    twi_url = models.URLField(blank=True, verbose_name="Посилання на twitter", default='https://twitter.com/')
    fb_url = models.URLField(blank=True, verbose_name="Посилання на facebook", default='https://www.facebook.com/')
    in_url = models.URLField(blank=True, verbose_name="Посилання на instagram", default='https://www.instagram.com/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Наша команда'


class Slider(models.Model):
    """
    This module contains the Slider model class.
    Slider is model that represents a slide in a website's slider. Each slide
    has a title, image, description, and optional buttons with their respective URLs.

    Fields:
        title (CharField): the title of the slide.
        position (SmallIntegerField): the position of the slide within the slider.
        image (ImageField): the image to display as the slide background.
        is_visible (BooleanField): whether the slide is currently visible.
        h_1 (CharField): the main heading of the slide.
        desc (TextField): the description text of the slide.
        tab_1 (CharField): the label for the first button (optional).
        tab_1_url (URLField): the URL for the first button (optional).
        tab_2 (CharField): the label for the second button (optional).
        tab_2_url (URLField): the URL for the second button (optional).

    Methods:
        str(): returns the string representation of the slide, which is its title.
    """
    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    image = models.ImageField(upload_to=get_file_name, verbose_name="Зображення")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок")
    desc = models.TextField(max_length=500, blank=True, verbose_name="Опис")
    tab_1 = models.CharField(max_length=50, verbose_name="Назва кнопки 1", blank=True)
    tab_1_url = models.URLField(blank=True, verbose_name="Посилання 1")
    tab_2 = models.CharField(max_length=50, verbose_name="Назва кнопки 1", blank=True)
    tab_2_url = models.URLField(blank=True, verbose_name="Посилання 2")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Слайдер'


class About(models.Model):
    """
    A model to store information about the company.

    Fields:
        - h1: CharField, the main heading or title of the About section.
        - desc: TextField, a longer description of the company or organization.
        - tab: CharField, the label or text for a button associated with the About section.
        - user: CharField, the name of the founder or creator of the organization.
        - pos_user: CharField, the position or role of the founder or creator.
        - img_user: ImageField, the photo or image of the founder or creator.
        - is_visible: BooleanField, indicates whether the section is visible on the website or not.
        - img_1: ImageField, an image or photo associated with the company or organization.
        - img_2: ImageField, an image or photo associated with the company or organization.
        - img_3: ImageField, an image or photo associated with the company or organization.

    Methods:
        - __str__(self): returns a string representation of the About instance.

    Meta:
        - ordering: a tuple of strings, indicates the default field or fields to order by.
        - verbose_name_plural: a string, the plural name for the model in the admin interface.
    """
    h1 = models.CharField(max_length=255, verbose_name="Текст заголовка")
    desc = models.TextField(max_length=1000, verbose_name="Опис")
    tab = models.CharField(max_length=55, verbose_name="Текст кнопки")
    user = models.CharField(max_length=55, verbose_name="Ім'я засновника")
    pos_user = models.CharField(max_length=55, verbose_name="Посада")
    img_user = models.ImageField(upload_to=get_file_name, verbose_name="Зображення засновника")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    img_1 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення дитини")
    img_2 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення дитини")
    img_3 = models.ImageField(upload_to=get_file_name, verbose_name="Зображення дитини")

    def __str__(self):
        return f'{self.h1}'

    class Meta:
        ordering = ('h1',)
        verbose_name_plural = 'Ми про нас'


class Testimonial(models.Model):
    """
    Defines a Testimonial model class for storing testimonials in the database.

    Fields:
        - name: The name of the person giving the testimonial (CharField).
        - profession: The profession of the person giving the testimonial (TextField).
        - position: The position of the testimonial in the list of testimonials (SmallIntegerField, unique).
        - is_visible: Indicates whether the testimonial is visible on the site or not (BooleanField).
        - image: An optional image of the person giving the testimonial (ImageField).
        - desc: The testimonial itself (TextField).

    Methods:
        - __str__(): Returns the name of the person giving the testimonial.

    Meta:
        - ordering: Specifies the default ordering of the testimonials by their position field.
        - verbose_name_plural: Specifies the plural name of the Testimonial model class.
    """

    name = models.CharField(max_length=50, verbose_name="Повне ім'я")
    profession = models.TextField(max_length=50, verbose_name="Посада")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    desc = models.TextField(max_length=500, verbose_name="Текст", blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Відгуки'


class Classes(models.Model):
    """
        The Classes model defines the attributes and methods of the classes offered by the organization.

    Fields:
        - title (CharField): the name of the class.
        - price (DecimalField): the price of the class.
        - image (ImageField): an image representing the class.
        - position (SmallIntegerField): the position of the class in the list of classes.
        - is_visible (BooleanField): whether the class is visible on the website or not.
        - teacher (ForeignKey): the teacher of the class, a reference to the Team model.
        - age (CharField): the age range for the class.
        - time (CharField): the time when the class starts.
        - capacity (CharField): the maximum number of students in the class.

    Methods:
        - __str__(self): returns the string representation of the class, which is the title.

    Meta:
        - ordering (tuple): specifies the order in which classes are displayed on the website, based on the position attribute.
        - verbose_name_plural (str): the plural name of the model, used in the admin interface.
    """
    title = models.CharField(max_length=50, verbose_name="Назва")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Фото")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    teacher = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='teacher')
    age = models.CharField(max_length=50, verbose_name="Вік", default='3-5 Years')
    time = models.CharField(max_length=50, verbose_name="Час початку занять", default='9-10 AM')
    capacity = models.CharField(max_length=50, verbose_name="Кількість в групі", default='30 Kids')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Класи'

class Facilities(models.Model):
    """
    This is a model class named Facilities that represents school facilities with four columns of headings and descriptions. The columns are represented by the h1_col_x and desc_col_x fields where x is a digit from 1 to 4. The position field is used to order the facilities and ensure uniqueness, and the is_visible field indicates whether the facilities should be visible or not.

    Fields:
        - h1_col_1: CharField with max length of 50 characters for the title of column 1
        - desc_col_1: TextField with max length of 255 characters for the description of column 1
        - h1_col_2: CharField with max length of 50 characters for the title of column 2
        - desc_col_2: TextField with max length of 255 characters for the description of column 2
        - h1_col_3: CharField with max length of 50 characters for the title of column 3
        - desc_col_3: TextField with max length of 255 characters for the description of column 3
        - h1_col_4: CharField with max length of 50 characters for the title of column 4
        - desc_col_4: TextField with max length of 255 characters for the description of column 4
        - position: SmallIntegerField used to order the facilities and ensure uniqueness
        - is_visible: BooleanField to indicate whether the facilities should be visible or not

    Meta:
        - ordering: a tuple of strings indicating how the facilities should be ordered
        - verbose_name_plural: a string indicating the plural name of this model class for better readability in Django's admin interface.
        """
    h1_col_1 = models.CharField(max_length=50, verbose_name="Назва колонка №1")
    desc_col_1 = models.TextField(max_length=255, verbose_name="Опис колонка №1")
    h1_col_2 = models.CharField(max_length=50, verbose_name="Назва колонка №2")
    desc_col_2 = models.TextField(max_length=255, verbose_name="Опис колонка №2")
    h1_col_3 = models.CharField(max_length=50, verbose_name="Назва колонка №3")
    desc_col_3 = models.TextField(max_length=255, verbose_name="Опис колонка №3")
    h1_col_4 = models.CharField(max_length=50, verbose_name="Назва колонка №4")
    desc_col_4 = models.TextField(max_length=255, verbose_name="Опис колонка №4")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Шкільні зручності'

class Call(models.Model):
    """
    The Call model represents a call to action on a website.

    Fields:
        - title (CharField): the title of the call to action.
        - desc (TextField): the description of the call to action, with a maximum length of 500 characters (optional).
        - image (ImageField): an image associated with the call to action (optional).
        - position (SmallIntegerField): the position of the call to action on the page, with a unique constraint.
        - is_visible (BooleanField): a flag indicating whether the call to action should be visible on the page by default.
        - tab_1 (CharField): the label of the button associated with the call to action (optional).
        - tab_1_url (URLField): the URL to which the button associated with the call to action should link (optional).

    Methods:
        - __str__(self): returns the string representation of the call to action, which is the title.

    Meta:
        - ordering: specifies the default ordering of calls to action by their position.
        - verbose_name_plural: the plural name of the model in the admin interface.
    """
    title = models.CharField(max_length=50, verbose_name="Заговок")
    desc = models.TextField(max_length=500, verbose_name="Текст", blank=True)
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Зображення")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    tab_1 = models.CharField(max_length=50, verbose_name="Текст кнопки", blank=True)
    tab_1_url = models.URLField(blank=True, verbose_name="Посилання")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Заклик'

class Gallery(models.Model):
    """
    Model representing an image in a gallery in footer.

    Fields:
        - image (django.db.models.ImageField): The image file uploaded for the gallery.
        - position (django.db.models.SmallIntegerField): The position of the image in the gallery.
        - is_visible (django.db.models.BooleanField): Whether the image is visible in the gallery.

    Meta:
        - ordering (tuple): A tuple of fields to use when ordering the gallery images (in ascending order).
        - verbose_name (str): The singular name of the model for display in the Django admin.
        - verbose_name_plural (str): The plural name of the model for display in the Django admin.
    """
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Зображення")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")

    class Meta:
        ordering = ('position',)
        verbose_name = 'Фото'
        verbose_name_plural = 'Галерея'

class Contacts(models.Model):
    """
    Model representing the contact details of an organization.

    Fields:
    h1 (str): The main heading of the contact page.
    address (str): The physical address of the organization.
    phone (str): The phone number of the organization.
    email (str): The email address of the organization.
    twi_url (str, optional): The URL of the organization's Twitter page. Defaults to blank.
    fb_url (str, optional): The URL of the organization's Facebook page. Defaults to blank.
    youtube_url (str, optional): The URL of the organization's YouTube channel. Defaults to blank.
    in_url (str, optional): The URL of the organization's LinkedIn page. Defaults to blank.
    """
    h1 = models.CharField(max_length=50, verbose_name="Заговок")
    address = models.CharField(max_length=50, verbose_name="Адреса")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.CharField(max_length=50, verbose_name="Пошта")
    twi_url = models.URLField(blank=True, verbose_name="Посилання на twitter")
    fb_url = models.URLField(blank=True, verbose_name="Посилання на facebook")
    youtube_url = models.URLField(blank=True, verbose_name="Посилання на youtube")
    in_url = models.URLField(blank=True, verbose_name="Посилання на LinkedIn")

    class Meta:
        ordering = ('h1',)
        verbose_name = 'Контакт'
        verbose_name_plural = 'Наші контакти'

class Appointment(models.Model):
    """
    Represents an appointment request made by a user.

    Fields:
        -  name (str): The name of the user making the appointment.
        - email (str): The email address of the user making the appointment.
        - child_name (str): The name of the child for whom the appointment is requested.
        - child_age (int): The age of the child for whom the appointment is requested.
        - message (str): An optional message from the user.
        - date (datetime.date): The date and time when the appointment was made.
        - date_processing (datetime.date): The date and time when the appointment was last processed.
        - is_processed (bool): Whether the appointment has been processed or not.

    Methods:
        - __str__(): Returns a string representation of the appointment, consisting of the name and email address of the user.

    Meta:
        - ordering: Specifies the default ordering for records in the database table.
        - verbose_name_plural: Specifies the display name for the model in the admin interface.
    """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    child_name = models.CharField(max_length=50)
    child_age = models.SmallIntegerField()
    message = models.TextField(max_length=250, blank=True)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Призначити зустріч'


class Subscription(models.Model):
    """
    The Subscription model represents an email subscription.

    Fields:
        - email: An EmailField representing the email address of the subscriber.
        - date: A DateField representing the date the subscription was made.
        auto_now_add=True is set to automatically set the date to the current date when the subscription is created.
        - date_processing: A DateField representing the date the subscription was last processed.
        auto_now=True is set to automatically update the date to the current date whenever the subscription is updated.
        - is_processed: A BooleanField representing whether the subscription has been processed or not.
        The default value is False.

    Methods:
        - str(self): A special method that returns a string representation of the object.
        In this case, it returns the date and email address of the subscriber.

    Meta:
        - ordering: A tuple indicating the default ordering for the model.
        In this case, the default ordering is by the date in descending order (i.e. latest subscriptions first).
        - verbose_name_plural: A string representing the human-readable plural name for the model.
        In this case, it is "Підписка на email розсилку".
    """
    email = models.EmailField()
    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Підписка на email розсилку'


class ContactUs(models.Model):
    """
    Defines a model `ContactUs` that represents a contact form submission.

    Fields:
        - name: a CharField representing the name of the person submitting the form
        - email: an EmailField representing the email address of the person submitting the form
        - message: a TextField representing the message the person submitting the form wants to convey
        - subject: a CharField representing the subject of the message
        - date: a DateField representing the date when the form was submitted
        - date_processing: a DateField representing the date when the form was processed
        - is_processed: a BooleanField representing whether the form has been processed or not

    Methods:
        - __str__: returns a string representation of the model instance

    Meta:
        - ordering: a tuple that specifies the default ordering for instances of the model
        - verbose_name_plural: a string that specifies the plural name for the model in the admin interface
    """

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=250, blank=True)
    subject = models.CharField(max_length=50)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Зворотній зв'язок"


class Headlines(models.Model):
    """
    Defines a  model called Headlines that represents headlines and corresponding description text for various aspects of an educational institution.

    Fields:
        - title_facilities: CharField with a maximum length of 50 and verbose name "Заговок facilities".
        - desc_facilities: TextField with a maximum length of 500 and verbose name "Текст facilities". Optional and can be blank.
        - title_classes: CharField with a maximum length of 50 and verbose name "Заговок classes".
        - desc_classes: TextField with a maximum length of 500 and verbose name "Текст classes". Optional and can be blank.
        - title_teachers: CharField with a maximum length of 50 and verbose name "Заговок teachers".
        - desc_teachers: TextField with a maximum length of 500 and verbose name "Текст teachers". Optional and can be blank.
        - title_testimonial: CharField with a maximum length of 50 and verbose name "Заговок testimonial".
        - desc_testimonial: TextField with a maximum length of 500 and verbose name "Текст testimonial". Optional and can be blank.

    Methods:
        - __str__: Returns the title_facilities field as a string.

    Meta:
        - verbose_name_plural: The plural name of the model, set to "Заголовки".
    """

    title_facilities = models.CharField(max_length=50, verbose_name="Заговок facilities")
    desc_facilities = models.TextField(max_length=500, verbose_name="Текст facilities", blank=True)
    title_classes = models.CharField(max_length=50, verbose_name="Заговок classes")
    desc_classes = models.TextField(max_length=500, verbose_name="Текст classes ", blank=True)
    title_teachers = models.CharField(max_length=50, verbose_name="Заговок teachers")
    desc_teachers = models.TextField(max_length=500, verbose_name="Текст teachers", blank=True)
    title_testimonial = models.CharField(max_length=50, verbose_name="Заговок testimonial")
    desc_testimonial = models.TextField(max_length=500, verbose_name="Текст testimonial", blank=True)
    def __str__(self):
        return f'{self.title_facilities}'

    class Meta:
        verbose_name_plural = "Заголовки"



class Schedule(models.Model):
    """
    Defines a model called Schedule that represents a schedule item with a title, description,
    image, position, and visibility flag.

    Fields:
        - title: CharField with a maximum length of 50 and verbose name "Заговок".
        - desc: TextField with a maximum length of 500 and verbose name "Текст". Optional and can be blank.
        - image: ImageField that uploads files to a directory specified by the get_file_name function (not shown).
        Optional and can be blank.
        - position: SmallIntegerField with a unique constraint and verbose name "Позиція".
        - is_visible: BooleanField with a default value of True and verbose name "Видимість".

    Methods:
     - __str__: Returns the title field as a string.

    Meta:
        - ordering: A tuple containing the field name to use for ordering the model instances.
        Here, it is set to 'position'.
        - verbose_name_plural: The plural name of the model, set to 'Розклад занять'.
    """

    title = models.CharField(max_length=50, verbose_name="Заговок")
    desc = models.TextField(max_length=500, verbose_name="Текст", blank=True)
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name="Зображення")
    position = models.SmallIntegerField(unique=True, verbose_name="Позиція")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")


    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Розклад занять'


