import db_engine

class Document(db_engine.Model):
    id = db_engine.Column(db_engine.Integer, primary_key=True)
    title = db_engine.Column(db_engine.String(100))
    content = db_engine.Column(db_engine.Text)
    json_data = db_engine.Column(db_engine.Text)
n
