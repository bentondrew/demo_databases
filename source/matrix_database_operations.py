#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from drewantech_common.postgres_database \
    import (connect_to_database,
            execute_postgres_command)
from demo_common.matrix_database_common \
    import (database_name,
            Base,
            Matrix,
            Dimension,
            Point)
from demo_databases.demo_database_web_service_common \
    import (db_user, db_password, db_host, db_port, users_to_manage)


def create_database():
  #  Create database.
  execute_postgres_command(engine=connect_to_database(
                           user_name=db_user,
                           user_password=db_password,
                           database_host=db_host,
                           database_port=db_port,
                           database_name=db_user),
                           command='CREATE DATABASE {}'.format(database_name))
  #  Restrict access to authorized database users.
  execute_postgres_command(engine=connect_to_database(
                           user_name=db_user,
                           user_password=db_password,
                           database_host=db_host,
                           database_port=db_port,
                           database_name=db_user),
                           command=('REVOKE connect ON DATABASE {} FROM PUBLIC'
                                    .format(database_name)))
  for user in users_to_manage:
    if database_name in users_to_manage[user]['authorized_databases']:
      execute_postgres_command(engine=connect_to_database(
                               user_name=db_user,
                               user_password=db_password,
                               database_host=db_host,
                               database_port=db_port,
                               database_name=db_user),
                               command=('GRANT connect ON DATABASE {} TO {}'
                                        .format(database_name, user)))


def drop_database():
  execute_postgres_command(engine=connect_to_database(
                           user_name=db_user,
                           user_password=db_password,
                           database_host=db_host,
                           database_port=db_port,
                           database_name=db_user),
                           command='DROP DATABASE {}'.format(database_name))


def create_tables():
  Base.metadata.create_all(bind=connect_to_database(
                           user_name=db_user,
                           user_password=db_password,
                           database_host=db_host,
                           database_port=db_port,
                           database_name=database_name))


def drop_tables():
  Base.metadata.drop_all(bind=connect_to_database(
                         user_name=db_user,
                         user_password=db_password,
                         database_host=db_host,
                         database_port=db_port,
                         database_name=database_name))
