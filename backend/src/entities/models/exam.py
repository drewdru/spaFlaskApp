# coding=utf-8
from datetime import datetime
from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, DateTime
from . import modelsHelper

class Exam(modelsHelper.Base):
    __tablename__ = 'exams'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String)
    title = Column(String)
    description = Column(String)

    def __init__(self):
        super().open()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().close()

    def getQuery(self):
        return self.session.query(Exam)

    def insert(self, created_by, title, description):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by
        self.title = title
        self.description = description


class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
