import psycopg2
import psycopg2.extras

hostname = 'localhost'
database = 'seshatdb'
username = 'postgres'
pwd = '5tr4%TR$'
port_id = 5432
conn = None

# 'ENGINE': 'django.db.backends.postgresql_psycopg2',
# 'NAME': 'seshatdb',
# 'USER': 'postgres',
# 'PASSWORD': '5tr4%TR$',
# 'HOST': 'seshatdb.ci27jhxneftu.eu-central-1.rds.amazonaws.com',
# 'PORT': '5432',

#  ec2-18-156-118-42.eu-central-1.compute.amazonaws.com

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            print('Hallo there')
            #cur.execute('DROP TABLE IF EXISTS employee')

            #create_script = ''' CREATE TABLE IF NOT EXISTS employee (
            #                        id      int PRIMARY KEY,
            #                        name    varchar(40) NOT NULL,
            #                        salary  int,
            #                        dept_id varchar(30)) '''
            #cur.execute(create_script)

            insert_script  = 'INSERT INTO core_polity (name, start, end) VALUES (%s, %s, %s)'
            insert_values = [('JamesAbad', 100, 200),]
            for record in insert_values:
                cur.execute(insert_script, record)

            # update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            # cur.execute(update_script)

            # delete_script = 'DELETE FROM employee WHERE name = %s'
            # delete_record = ('James',)
            # cur.execute(delete_script, delete_record)

            # cur.execute('SELECT * FROM EMPLOYEE')
            # for record in cur.fetchall():
            #     print(record['name'], record['salary'])
            select_script = "SELECT * FROM user;"
            cur.execute(select_script)
            for record in cur.fetchall():
                print(record['name'])
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()