# PostgreSQL Python
---
1. [Conect To PostgreSQL Database Server](#Connect-To-PostgreSQL-Database-Server): how to connect to the PostgreSQL database server from a Python application.
2. [Create Tables](#Create-Tables): the steps of creating new tables in PostgreSQL using psycopg2.
3. [Insert Data](#Insert-Data): explains how to insert data into a PostgreSQL database table in Python.
4. [Update Data](#Update-Data): learns various ways to update data in the PostgreSQL table.
5. [Query Data](#Query-Data): steps of querying data from the PostgreSQL tables in a Python application.
6. [Store Procedures](#Store-Procedures): call stored procedures from the PostgreSQL database in a Python application.
7. [Handling Blob_Data](#Handling-Blob-Data): gives an example of inserting and selecting the PostgreSQL Blob Data in a Python application.
8. [Delete Data](#Delete-Data): delete data in a table in Python.
9. [Reference](#Reference)
---
## Connect To PostgreSQL Database Server
Create a new database named suppliers in PostgreSQL database server:  

    CREATE DATABASE suppliers;
To connect to the <i>suppliers</i> database, use the <i>connect()</i> function of the psycopg2 module. The <i>connect()</i> function creates a new database session and returns a new instance of the <i>connection</i> class. <br>
With a <i>connection</i> object, create a new cursor to execute an SQL statement and terminate a transaction using either <i>commit()</i> or <i>rollback()</i> method. <br>
Specify the connection parameters as a string and pass it to the <i>connect()</i> function as follows:<br>

    conn = psycopg2.connect(host="localhost", database="db_name", user="user_name", password="password_name")
The following is the list of the connection parameters:
<ul>
    <li><b>database</b>: the name of the database that you want to connect.</li>
    <li><b>user</b>: the username userd to authenticate.</li>
    <li><b>password</b>: password used to authenticate.</li>
    <li><b>host</b>: database server address</li>
    <li><b>port</b>: the port number that defeaultsto 5432 if it is not provided</li>
</ul>
To make it more convenient, use a configuration file to store all connection parameters. The following is the content of the <i>database.ini</i> file:<br>

    [postgresql]
    host = localhost 
    database = database_name 
    user = user_name
    passwor = password_name
The following <i>config()</i> funtion read the <i>database.ini</i> file and returns the connection parameters. I put the <i>config()</i> function in the <i>config.py</i> file.<br>
The following <i>connect()</i> function connects to the <i>suppliers</i> database and prints on the PostgreSQL database version.<br>
How it work: <br>
<ul>
    <li>First, read database connection parameters from the <i>database.ini</i> file.</li>
    <li>Next, create a new database connection by calling the <i>connect()</i> function.</li>
    <li>Then, create a new <i>cursor</i> and execute an SQL statement to get the PostgreSQL database version.</li>
    <li>After that, read the result set by calling the <i>fetchone()</i> method of the cursor object.</li>
    <li>Finally, close the communication with the database server by calling the <i>close()</i> method of the <i>close()</i> method of the <i>cursor</i> and <i>connection</i> objects.</li>
</ul>
The <i>connect()</i> function raises the <i>DatabaseError</i> exception if an error occurred. To see how it works, we can change the connection parameters in the <i>database.ini</i>.To see how it works, we can change the conection parameters in the <i>database.ini</i> file.

---
## Create Tables
To create a new table in a PostgreSQL database, use the following steps:
<ul>
    <li>First, construct a <b>CREATE TABLE</b> statement.</li>
    <li>Next, <i>connect to the PostgreSQL database</i> by calling the <i>connect</i> function. The <i>connect()</i> function returns a <i>connection</i> object.</li>
    <li>Then, create a <i>cursor</i> object by calling the <i>cursor</i> method of the <i>connection</i> object.</li>
    <li>After that, execute the <b>CREATE TABLE</b> by calling the execute() method of the <i>cursor</i> object.</li>
    <li>Finally, close the communication with the PostgreSQL database server by calling the <i>close()</i> methods of the <i>cursor</i> and <i>connection</i> objects.
</ul>
Let's run the program in <i>connect_table.py</i> and use the <i>\dt</i> command to display table list in the <i>suppliers</i> database.

    suppliers=# \dt
                 List of relations
     Schema |     Name      | Type  |  Owner   
    --------+---------------+-------+----------
     public | part_drawings | table | postgres
     public | parts         | table | postgres
     public | vendor_parts  | table | postgres
     public | vendors       | table | postgres
    (4 rows)
The tables created successfully in the <i>suppliers</i> database.

---
## Insert Data
#### Steps for inserting one row into a PostgreSQL table
To insert a row into a PostgreSQL table in Python, following steps: <br>
First, [Conect To PostgreSQL Database Server](#Connect-To-PostgreSQL-Database-Server) by calling the connect() function of <i>psycopg2</i> module.

    conn = psycopg2.connect(dsn)
The <i>connect</i> function returns a new instance of the <i>connection</i> class.<br>
Next, create a new <i>cursor</i> object by calling the <i>cursor()</i> method of the <i>connection</i> object.

    cur = conn.cursor()
Then, execute the <b>INSERT</b> statement with the input values by calling the <i>execute()</i> method of the <i>cursor</i> object.

    cur.execute(sql, (value1, value2))
Pass the <b>INSERT</b> statement to the first parameter and a list of values to the second parameter of the <i>execute()</i> method.<br>
In case the <i>primary key</i> of the table is an auto-generated column, can get the generated ID back after inserting the row. To do this, in the <b>INSERT</b> statement, use the <b>RETURNING <i>id</i></b> clause. After calling the <i>execute()</i> method, call the <i>fetchone()</i> method of the <i>cursor</i> object to get the id value as follows:
    
    id = cur.fetchone()[0]
After that, call the <i>commit()</i> method of the <i>connection</i> object to save the changes to the database permanently. If you gorget to call the <i>commit()</i> method, psycopg2 will not change anything to the database. <br>

    conn.commit()
Finally, close the communication with the PostgreSQL database server by calling the <i>close()</i> method of the <i>cursor</i> and <i>connection</i> objects.
    
    cur.close()
    conn.close()
#### Inserting one row into a PostgreSQL table example
For the demonstration, use the <i>vendors</i> table in the <i>suppliers</i> table that we created in [Create Tables](#Create-Tables).<br>
The following <i>insert_vendor()</i> function inserts a new row into the <i>vendors</i> table and returns the newly generated <i>vendor_id</i> value.(see insert_data.py) <br>
#### Inserting multiple rows into a PostgreSQL table example
The steps for inserting multiple rows into a table are similar to the steps of inserting one row, except that in the third step, instead of calling the <i>execute()</i> method of the <i>cursor</i> object, call the <i>executemany()</i> method.<br>
For example, the following <i>insert_vendor_list()</i> function inserts multiple rows into the <i>vendors</i> table. (see insert_data.py)

---
## Update Data
#### Steps for updating data in a PostgreSQL table using psycopg2
The steps for updating data are similar to the [Insert Data](#Insert-Data). <br>
First, [Conect To PostgreSQL Database Server](#Connect-To-PostgreSQL-Database-Server) by calling the <i>connect()</i> function of the <i>psycopg2</i> module.<br>

    conn = psycopg2.connect(dns)
Next, create a new <i>cursor</i> object by calling the <i>cursor()</i> method of the <i>connection</i> object.

    cur = conn.cursor()

Then, execute the <b>UPDATE</b> statement with the input values by calling the <i>execute()</i> method of the <i>cursor</i> object.
    
    cur.execute(update_sql, (value1, value2))

The <i>execute()</i> method accepts two parameters. The first parameter is an SQL statement to be executed, in this case, it is the <b>UPDATE</b> statement. The second parameter is a list of input values that you want to pass to the <b>UPDATE</b> statement.<br>
If you want to get the number of rows affected by the <b>UPDATE</b> statement, you can get it from the <i>rowcount</i> attribute of the <i>cursor</i> object after calling the <i>execute()</i> method.<br>
After that, save the changes to the database permanently by calling the <i>commit()</i> method of the connection object.

    conn.commit()
Finally, close the communication with the PostgreSQL database server by calling the <i>close()</i> method of the cursor and connection objects.

    cur.close()
    conn.close()
#### Updating data example
Use the <i>vendors</i> table in the <i>suppliers</i> database that created in the [Create Tables](#Create-Tables) for the sake of demonstration.<br>
Suppose a vendor changed its name and we want to update the changes in the <i>vendors</i> table. To do this, we develop the <i>update_vendor()</i> function that updates the vendor name based on the vendor id.(see update_data.py)<br>
Before testing the function, we query data from the <i>vendors</i> table as follows:

    suppliers=# SELECT * FROM vendors WHERE vendor_id=1;
     vendor_id | vendor_name 
    -----------+-------------
             1 | 3M Co.
    (1 row)
 
Now, run the Python program (update_data.py) to update the name of the vendor id 1 and query data from the <i>vendors</i> table again to verify the changes made by the Python program. 

    suppliers=# SELECT * FROM vendors WHERE vendor_id=1;
     vendor_id | vendor_name 
    -----------+-------------
             1 | 3M Corp
    (1 row)

The name of the vendor id 1 has been changed as expected.

---
## Query Data
To query data from one or more PostgreSQL tables in Python, use the following steps.<br>
First, [Conect To PostgreSQL Database Server](#Connect-To-PostgreSQL-Database-Server) by calling the <i>connect()</i> function of the <i>psycopg</i> module. <br>

    conn = psycopg2.connect(dsn)
If the connection was created successfully, the <i>connect()</i> function returns a new <i>connection</i> object, otherwise, it throws a <i>DatabaseError</i> exception.<br>
Next, create a new cursor by calling the <i>cursor()</i> method of the <i>connection</i> object. The <i>cursor</i> object is used to execute <b>SELECT</b> statements.<br>

    cur = conn.cursor()
Then, execute a <b>SELECT</b> statement by calling the <i>execute</i> method. If you want to pass values to the <b>SELECT</b> statement, you use the placeholder (%s) in the <b>SELECT</b> statement and bind the input values when you call the <i>execute()</i> method as follows.

    cur.execute(sql, (value1, value2))

After that, process the result set returned by the stored procedure using the <i>fetchone, fechall(),</i> or <i>fetchmany()</i> method.<br>
<ul>
    <li> The <b>fetchone()</b>: fetches the next row in the result set. It returns a single tuple or <i>None</i> when no more row is available.</li>
    <li> The <b>fetchmany(size=cursor.arraysize)</b> fetches the next set of rows specified by the <i>size</i> parameter. If you omit this parameter, the <i>arraysize</i> will  determine the number of rows to be fetched. The <i>fetchmany()</i> method returns a list of tuples or an empty list if no more rows available.</li>
    <li> The <b>fetchall()</b> fetches all rows in the result set and returns a list of tuples. If there are no rows to fetch, the <i>fetchall()</i> method returns an empty list.</li>
</ul>
Finally, close the communication with the PostgreSQL by calling the <i>close()</i> method of the <i>cursor</i> and <i>connection</i> objects.<br>

    cur.close()
    conn.close()
#### Querying data using fetchone() method
For the demonstrations, use the <i>parts, vendors</i> and <i>vendor_parts</i> tables in the <i>suppliers</i> database that we created in the [Create Tables](#Create-Tables).<br>
The folowing <i>get_vendor()</i> function selects data from the <i>vendors</i> table and fetches the rows using the <i>fetchone()</i> method. (see query_data.py) <br>
#### Querying data using fetchall() method
The following <i>get_parts</i> function uses the <i>fetchall()</i> method of the cursor object to fetch rows from the result set and displays all the parts in the <i>parts</i> table. <br> (see query_data.py) <br>
#### Querying data using fetchmany() method
The following <i>get_suppliers()</i> function selects parts and vendors data using the <i>fetchmany()</i> method. (see query_data.py) <br>

---
## Store Procedures
To call a PostgreSQL stored procedure in a Python program, use the following steps:<br>
First, [Conect To PostgreSQL Database Server](#Connect-To-PostgreSQL-Database-Server) to the PostgreSQL database server by calling the <i>connect()</i> function of the psycopg2 module. <br>

    conn = psycopg2.connect(dsn)
The <i>connect()</i> method returns a new instance of the <i>connection</i> class.<br>
Next, create a new cursor by calling the <i>cursor()</i> method of the connection object.<br>
Next, create a new cursor by calling the <i>cursor()</i> method of the connection object.

    cur = conn.cursor()
Then, pass the name of stored procedure and the optional input values to the <i>callproc()</i> method of the cursor object.

    cur.callproc('stored_procedure_name: ', (value1, value2))
Internally, the <i>callproc()</i> method translates the stored procedure call and input values into the following statement:

    SELECT * FROM stored_procedured_name(value1, value2);
Therefore, you can use the <i>execute()</i> method of the cursor object to call a stored procedure as follows:

    cur.execute("SELECT * FROM stored_procedure_name(%s, %s); ", (value1, value2))
Both statements have the same effect.<br>
After that, process the result set returned by the stored procedure using the <i>fetchone(), fetchall()</i> or <i>fetchmany()</i> method.<br>
Finally, call the <i>close()</i> method of the <i>cursor</i> and <i>connection</i> objects to close the communication with the PostgreSQL database server.(see store_procedure.py)<br>

---
## Handling Blob Data
Standard SQL defines BLOB as the binary large object for storing binary data in the database. With the BLOB data type, you can store the content of a picture, a document, etc.tinto the table.<br>
PostgreSQL dose not support BLOB but you can use the BYTEA data type for storing the binary data. <br>
#### Insert BLOB into a table
To insert BLOB data into a table, you use the following steps:
<ul>
    <li>First, read data from a file.</li>
    <li>Next, Conect To PostgreSQL Database Server](#Connect-To-PostgreSQL-Database-Server)by creating a new connection object from the <i>connect()</i> function.</li>
    <li>Then, create a <i>cursor</i> object from the <i>connection</i> object.</li>
    <li>After that, execute the <b>INSERT</b> statement with the input values. For BLOB data, use the <b>Binary</b> object of the psycopg2 module.</li>
    <li>Finally, commit the changes permanently to the PostgreSQL database by calling the <i>commit()</i> method of the <i>connection</i> object.</li>
</ul>
The following <i>write_blob()</i> function reads binary data from a file specified by the <i>path_to_file</i> parameter and inserts it into the <i>part_drawings</i> table. (see handling_blob_data.py) <br>
#### Read BLOB in the table
The steps of reading BLOB from a table are similar to the steps of querying data from a table. After fetching binary data from the table, we can save to a file, output it to the web browser, etc.

---
## Delete Data
#### Steps for deleting data from the PostgreSQL table in Python
To delete data from the PostgreSQL table in Python, following steps:<br>
First, [Conect To PostgreSQL Database Server](#Connect-To-PostgreSQL-Database-Server) by calling the <i>connect()</i> function of the psycopg2 module. <br>

    conn = psycopg2.connect(dsn)
The <i>connect()</i> function returns a new <i>connection</i> object.<br>
Next, to execute any statement, you need a <i>cursor</i> object. To create a new cursor object, call the <i>cursor()</i> method of the connection object as follows:

    cur = conn.cursor()

Then, execute the <b>DELETE</b> statement. If you want to pass values to the <b>DELETE</b> statement, use the placeholders(%s) in the <b>DELETE</b> statement and pass input values to the second parameter of the <i>execute()</i> method.<br>
The <b>DELETE</b> statement with a placeholder for the value of the <i>id</i> field is as follows:

    DELETE FROM table_1 WHERE id=%s;
To bind value value_1 to the placeholder, you call the <i>execute()</i> method and pass the input value as a tuple to the second parameter like the following:

    cur.execute(delete_sql, (value_1,))
After that, save the changes to the database permanently by calling the <i>commit()</i> method of the <i>connection</i> object.

    conn.commit()
Finally, close the communication with the PostgreSQL database server by calling the <i>close()</i> method of the <i>cursor</i> and <i>connection</i> objects.
    
    cur.close()
    conn.close()
#### Example of deleting data in PostgreSQL table in Python
Use the <i>parts</i> table in the <i>suppliers</i> database that we created in the [Create Tables](#Create-Tables) for the sake of demonstration.<br>
The following <i>delete_part()</i> function deletes a row in the <i>parts</i> table specified by the <i>part_id</i>.(see delete data.py)<br>
Before testing the delete_part() function, we query data from the <i>parts</i> table as follows:

    suppliers=# SELECT * FROM parts;
     part_id |  part_name  
    ---------+-------------
           1 | SIM Tray
           2 | Specker
           3 | Vibrator
           4 | Antenna
           5 | Hone Button
           6 | LTE Modem
    (6 rows)

Now run the Python program to delete the part with the part id 1.<br>
Select data from the <i>parts</i> table again to confirm the deletion made by the Python program.

    suppliers=# SELECT * FROM parts;
     part_id |  part_name  
    ---------+-------------
           1 | SIM Tray
           3 | Vibrator
           4 | Antenna
           5 | Hone Button
           6 | LTE Modem
(After delete part_id=2)

---
## Reference
[Tutorial](https://www.postgresqltutorial.com/postgresql-python/)
