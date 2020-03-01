import psycopg2
from config import config

def write_blob(part_id, path_to_file, file_extension):
    # insert a blob into a table
    conn = None 
    try:
        # read data from a picture
        drawing = open(path_to_file, 'rb').read()
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the INSERT statement
        query = '''
            INSERT INTO part_drawings(part_id, file_extension, drawing_data)
            VALUES(%s, %s, %s)
        '''
        cur.execute(query, (part_id, file_extension, psycopg2.Binary(drawing)))
        # commit the changes to the database
        conn.commit()
        # close the communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def read_blob(part_id, path_to_dir):
    # read BLOB data from a table
    conn = None 
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor object
        cur = conn.cursor()
        # execute the SELECT statement
        query = '''
            SELECT part_name, file_extension, drawing_data
            FROM part_drawings
            INNER JOIN parts on parts.part_id = part_drawings.part_id
            WHERE parts.part_id = %s
        '''
        cur.execute(query, (part_id,))
        blob = cur.fetchone()
        open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])

        #close the communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            