#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from drewantech_common.postgres_database \
    import (connect_to_database,
            execute_postgres_command)
from demo_databases.demo_database_web_service_common \
    import (db_user, db_password, db_host, db_port, users_to_manage)


def create_users():
  for user in users_to_manage:
    execute_postgres_command(engine=connect_to_database(
                             user_name=db_user,
                             user_password=db_password,
                             database_host=db_host,
                             database_port=db_port,
                             database_name=db_user),
                             command=('CREATE USER {} WITH PASSWORD {}'
                                      .format(user,
                                              users_to_manage
                                              [user]
                                              ['password'])))


def drop_users():
  for user in users_to_manage:
    execute_postgres_command(engine=connect_to_database(
                             user_name=db_user,
                             user_password=db_password,
                             database_host=db_host,
                             database_port=db_port,
                             database_name=db_user),
                             command='DROP USER {}'.format(user))
