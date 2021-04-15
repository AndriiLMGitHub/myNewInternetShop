from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from contact.forms import ContactForm

# Create your views here.

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']

			recipients = ['andreydecua@gmail.com']
			#Если пользователь захотел получить копию себе, добавляем его в список получателей
			# if copy:
			# 	recipients.append(sender)
			try:
				send_mail(subject, message, sender, recipients)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
			return render(request, 'contact/thanks.html', )
	else:
		#Заполняем форму
		form = ContactForm()
	#Отправляем форму на страницу
    
	return render(request, 'contact/contact.html', { 'form': form, })