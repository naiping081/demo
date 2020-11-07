import pymysql

# create database heima charset=utf8;
# create table goods(id int unsigned primary key not null auto_increment,name varchar(20) not null unique,price decimal(7,2));

class sp(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='mysql',
                                    database='heima', port=3306, charset='utf8')
    @staticmethod
    def menu():
        print("------商品管理系统------")
        print('1:添加商品')
        print('2.查询商品')


    def add(self):
        '''商品名称、单价，若全部输入正确，
        将该商品名和单价信息存入数据库，
        提示“添加成功”并返回主页面；
        若数据库中已存在该商品名，提示“该商品已存在, 请重新添加!”；'''
        name = input('请输入商品名称')
        cursor = self.conn.cursor()
        sql = 'select * from heima where name=%s;'
        count = cursor.execute(sql,(name,))
        if count==0:
            price=input('请输入价格')
            try:
                sql = 'insert into heima(name,price) value(%s,%s);'
                cursor.execute(sql,(name,price))
                self.conn.commit()
            except Exception as x:
                print(x)
                self.conn.rollback()
                print('添加失败')
        else:
            print('姓名已经存在')
        cursor.close()
        self.conn.close()


    def search(self):
        while True:
            name = input('输入查询商品名称')
            cursor=self.conn.cursor()
            sql = 'select * from heima where name=%s;'
            count = cursor.execute(sql,(name))
            if count:
                print(cursor.fetchone())
                cursor.close()
                self.conn.close()
                return
            else:
                print('商品名称有误请重新输入')






    def strat(self):
        while True:
            self.menu()
            but = input('请输入功能对应的序列号：')

            if but=='1':
                self.add()
            elif but=='2':
                self.search()


if __name__ == '__main__':
    w=sp()
    w.strat()
    print('哈哈哈哈')
