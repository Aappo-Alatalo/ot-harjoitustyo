from initialize_database import initialize_database # pylint: disable=import-error
# Pylint disabled due to fixing the "error" makes the actual code not work

def build():
    initialize_database()


if __name__ == "__main__":
    build()
