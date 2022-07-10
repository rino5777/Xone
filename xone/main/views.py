
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from user.forms import OwnerUrlsForm
from user.models import OwnerUrls
from django.contrib.auth import get_user_model
import short_url
import os
# Create your views here.
import qrcode
from django.http import HttpResponse

def main_page(request):
    user = request.user
    actual_key, actual_value, ownerlist = '', '', {}

    history = OwnerUrls.objects.all()
    form = OwnerUrlsForm()
    #print(request.user.is_authenticated)
    #print(user)
    waytoimg = '/'.join(os.path.abspath('img').split('\\'))
    
    if request.method == 'POST':
        form = OwnerUrlsForm(request.POST)
        if form.is_valid():
            surl = form.save(commit=False)
            surl.owner = user 
            surl.save()
            surl.short_url = short_url.encode_url(surl.id)
            
            img = qrcode.make(surl.short_url)
            type(img)  # qrcode.image.pil.PilImage
            img.save("img/testqr.jpg" )
            print('/'.join(os.path.abspath('img').split('\\')))
            surl.save()
            
            
            messages.success(request, 'Ссылка готова !')
            return redirect('main:main_page')

    for i in history:
        if i.owner == user:
                ownerlist[i.short_url] = i.long_url
                actual_key = list(ownerlist.keys())[-1::][0]
                actual_value = list(ownerlist.values())[-1::][0]
    return render(request, 'home/home.html', {'form': form, 'actual_key':actual_key, 'actual_value':actual_value, 'waytoimg':waytoimg, 'history':history })



def urlre(request, short_url):
    #elem = get_object_or_404(OwnerUrls, id=id)
    url = ''
    elem = OwnerUrls.objects.all()
    print(elem)
    for i in elem:
        print(i)
        if i.short_url == short_url: 
            url = i.long_url
    

            
    #return HttpResponse('hi!!!'+str(short_url ) )
    return redirect('{}'.format(url))
