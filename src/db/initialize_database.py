from db.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.executescript('''
        DROP TABLE IF EXISTS investment;
        DROP TABLE IF EXISTS portfolio;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE investment (
            id integer primary key autoincrement,
            portfolio_id integer REFERENCES portfolio(id),
            type text,
            name text,
            amount real,
            purchase_price real
        );
    ''')

    cursor.execute('''
        CREATE TABLE portfolio (
            id integer primary key autoincrement,
            name text,
            funds real
        );
    ''')


    connection.commit()


def initialize_database():
    print("Connecting to the database...")
    connection = get_database_connection()
    print("Done ✅")

    print("Dropping existing tables...")
    drop_tables(connection)
    print("Done ✅")

    print("Creating new tables...")
    create_tables(connection)
    print("Done ✅")

    print("Populating portfolio table...")
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO portfolio (name, funds)
        VALUES ('Default', 10000.0)
    ''')
    connection.commit()
    print("Done ✅")
    print("")
    print("Database initialized successfully! 🎉")
    print("You can now run the application.")
    print("")


if __name__ == "__main__":
    initialize_database()
