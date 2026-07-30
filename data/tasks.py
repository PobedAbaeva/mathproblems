import sqlalchemy
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase

task_topic_association = sqlalchemy.Table(
    'task_topics',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('task_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('tasks.id'), primary_key=True),
    sqlalchemy.Column('topic_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('topics.id'), primary_key=True)
)


class Task(SqlAlchemyBase):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    condition = sqlalchemy.Column(sqlalchemy.Text)
    solution = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

    topics = relationship('Topic',
                          secondary=task_topic_association,
                          back_populates='tasks')


class Topic(SqlAlchemyBase):
    __tablename__ = 'topics'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    theme = sqlalchemy.Column(sqlalchemy.String(100), unique=True, nullable=False)

    tasks = relationship('Task',
                         secondary=task_topic_association,
                         back_populates='topics')