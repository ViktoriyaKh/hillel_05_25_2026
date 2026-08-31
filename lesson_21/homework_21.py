import random
from faker import Faker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

POSTGRESQL_URL = "postgresql://postgres:password@localhost:5432/homework_21"

engine = create_engine(POSTGRESQL_URL)

Base = declarative_base()

student_course = Table(
    'student_course',
    Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship(
        'Course',
        secondary=student_course,
        back_populates='students'
    )

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship(
        'Student',
        secondary=student_course,
        back_populates='courses'
    )

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

# courses = [
#     Course(name='Python'),
#     Course(name='SQL'),
#     Course(name='Git'),
#     Course(name='API'),
#     Course(name='QA')
# ]
#
# students = []
#
# for i in range(20):
#     student = Student(name=faker.name())
#     students.append(student)
#
# for student in students:
#     student.courses = random.sample(courses, random.randint(1, 3))

# session.add_all(courses)
# session.add_all(students)
#
# session.commit()

# new_student = Student(name=faker.name())
#
# course = session.query(Course).filter_by(name='Python').first()
#
# new_student.courses.append(course)
#
# session.add(new_student)
# session.commit()

python_students = session.query(Student).join(Student.courses).filter(Course.name == 'Python').all()

for student in python_students:
    print(student.name)

student = session.query(Student).first()

print(f"Student: {student.name}")

for course in student.courses:
    print(course.name)

test_student = Student(name='Test Student')
session.add(test_student)
session.commit()

test_student.name = 'Updated Student'
session.commit()

print(test_student.name)

session.delete(test_student)
session.commit()