from django.shortcuts import render, get_object_or_404

from list_dragons.models import Dragon


def index(request):
    dragon_list = Dragon.objects.all()
    context = {'dragon_list': dragon_list}
    return render(request, 'list_dragons/index.html', context)


def detail(request, dragon_id):
    selected_dragon = get_object_or_404(Dragon, pk=dragon_id)
    context = {'dragon': selected_dragon, 'age': selected_dragon.get_age()}
    return render(request, 'list_dragons/detail.html', context)