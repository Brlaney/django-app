from django.shortcuts import render, redirect
# from .models import Location, Dataset, Contact
# from .forms import ContactForm
# from django.contrib import messages


def index(request):
    # locations = Location.objects.all()
    # context = {'locations': locations}
    return render(request, 'pages/index.html')


# def datasets(request, city):
#     location = Location.objects.get(city=city)
#     datasets = location.dataset_set.all()
#     return render(request, 'datasets/sets.html', {'datasets': datasets, 'location': location})


# def contact(request):
#     if request.method != 'POST':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your contact info has been successfully submitted.')
#             return redirect ('datasets:index')
#     context = {'form': form}
#     return render(request, 'datasets/contact.html', context)
