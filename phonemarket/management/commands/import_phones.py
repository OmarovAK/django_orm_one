from django.core.management.base import BaseCommand
import csv, os, transliterate

from phonemarket.models import Phones


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        def create_tuple(some_dict):
            list_id = set()
            for _ in some_dict:
                object_ = Phones.objects.filter(id=some_dict['id'])
                for k in object_:
                    list_id.add(str(k).split()[-1])

            if some_dict['id'] not in list_id:
                slug = transliterate.slugify(transliterate.translit(some_dict['name'], 'ru'))
                Phones.objects.create(id=some_dict['id'], name=some_dict['name'], slug=slug, price=some_dict['price'],
                                      image=some_dict['image'], release_date=some_dict['release_date'],
                                      lte_exists=some_dict['lte_exists'])
                phone = str(Phones.objects.get(id=some_dict['id']))

                result = f'Телефон {phone[:-3]} успешно записан в БД'

            else:
                phone = str(Phones.objects.get(id=some_dict['id']))
                result = f'{phone[:-3]} ранее был добавлен в БД'

            print(result)

        file_source = os.path.join(os.getcwd(), 'phones.csv')
        my_list = []
        with open(file_source, mode='r', encoding='utf-8') as file_csv:
            reading = csv.DictReader(file_csv, delimiter=';')
            for i in reading:
                my_list.append(i)
        for i in my_list:
            create_tuple(i)
