import sqlite3


class CRUD:

    def __init__(self):
        self.connect = sqlite3.connect('CRUD.db')
        self.cursor = self.connect.cursor()

    def create_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name CHAR(30) NOT NULL,
                record TEXT default "Zero" 
            )
            """
        )
        self.connect.commit()

    def insert(self, data: tuple[str, ...]) -> None:
        self.cursor.execute(
            """
            INSERT INTO records (name, record) 
            VALUES (?, ?)
            """, data
        )
        self.connect.commit()

    def read(self, record_id: int) -> tuple[int, str]:
        self.cursor.execute(
            """
            SELECT * FROM records WHERE id=(?)
            """, (record_id,)
        )
        return self.cursor.fetchone()

    def readall(self) -> tuple[int, str]:
        self.cursor.execute(
            """
            SELECT * FROM records
            """
        )
        return self.cursor.fetchall()

    def delete(self, record_id: int) -> None:
        self.cursor.execute(
            """
            DELETE FROM records WHERE id=(?) 
            """, (record_id,)
        )
        self.connect.commit()

    def update(self, data: list[str]):
        self.cursor.execute(
            """
            UPDATE records 
            SET name=?, record=?
            WHERE records.id=?
            """, (data[1], data[2], data[0])
        )
        self.connect.commit()


def main():
    crud = CRUD()
    crud.create_table()
    while True:
        request = input(
            'Что вы хотите сделать?'
            '\n"Записать-insert","Прочитать-read","Прчитать всё-readall","Оновить-update","Удалить-delete","Выйти из программы-exit":'
            '\n->'
        )
        if request == 'insert':
            data = (input('Введите имя: '), input('Введите данные: '))
            crud.insert(data=data)
            continue
        elif request == 'read':
            data = int(input('Введите id: '))
            print(crud.read(record_id=data))
            continue
        elif request == 'readall':
            print(crud.readall())
            continue
        elif request == 'delete':
            data = int(input('Введите id: '))
            crud.delete(record_id=data)
            continue
        elif request == 'update':
            data = [int(input('Id: ')), input('Введите имя: '), input('Введите данные: ')]
            crud.update(data=data)
            continue
        elif request.strip() == 'exit':
            exit()
        else:
            continue


if __name__ == '__main__':
    main()
