
import os
from time import time

from prettyprinter import pprint
try:
    import aiomysql
    import asyncio
except:
    os.system("pip3 install PyMySQL")
    os.system("pip3 install aiomysql")
    os.system("pip3 install asyncio")


try:
    import configparser
except:
    os.system("pip3 install configparser")


config = configparser.ConfigParser()
chpath = os.path.dirname(os.path.realpath('__file__')) + "/config/config.ini"
config.read(chpath)


user = config['DATABASE']['user']
password = config['DATABASE']['password']
host = config['DATABASE']['host']
database = config['DATABASE']['database']


async def register():
    """ 初始化，获取数据库连接池
    Raises:
        asyncio.CancelledError: _description_
    Returns:
        _type_: _description_
    """

    try:

        pool = await aiomysql.create_pool(host=host, port=3306,
                                          user=user, password=password,
                                          db=database, charset='utf8')
        print("succeed to connect db!")
        return pool
    except asyncio.CancelledError:
        raise asyncio.CancelledError
    except Exception as ex:
        print("mysql数据库连接失败：{}".format(ex.args[0]))
        return False


async def getCurosr(pool):
    """获取db连接和cursor对象，用于db的读写操作

    Args:
        pool (_type_): _description_

    Returns:
        _type_: _description_
    """
    conn = await pool.acquire()
    cur = await conn.cursor()
    return conn, cur


async def batchInsert(pool, sql, values):
    """批量写入操作

    Args:
        pool (_type_): _description_
        sql (_type_): _description_
        values (_type_): _description_

    Returns:
        _type_: _description_

    # loop = asyncio.get_event_loop()
    # pool = loop.run_until_complete(register())  
    # 批量插入
    # records = [('一灰灰1', 'asdf', 0, int(time.time()), int(time.time())),
    #         ('一灰灰2', 'qwer', 0, int(time.time()), int(time.time()))]
    # sql = "insert into user(`name`, `pwd`, `isDeleted`, `created`, `updated`) values (%s, %s, %s, %s, %s)"
    # task = asyncio.ensure_future(batchInsert(pool, sql, records))
    # result = loop.run_until_complete(task)
    # print("insert res:", result)    
    # 最后关闭连接
    # loop.run_until_complete(close(pool))
    # loop.close() 
    """
    start = time()
    # 第一步获取连接和cursor对象
    conn, cur = await getCurosr(pool)
    try:
        # 执行sql命令
        await cur.executemany(sql, values)
        await conn.commit()
        # 返回sql执行后影响的行数
        return cur.rowcount
    finally:
        # 最后不能忘记释放掉连接，否则最终关闭连接池会有问题
        await pool.release(conn)
        print("execute insert cost: ", time() - start)


async def query(pool, sql):
    """查询, 一般流程是首先获取连接，光标，获取数据之后，则需要释放连接

    Args:
        pool (_type_): _description_
        sql (_type_): _description_

    Returns:
        _type_: _description_

    # loop = asyncio.get_event_loop()
    # pool = loop.run_until_complete(register())

    # # 开始增删改查操作

    # # 查询
    # start = now()
    # tasks = [
    #     asyncio.ensure_future(query(pool, 'select * from user where id<3 order by id desc limit 2')),
    #     asyncio.ensure_future(query(pool, 'select * from user where id<7 order by id desc limit 2')),
    #     asyncio.ensure_future(query(pool, 'select * from user where id<9 order by id desc limit 2')),
    # ]
    # result = loop.run_until_complete(asyncio.gather(*tasks))
    # print("total cose: ", now() - start)
    # for res in result:
    #     print("record: ", res)

    # # 最后关闭连接
    # loop.run_until_complete(close(pool))
    # loop.close()
    """

    conn, cur = await getCurosr(pool)
    try:
        await cur.execute(sql)
        return await cur.fetchall()
    finally:
        await pool.release(conn)


async def close(pool):
    """关闭连接

    Args:
        pool (_type_): _description_
    """
    pool.close()
    await pool.wait_closed()
    print("close pool!")
