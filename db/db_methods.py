# Про методы можно почитать здесь (это себе)
# https://docs-python.ru/standart-library/modul-sqlite3-python/obekt-connection-modulja-sqlite3/
import sqlite3


class new_db_create():
    def __init__(self):
        # Создаем базу данных
        self.conn = sqlite3.connect(r'db/corpus.db')
        self.cur = self.conn.cursor()
        self.new_table_texts_create()
        self.new_table_words_create()
        self.new_table_nouns_create()

    # Создаем таблицу для загрузки текстов
    def new_table_texts_create(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS TEXTS(
            text_id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_content TEXT UNIQUE
            );
        """)
        self.conn.commit()

    # Создаем таблицу для загрузки слов
    def new_table_words_create(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS WORDS(
            word_id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_content string UNIQUE
            );
        """)
        self.conn.commit()

    # Создаем таблицу для загрузки существительных
    # case - падеж
    # plural - множественное число
    # possessive - притяжательная форма
    def new_table_nouns_create(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS NOUNS(
            noun_id INTEGER PRIMARY KEY AUTOINCREMENT,
            noun_content string UNIQUE,
            noun_normalform_id INTEGER,
            noun_case string,
            noun_plur string,
            noun_poss string
            );
        """)
        self.conn.commit()


class db_content:
    def __init__(self):
        # Соединяемся с базой данных
        self.conn = sqlite3.connect(r'db/corpus.db')
        self.cur = self.conn.cursor()

    # Добавление данных в аргументе в таблицу TEXTS
    # форма вызова
    # table_texts_content_add('Вводимые данные')
    '''
    user = ('00002', 'Lois', 'Lane', 'Female')
    cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
    conn.commit()
    
    more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]
    cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
    conn.commit()
    '''
    def table_texts_content_add(self, content):
        try:
            self.cur.execute(f"""INSERT INTO TEXTS(text_content) 
               VALUES('{content}');
               """)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print('В базе данных этот текст уже есть.')
            return 'В базе данных этот текст уже есть.'
        else:
            print('Текст загружен.')
            return 'Текст загружен.'

    # Добавление данных в аргументе в таблицу TEXTS
    # форма вызова
    # table_texts_content_add('Вводимые данные')
    def table_words_content_add(self, content):
        try:
            self.cur.executemany(f"""
            INSERT INTO WORDS(word_content) 
            VALUES(?);""", content)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print('Ошибка при загрузке списка слов.')
        else:
            print('Слово загружено.')

    # Добавление данных в аргументе в таблицу TEXTS
    # форма вызова
    # table_texts_content_add('Вводимые данные')
    def table_nouns_content_add(self, content, case='nomn', plur=False, poss=0):
        try:
            self.cur.execute(f"""INSERT INTO NOUNS(noun_content, noun_case, noun_plur, noun_poss)
               VALUES('{content}', '{case}', '{plur}', '{poss}');
               """)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print('В таблице это слово уже есть.')
        else:
            print('Слово загружено.')


    # Считываем данные с таблицы в аргументе
    # форма вызова
    # table_texts_content_read('TEXTS')
    def table_texts_content_read(self, TABLE):
        try:
            self.cur.execute(f"SELECT * FROM {TABLE};")
        except sqlite3.IntegrityError:
            print(f'При чтении данных из таблицы {TABLE} произошла ошибка')
        else:
            print(f'Данные из таблицы {TABLE} успешно считаны')
            return set(self.cur)

    # функция заготовка для удаления данных
    def teble_del_exec(self, content):
        self.cur.execute(f"""DELETE from NOUNS where noun_content = '{content}'""")
        self.conn.commit()
