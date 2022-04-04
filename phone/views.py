from django.shortcuts import render, redirect
from django.views import generic
from .models import *
from django.urls import reverse
from .forms import *


class IndexPage(generic.ListView):
    template_name = 'index.html'
    model = Phone
    context_object_name = 'phones'


# class CreatePhoneView(generic.CreateView):
#     template_name = 'index'
#     model = Phone
#     context_object_name = 'phones'
#
#     def get_success_url(self):
#         return redirect('index')


def create_phone_view(request):
    form = PhoneCreateForm()
    if request.method == 'POST':
        form = PhoneCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create.html', locals())


class DetailPhoneView(generic.DetailView):
    template_name = 'detail.html'
    model = Phone
    context_object_name = 'phone'


class UpdatePhoneView(generic.UpdateView):
    template_name = 'update.html'
    model = Phone
    form_class = PhoneCreateForm
    context_object_name = 'phone'

    def get_success_url(self):
        return reverse('index')


class DeletePhoneView(generic.DeleteView):
    model = Phone
    success_url = '/'
    template_name = 'delete.html'


def search(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            phones = Phone.objects.filter(title__icontains=text)
            return render(request, 'search_result.html', {'phones': phones})

    return render(request, 'search.html', {'form': form})
