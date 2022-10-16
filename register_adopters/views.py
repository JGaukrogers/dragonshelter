from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from register_adopters.models import Adopter, AdoptersCharacteristic


def index(request):
    characteristics_list = AdoptersCharacteristic.objects.all()
    context = {'characteristics_list' : characteristics_list}
    return render(request, 'register_adopters/index.html', context)


def adopter(request):
    print('in adopter()')
    print(request.POST)
    print(request.POST['birthdate'].__class__)

    new_adopter = Adopter()
    new_adopter.adopters_name = request.POST['adopters_name']
    new_adopter.id_number = request.POST['adopters_id']

#    new_adopter.date_of_birth = request.POST['birthdate']
    new_adopter.date_of_birth = timezone.now()

#    new_adopter.list_of_characteristics = None

    new_adopter.save()

    return render(request, 'register_adopters/thanks.html')


class RegisterAdopterView(generic.DetailView):
    new_adopter = Adopter
    template_name = 'register_adopters/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
