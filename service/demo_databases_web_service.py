#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from flask import (Flask,
                   render_template,
                   flash,
                   redirect,
                   url_for)
from os import urandom
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


@app.route('/matrix', methods=['GET'])
def matrix_database_operations():
  return render_template('matrix_database_operations.html')


@app.route('/matrix_database_create')
def matrix_database_create():
  try:
    matrix_create_database()
    flash('Successfully created matrix database.')
  except Exception as e:
    flash('Error in creating matrix database: {}'.format(e))
  return redirect(url_for('matrix_database_operations'))


@app.route('/matrix_table_create')
def matrix_table_create():
  try:
    matrix_create_tables()
    flash('Successfully created matrix database tables.')
  except Exception as e:
    flash('Error in creating matrix database tables: {}'.format(e))
  return redirect(url_for('matrix_database_operations'))


@app.route('/matrix_table_drop')
def matrix_table_drop():
  try:
    matrix_drop_tables()
    flash('Successfully dropped matrix database tables.')
  except Exception as e:
    flash('Error in dropping matrix database tables: {}'.format(e))
  return redirect(url_for('matrix_database_operations'))


@app.route('/matrix_database_drop')
def matrix_database_drop():
  try:
    matrix_drop_database()
    flash('Successfully dropped matrix database.')
  except Exception as e:
    flash('Error in dropping matrix database: {}'.format(e))
  return redirect(url_for('matrix_database_operations'))
