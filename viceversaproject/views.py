from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reversed(request):
	test = request.GET['userstep']
	reservedtest = test[::-1]
	return render(request, 'reversed.html', {'xxx':test,'yyy':reservedtest})