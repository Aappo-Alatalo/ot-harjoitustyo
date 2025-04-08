from database_connection import get_database_connection # pylint: disable=import-error
# Pylint disabled due to fixing the "error" makes the actual code not work


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS investments;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE investments (
            id integer primary key autoincrement,
            type text,
            name text,
            amount real,
            purchase_price real
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
