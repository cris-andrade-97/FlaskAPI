import mysql.connector as conector

conexion = conector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="instrumentosdb",
    auth_plugin='mysql_native_password'
)
