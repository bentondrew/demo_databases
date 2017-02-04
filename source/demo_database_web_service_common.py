#  Copyright 2016
#  Drewan Tech, LLC
#  ALL RIGHTS RESERVED

db_user = 'web_service_admin'
db_password = 'web_service_admin'
db_host = 'postgres'
db_port = '5432'
users_to_manage = {'random_matrix':
                   {'authorized_databases':
                    ['matrix_database'],
                    'password':
                    'random_matrix'},
                   'matrix_mult':
                   {'authorized_databases':
                    ['matrix_database'],
                    'password':
                    'matrix_mult'}}
