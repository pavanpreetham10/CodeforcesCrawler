from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def home(request):
    if request.method=='POST':
        form=handleForm(request.POST)
        if form.is_valid():
            handle=form.cleaned_data.get('handle')
            return redirect('/display/'+handle)
    else:
            form=HandleForm()
    return render(request, 'crawler/index.html', handle)

def display(request,handle):
    context={
        'handle': handle,
    }
    return render(request, 'crawler/index2.html', context)


