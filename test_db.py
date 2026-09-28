from db import get_connection


def test_database_connection():
    connection = get_connection()

    assert connection is not None

    connection.close()


def test_insert_student():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, age) VALUES (%s, %s) RETURNING id",
        ("Test Student", 25)
    )

    student_id = cursor.fetchone()[0]

    connection.commit()

    assert student_id is not None

    cursor.close()
    connection.close()

def test_update_student():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET age = %s WHERE name = %s",
        (30, "Test Student")
    )

    connection.commit()

    assert cursor.rowcount == 1

    cursor.close()
    connection.close()

def test_delete_student():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE name = %s",
        ("Test Student",)
    )

    connection.commit()

    assert cursor.rowcount == 1

    cursor.close()

    connection.close()

def test_select_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, name, age FROM students")

    students = cursor.fetchall()

    assert isinstance(students, list)
    assert len(students) >= 0

    cursor.close()
    connection.close()