import psycopg2
from config import config 

def get_parts(vendor_id):
    # get parts provided by a vendor specified by the vendor_id
    conn = None 
    try:
        # read database configuration 
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()
        query = '''
            RETURN QUERY
            SELECT parts.part_id, parts.part_name
            FROM parts
            INNER JOIN vendor_parts on vendor_parts.part_id = parts.part_id
            WHERE vendor_id = id;
        '''
        # another way to call a stored procedure
        cur.callproc(query, (vendor_id))
        # process the result set
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        # close the communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__=='__main__':
    get_parts(1)