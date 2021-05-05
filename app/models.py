from app import db
from datetime import datetime


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    startdate = db.Column(db.Date, index=True)
    enddate = db.Column(db.Date, index=True)
    hours = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Course {self.id}>: {self.title} | {self.startdate} - {self.enddate}'
    
    def __init__(self, title, startdate, enddate, hours):
        self.title = title
        self.startdate = datetime.strptime(startdate, "%Y-%m-%d").date(),
        self.enddate = datetime.strptime(enddate, "%Y-%m-%d").date(),
        self.hours = hours

    @property
    def dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'startdate': self.startdate.isoformat() + 'Z',
            'enddate': self.enddate.isoformat() + 'Z',
            'hours': self.hours,
            }
        return data
