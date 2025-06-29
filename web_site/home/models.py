from django.db import models
from django.forms import ModelForm,TextInput,Textarea
# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    status = models.BooleanField()
    craete_at= models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
llist =Language.objects.all()
list1 = []

for rs in llist:
    list1.append((rs.code, rs.name))
langlist = (list1)

class Setting(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    smtp_server = models.CharField(max_length=255)
    smtp_email = models.CharField(max_length=255)
    smtp_password = models.CharField(max_length=255)
    smtp_port = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='setting/')
    aboutus = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.title

class SettingLang(models.Model):
    seting =models.ForeignKey(Setting, on_delete=models.CASCADE)
    lang= models.CharField(max_length=6, choices=langlist)
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    smtp_server = models.CharField(max_length=255)
    smtp_email = models.CharField(max_length=255)
    smtp_password = models.CharField(max_length=255)
    smtp_port = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='setting/')
    aboutus = models.TextField()
    contact = models.TextField()

    def __str__(self):
        return self.title
class ContactMessage(models.Model):
    STATUS = (
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed'),
    )
    name =models.CharField(blank=True,max_length=20)
    phone =models.CharField(blank=True, max_length=50)
    subject= models.CharField(blank=True, max_length=50)
    message=models.TextField(blank=True, max_length=225)
    status= models.CharField( max_length=10,choices=STATUS,default='New')
    ip =models.CharField(blank=True, max_length=20)
    note=models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','phone','subject','message']
        widgets ={
            'name': TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class':'input','placeholder':'Subject'}),
            'phone':TextInput(attrs={'class':'input','placeholder':'Phone Number'}),
            'message':TextInput(attrs={'class':'input','placeholder':'Your message','rows':5}),

        }
