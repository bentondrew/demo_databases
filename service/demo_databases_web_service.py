#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   flash,
                   redirect,
                   url_for)
from os import urandom
from demo_databases.database_operations \
    import (create_users,
            drop_users)
from demo_databases.matrix_database_operations \
    import (create_database as matrix_create_database,
            drop_database as matrix_drop_database,
            create_tables as matrix_create_tables,
            drop_tables as matrix_drop_tables)

app = Flask(__name__)
app.secret_key = urandom(32)


@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')


@app.route('/databases_initialization')
def databases_initialization():
  try:
    flash('Attempting to create database users.')
    create_users()
    flash('Successfully created database users.')
    flash('Attempting to create matrix database.')
    matrix_create_database()
    flash('Successfully created matrix database.')
    flash('Attempting to create matrix database tables.')
    matrix_create_tables()
    flash('Successfully created matrix database tables.')
  except Exception as e:
    raise flash('Error in initializing databases: {}'.format(e))
  return redirect(url_for('index'))


@app.route('/databases_tear_down')
def databases_tear_down():
  try:
    flash('Attempting to drop matrix database tables.')
    matrix_drop_tables()
    flash('Successfully dropped matrix database tables.')
    flash('Attempting to drop matrix database.')
    matrix_drop_database()
    flash('Successfully dropped matrix database.')
    flash('Attempting to drop database users.')
    drop_users()
    flash('Successfully dropped database users.')
  except Exception as e:
    raise flash('Error in tearing down databases: {}'.format(e))
  return redirect(url_for('index'))
