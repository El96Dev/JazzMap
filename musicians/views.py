from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Musician


def musicians(request):
    musicians = Musician.objects.all()
    paginator = Paginator(musicians, 6)
    musicians_dict = dict()

    page_number = request.GET.get('page')
    print("page number", page_number)

    current_page = paginator.get_page(page_number)

    page_obj = paginator.get_page(page_number)


    for musician in current_page:
        if musician.first_name[0] in musicians_dict:
            musicians_dict[musician.first_name[0]].append(musician)
        else:
            musicians_dict[musician.first_name[0]] = [musician,]

    musicians_dict = dict(sorted(musicians_dict.items()))

    return render(request, 'musicians/musicians_list.html', {"musicians_dict": musicians_dict, "page_obj": page_obj})


def show_musician(request, musician_slug):
    musician = Musician.objects.filter(slug=musician_slug)
    print(musician[0].image.url)
    return render(request, 'musicians/musician.html', {"musician": musician[0]})
