
import os
try:
    import pymysql
except:
    os.system("pip3 install PyMySQL")


try:
    import configparser
except:
    os.system("pip3 install configparser")



class MysqlHelper(object):
    conn = None

    def __init__(self):
        config = configparser.ConfigParser()
        chpath = os.path.dirname(os.path.realpath('__file__')) + "/config/config.ini"
        config.read(chpath)
        user = config['DATABASE']['user']
        password = config['DATABASE']['password']
        host = config['DATABASE']['host']
        database = config['DATABASE']['database']
        
        self.host = host
        self.username = user
        self.password = password
        self.db = database
        self.charset = 'utf8'
        self.port = 3306

    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.username,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset)

        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql, params=()):
        list_data = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list_data = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list_data

    def delete_one(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
            
    def addAll(self, tableName,data):
    		#获取字段
        field = []
        for key in data[0]:
            field.append("`"+key+"`")
        addAllArr =  []
        for x in data:
            addAllArr.append(str(tuple(x.values())))
        addAllArr = tuple(addAllArr)
        sql = """ INSERT INTO `%s` (%s) VALUES %s """ % (tableName, ','.join(field), ','.join(tuple(addAllArr)))
        sql = sql.replace('None', 'null')
        self.connect()
        self.cursor.execute(sql)
        self.conn.commit()
        self.close()

