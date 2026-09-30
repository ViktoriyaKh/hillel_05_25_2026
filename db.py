import os
import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5433"),
        database=os.getenv("DB_NAME", "test_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres")
    )

    return connection


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INTEGER
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


def insert_student(name, age):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, age) VALUES (%s, %s)",
        (name, age)
    )

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    create_table()
    print("Таблица students создана!")