from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from agenda.models import Contact
from django.views import generic

def base(request):
       return render(request, 'agenda/contact_list.html')



class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return Contact.objects.filter(fullname__icontains=q)

        return super().get_queryset()


class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('avatar', 'name','fullname', 'email', 'birth', 'phone',)
    success_url = reverse_lazy('contact_list')


class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('avatar', 'name', 'fullname', 'email', 'birth', 'phone',)
    success_url = reverse_lazy('contact_list')


class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
