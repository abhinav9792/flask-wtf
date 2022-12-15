from flask import Flask,render_template
#for database
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, MetaData

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


app = Flask(__name__)
engine = create_engine("sqlite:///user.db", echo=True)
# for creating table
meta = MetaData()
app.config["SECRET_KEY"] = "efdck4549itfdfvslkreit054tgr44"

User = Table(
    "User",meta,
    Column("s.no",Integer,primary_key=True,autoincrement=True),
    Column("name",String),
    Column("email",String),
    Column("password",String)
)
meta.create_all(engine)

class Register(FlaskForm):
    name= StringField(label="name")
    email = StringField(label="email")
    submit = SubmitField(label="submit")

@app.route("/")
def hello_world():
    #creating instance
    form =Register()
    return render_template("a.html",form=form)

if __name__ == "__main__":
    app.run(debug=True)