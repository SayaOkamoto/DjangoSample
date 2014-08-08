# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from topics.models import ContactForm
from django.template import RequestContext
# アップロードファイルを処理する関数を import します
# from somewhere import handle_uploaded_file

# Create your views here.
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def contact(request):
    if request.method == 'POST': # フォームが提出された
        form = ContactForm(request.POST) # POST データの束縛フォーム
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['saya_okamoto@voyagegroup.com']
            if cc_myself:
                recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/topics/thanks/') # POST 後のリダイレクト
    else:
        form = ContactForm() # 非束縛フォーム
    return render_to_response('topics/contact.html',
            {'form': form, },
            context_instance=RequestContext(request),
            )

def thanks(request):
    return render(request, 'topics/thanks.html')

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file  = forms.FileField()
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render_to_response('topics/upload.html', {'form': form})
#
# def handle_uploaded_file(f):
#     destination = open('some/file/name.txt', 'wb+')
#     for chunk in f.chunks():
#         destination.write(chunk)
#         destination.close()
