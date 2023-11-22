from django.shortcuts import render

from phonemarket.models import Phones


def all_phones(request):
    get_req = request.GET.get('sort', None)
    if get_req == 'name':
        all_phones_ = Phones.objects.all().order_by(get_req)
    elif get_req == 'price':
        all_phones_ = Phones.objects.all().order_by(get_req)
    elif get_req == '-price':
        all_phones_ = Phones.objects.all().order_by(get_req)
    else:
        all_phones_ = Phones.objects.all()

    my_dict = {
        'phones': all_phones_,
        'title': 'Телефоны',

    }
    return render(request, 'phonemarket/index.html', my_dict)


def phone_detail(request, slug):
    phone = Phones.objects.get(slug=slug)
    id_ = Phones.objects.filter(slug=slug)
    for i in id_:
        list_ = [k for k in str(i).split()]
        print(list_)

    my_dict = {
        'phone': phone,
        'title': f'Телефон {str(phone)[:-3]}',

    }
    return render(request, 'phonemarket/phone_detail.html', my_dict)


def list_pages(request):
    my_dict = {
        'title': 'Главная страница',
    }
    return render(request, 'phonemarket/list_pages.html', my_dict)
