from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is home page")
def about(request):
    return render(request,'about.html',)
    
def services(request):
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    Doge_coin = requests.get("https://coinswitch.co/coins/dogecoin/dogecoin-to-inr").text
    soup = BeautifulSoup(Doge_coin, 'html.parser')
    cryptos = soup.find_all('a', class_="assets__card")
    list1=[]
    list2=[]
    for crypto in cryptos:
        co = crypto.get_text().replace(' ', '').split()
        list1.append(co)
    con=pd.DataFrame(list1)
    con.columns=["coins","price"]
    for i in range(con.shape[0]):
        temp=con.iloc[i]
        list2.append(dict(temp))
    # print(list2)

    context = {'data':list2}


    return render(request,'services.html',context)
def contact(request):
    if request.method ==  "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        contact = Contact(name=name, email=email, description=description, date=datetime.today())
        contact.save()
        messages.success(request, 'Successfully Submitted.!')
    return render(request,'contact.html')