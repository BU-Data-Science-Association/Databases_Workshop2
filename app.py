import os
from datetime import datetime
from flask import Flask, jsonify, redirect, render_template, request, send_from_directory, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import MetaData

app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)

# WEBSITE_HOSTNAME exists only in production environment
if 'WEBSITE_HOSTNAME' not in os.environ:
    # local development, where we'll use environment variables
    print("Loading config.development and environment variables from .env file.")
    app.config.from_object('azureproject.development')
else:
    # production
    print("What are you doing here, this is just a workshop.")
    print("Loading config.production.")
    app.config.from_object('azureproject.production')

app.config.update(
    SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Initialize the database connection
db = SQLAlchemy(app)

# Enable Flask-Migrate commands "flask db init/migrate/upgrade" to work
migrate = Migrate(app, db)

# The import must be done after db initialization due to circular import issue
from models import Restaurant, Review

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/subject/<name>', methods = ['GET'])
def subject(name):

    # TODO Write SQL Query to get all artworks that depict the subject given in {name} 

    sql = f'''
        SELECT *
        FROM "work" 
        LEFT JOIN "subject"
        ON "work".work_id = "subject".work_id
        WHERE "subject".subject = '{name}'
        LIMIT 25
    '''

    with db.engine.connect() as conn:
        result = conn.execute(db.text(sql)).fetchall()

    rows = [dict(row._mapping) for row in result]
    return render_template('index.html', results = rows)

@app.route('/style/<name>', methods = ['GET'])
def style(name):

    # TODO Write SQL Query to get all food items containing meat -> {name} 

    sql = f'''
        SELECT * 
        FROM "work"
        LEFT JOIN "subject"
        ON "work".work_id = "subject".work_id
        WHERE "work".style = '{name}'
        LIMIT 25
    '''

    with db.engine.connect() as conn:
        result = conn.execute(db.text(sql)).fetchall()

    rows = [dict(row._mapping) for row in result]
    return render_template('index.html', results = rows)

@app.route('/meal_type/<name>', methods = ['GET'])
def mealType(name):
    name = name.lower()

    # TODO Write SQL Query to get all food item served during meal_type -> {name} 

    sql = f'''
        SELECT *
        FROM "work"
        LEFT JOIN "subject"
        ON "work".work_id = "subject".work_id
        WHERE "work".museum_id = '{name}'
        LIMIT 25
    '''
    
    with db.engine.connect() as conn:
        result = conn.execute(db.text(sql)).fetchall()

    rows = [dict(row._mapping) for row in result]
    return render_template('index.html', results = rows)


@app.route('/add_artwork', methods=['POST'])
@csrf.exempt
def add_artwork():
    try:
        work_id = request.form.get('work_id')
        work_name = request.form.get('work_name')
        artist_id = request.form.get('artist_id')
        style = request.form.get('style')
        museum_id = request.form.get('museum_id')
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400

    sql = '''
        INSERT INTO public."work" ("work_id", "name", "artist_id", "style", "museum_id")
        VALUES (:work_id, :work_name, :artist_id, :style, :museum_id)
    '''

    with db.engine.begin() as conn:
        conn.execute(db.text(sql), {
            'work_id': work_id,
            'work_name': work_name,
            'artist_id': artist_id,
            'style': style,
            'museum_id': museum_id,
        })

    return redirect(url_for('index'))

@app.route('/add_artwork_form', methods=['GET'])
def add_artwork_form():
    return render_template('add.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()
