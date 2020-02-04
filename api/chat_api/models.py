from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    """
    Message description.

    Attributes:
        sender: User who sent a message
        receiver: User who got a message
        message: Message text
        subject: Subject of the message
        is_read: Flag which indicates if the message is read by receiver
        creation date: Date of creation of the Message by sender.


    """
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Создатель',
                               related_name='sent_messages', null=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Получатель',
                                 related_name='got_messages', null=True)
    message = models.CharField('Содержание сообщения', max_length=4095,
                               help_text='Содержание письма может быть максимум в 4095 символов')
    subject = models.CharField('Тема сообщения', max_length=255,
                               help_text='Тема сообщения может быть максимум в 255 символов')
    is_read = models.BooleanField('Прочитано ли?', default=False)
    creation_date = models.DateTimeField('Дата создания', auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        db_table = 'messages'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-creation_date']
