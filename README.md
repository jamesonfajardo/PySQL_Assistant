![pysql](https://raw.githubusercontent.com/jamesonfajardo/PySQL_Assistant/master/pysql.png)

# PySQL_Assistant
PySQL_Assistant(python mysql assistant) is a module that makes it easy to query mysql using python

How to use:
1. Start by importing the module  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) import PySQL_Assistant**
    
2. Define a function (steps 3-5 will be inside this function)  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) def PySQL():**

3. Create 7 variables. Make the value empty if you won't be using it:  

    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) host = ''** `Your database host`  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) user = ''** `Your database username`  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) passwd = ''** `Your database password`  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) db = ''** `Your database name`  
    
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) query=''** `This will contain your queries. Always query using string interpolation {} and placeholders %s`  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) placeholder_value=''** `This will contain the value of the placeholders, must be always inside tuple`  
    **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) appends=''**  `This will contain the value of the interpolation`
    
4. Bind the object MYSQL_DBH (mysql database handler) to a var  
  **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, `query.format(appends)`, `placeholder_value`)**  
  ..4.1 Placeholders are necessary that's why there's a query and placeholder value  
  
5. Return DB_Query  
  **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) return qObj.DB_Query()**
  
6. Call the function (in this case PySQL)  
  **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) PySQL()**  
  **![#00FA9A](https://placehold.it/15/00FA9A/000000?text=+) print(PySQL())** --> optional, used to print success message


# Sample Queries
![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Create database`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = ''

        query = 'create database {}'
        placeholder_value = ''
        appends = 'pydb'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())



![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Create table`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'create table {}(name varchar(255), address varchar(255))'
        placeholder_value = ''
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())

    
    
![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Alter table`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'alter table {} add id int auto_increment primary key not null'
        placeholder_value = ''
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())

    
    
![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Insert 1 record`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'insert into {}(name, address) values(%s, %s)'
        placeholder_value = ('John', 'Highway 21')
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())





![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Insert multiple records`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'insert into {}(name, address) values(%s, %s)'
        placeholder_value = [
                              ('Peter', 'Lowstreet 4'),
                              ('Amy', 'Apple st 652'),
                              ('Hannah', 'Mountain 21'),
                              ('Michael', 'Valley 345'),
                              ('Sandy', 'Ocean blvd 2'),
                              ('Betty', 'Green Grass 1'),
                              ('Richard', 'Sky st 331'),
                              ('Susan', 'One way 98'),
                              ('Vicky', 'Yellow Garden 2'),
                              ('Ben', 'Park Lane 38'),
                              ('William', 'Central st 954'),
                              ('Chuck', 'Main Road 989'),
                              ('Viola', 'Sideway 1633')
                            ]
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())




![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Select all records`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'select * from {}'
        placeholder_value = ''
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    for x in PySQL():
            print(x)





![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Select with filter`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'select * from {} where id=%s'
        placeholder_value = (1,)
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    for x in PySQL():
            print(x)




![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Update record`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'update {} set name=%s where id=%s'
        placeholder_value = ('Harry Peter', 2)
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())




![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Delete record`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'delete from {} where address like %s'
        placeholder_value = ('%way%',)
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())



![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Truncate table`

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'truncate {}'
        placeholder_value = ''
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())




![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Drop table`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'drop table {}'
        placeholder_value = ''
        appends = 'customers'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())

    
    
    
![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Drop database`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'drop database {}'
        placeholder_value = ''
        appends = 'pydb'

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    print(PySQL())


![#1589F0](https://placehold.it/15/1589F0/000000?text=+) `Join tables`  

    import PySQL_Assistant

    def PySQL():

        host = 'localhost'
        user = 'root'
        passwd = ''
        db = 'pydb'

        query = 'select products.name as product, customers.name as customer, customers.address as address \
                 from customers \
                 inner join products \
                 on customers.id=products.id;'
        placeholder_value = ''
        appends = ''

        qObj = PySQL_Assistant.MYSQL_DBH(host, user, passwd, db, query.format(appends), placeholder_value)
        return qObj.DB_Query()

    for x in PySQL():
        print(x)


