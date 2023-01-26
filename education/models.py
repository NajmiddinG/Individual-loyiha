from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Course(models.Model):
    name = models.CharField(_("Kurs nomi"), max_length=50)
    image = models.ImageField(_("Rasm"), upload_to='images/courses/')
    finish = models.CharField(_("Kurs davomiyligi"), max_length=100)
    duration = models.CharField(_("Kurs necha soat o'tilishligi"), max_length=100)
    day = models.CharField(_("Kurs haftasiga nech kun bo'lishi"), max_length=100)
    requirement = models.CharField(_("O'quvchining minimall bilimi"), max_length=100)
    level = models.CharField(_("O'quvchi kursni tugatib qanday darajaga ega bo'lishi"), max_length=100)
    language = models.CharField(_("Dars qanday tilda o'tilishi"), max_length=100)
    price = models.IntegerField(_("Kurs narxi (so'm)"), default=100000)
    date = models.DateTimeField(_("Yaratilgan vaqt"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("O'quv kurs")
        verbose_name_plural = _("1-O'quv kurslari")


class Teacher(models.Model):
    name = models.CharField(_("O'qituvchi ismi"), max_length=50)
    science = models.CharField(_("O'qituvchining dars o'tish fani"), max_length=50)
    image = models.ImageField(_("O'qituvchining rasmi"), upload_to='images/teachers/')
    telegram = models.URLField(_("Telegram"), max_length=200, null=True, blank=True)
    facebook = models.URLField(_("Facebook"), max_length=200, null=True, blank=True)
    linkedin = models.URLField(_("LinkedIn"), max_length=200, null=True, blank=True)
    instagram = models.URLField(_("Instagram"), max_length=200, null=True, blank=True)
    youtube = models.URLField(_("YouTube"), max_length=200, null=True, blank=True)
    date = models.DateTimeField(_("Qo'shilgan vaqti"), auto_now_add=True)

    class Meta:
        verbose_name = _("O'qituvchi")
        verbose_name_plural = _("2-O'qituvchilar")

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(_("Ismi"), max_length=50)
    phone = PhoneNumberField(_("Telefoni"), max_length=50)
    subject = models.CharField(_("Sarlavxasi"), max_length=50)
    message = models.CharField(_("Xabar matni"), max_length=50)
    date = models.DateTimeField(_("Yuborilgan vaqti"), auto_now_add=True)

    class Meta:
        verbose_name = _("Xabar yuborgan odam")
        verbose_name_plural = _("3-Xabarlar")

    def __str__(self):
        return self.name


class Qoshilish(models.Model):
    name = models.CharField(_("Ismi"), max_length=50)
    phone = PhoneNumberField(_("Telefoni"), max_length=50)
    course = models.ForeignKey(Course, verbose_name=_("Kurs nomi"), on_delete=models.CASCADE)
    date = models.DateTimeField(_("Yuborilgan vaqti"), auto_now_add=True)

    class Meta:
        verbose_name = _("Kursga yozilish xabari")
        verbose_name_plural = _("4-Kursga yozilish xabarlari")

    def __str__(self):
        return self.name