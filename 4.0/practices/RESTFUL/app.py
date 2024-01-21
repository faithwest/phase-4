from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from models import db, Book, Customer, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)  # Corrected function call

#MIGRATIONS>>flask db.init>>flask db migrate
migrate = Migrate(app, db)  # Corrected class capitalization


@app.route('/')#default for GET
def home():
    return jsonify({'message':'hello world'}), 200

#routes for ALL authors
@app.route('/')#default for GET
def get_authors():
    authors= Author.query.all
    authors_list=[]

    for author in authors:
        authors_list.append({
          'id':author.id,
          'name':author.name,
          'yob':author.yob,
          'nationality':author.nationality,
        })

    return jsonify({'authors':authors_list}), 200

#routes  single authors
@app.route('/authors/<int:author_id>')#default for GET
def get_author(author_id):
    author= Author.query.get(author_id)
    author_list=[]
    if author:
         author_list.append({
                 'id':author.id,
                 'name':author.name,
                 'yob':author.yob,
                 'nationality':author.nationality,
             })

         return jsonify({'authors':author_list}), 200
    else:
         return jsonify({"error":"Author not found"}), 404

 #PUT
@app.route('/authors', methods=['Post'])#default for GET
def add_author(): 
    data =request.get_json()
    print(request.data.name)
    new_author = Author(data["name"],data["yob"])
    db.session.add(new_author)
    db.session.commit()
    return jsonify({'success':'added authors'}) , 200      

if  __name__=='__main__':
     app.run(port= 4000, debug=True)    