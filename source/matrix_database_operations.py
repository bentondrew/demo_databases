#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

from drewantech_common.postgres_database \
    import (connect_to_database,
            generate_create_database_command,
            generate_drop_database_command,
            execute_postgres_command)
from demo_common.matrix_database_common \
    import (database_name,
            Base,
            Matrix,
            Dimension,
            Point)
from demo_databases.demo_database_web_service_common \
    import (db_user, db_password)


def create_database():
  execute_postgres_command(engine=connect_to_database(user_name=db_user,
                                                      user_password=db_password,
                                                      database_name=db_user),
                           command=generate_create_database_command(database_name))


def drop_database():
  execute_postgres_command(engine=connect_to_database(user_name=db_user,
                                                      user_password=db_password,
                                                      database_name=db_user),
                           command=generate_drop_database_command(database_name))


def create_tables():
  Base.metadata.create_all(bind=connect_to_database(user_name=db_user,
                                                    user_password=db_password,
                                                    database_name=database_name))


def drop_tables():
  Base.metadata.drop_all(bind=connect_to_database(user_name=db_user,
                                                  user_password=db_password,
                                                  database_name=database_name))
