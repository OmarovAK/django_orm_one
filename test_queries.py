import sqlalchemy

import csv, transliterate, os


class db_connect:
    def __init__(self, login, password, base):
        self.login = login
        self.password = password
        self.base = base

    def connect(self):
        db = f'postgresql://{self.login}:{self.password}@localhost:5432/{self.base}'
        engine = sqlalchemy.create_engine(db)
        connection = engine.connect()
        return connection


conn = db_connect('postgres', '123456', 'marketplace')


def insert_data():
    list_dict = []
    file_source = os.path.join(os.getcwd(), 'phones.csv')
    with open(file_source, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for dict_ in reader:
            list_dict.append(dict_)

    def insert_tuple_(some_dict):
        slug = transliterate.slugify(transliterate.translit(some_dict['name'], 'ru'))
        with conn.connect() as conn_:
            tuple_from_model = f"id, name, slug, price, image, release_date, lte_exists"
            conn_.execute(sqlalchemy.text(f"INSERT INTO phonemarket_phones ({tuple_from_model})"
                                          f"VALUES "
                                          f"('{some_dict['id']}', '{some_dict['name']}', '{slug}',"
                                          f"'{some_dict['price']}' , '{some_dict['image']}',"
                                          f"'{some_dict['release_date']}', '{some_dict['lte_exists']}')"
                                          f"ON CONFLICT DO NOTHING"))
            conn_.commit()
    for i in list_dict:
        insert_tuple_(i)

insert_data()