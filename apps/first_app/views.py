from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if not (request.session.get('farm') or request.session.get('cave') or request.session.get('house') or request.session.get('casino') or request.session.get('total')):
        request.session['history'] = []
        request.session['total'] = 0
        request.session['update'] = False
    return render(request, "first_app/index.html")

def process_money(request):
    if request.POST['building'] == 'farm':
        randGold = random.randint(10, 20)
        request.session['total'] += randGold
        print("total", request.session['total'])
        output = "Earned " + str(randGold) + " gold from the farm!"
        request.session['history'].append(output)
    if request.POST['building'] == 'cave':
        randGold = random.randint(5, 10)
        request.session['total'] += randGold
        print("total", request.session['total'])
        output = "Earned " + str(randGold) + " gold from the cave!"
        request.session['history'].append(output)
    if request.POST['building'] == 'house':
        randGold = random.randint(2, 5)
        request.session['total'] += randGold
        print("total", request.session['total'])
        output = "Earned " + str(randGold) + " gold from the house!"
        request.session['history'].append(output)
    if request.POST['building'] == 'casino':
        switch = random.randint(0, 1)  # 0 for subtraction, 1 for addition
        randGold = random.randint(0, 50)
        if switch == 1:
            request.session['total'] += randGold
            output = "Entered a casino and won " + str(randGold) + "!"
            request.session['history'].append(output)
        else:
            request.session['total'] -= randGold
            if request.session['total'] < 0:
                request.session['total'] = 0
            output = "Entered a casino and lost " + str(randGold) + " golds... Ouch.."
            request.session['history'].append(output)
        print("total", request.session['total'])

    return redirect("/")

def restart(request):
    request.session['history'] = []
    request.session['total'] = 0
    request.session['update'] = False

    return redirect("/")