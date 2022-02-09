from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String, nullable=False)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_description = db.Column(db.String)
    course_enrollments = db.relationship("Enrollment", backref='enrolled_course')

    def __repr__(self):
        return "<Course %r>" % self.course_code

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)
    student_enrollments = db.relationship('Enrollment', backref='enrolled_student')

    def __repr__(self):
        return '<Student %r>' % self.roll_number

class Enrollment(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable=False)

    def __repr__(self):
        return "<Enrollment %r>" % self.enrollment_id