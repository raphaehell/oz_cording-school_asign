import pymysql

# 데이터베이스 연결 설정
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='airbnb')

try:
    # 커서 생성
    with connection.cursor() as cursor:
        # 문제 1 새로운 제품 추가
        sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('Python Book', 29.99, 50))
        connection.commit()

        #문제 2 고객 목록 조회
        sql = "SELECT * FROM Customers"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

        #문제 3 제품 재고 업데이트
        sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
        cursor.execute(sql, (1,1))
        connection.commit()
        
        #문제 4 고객벽 총 주문 금액 계산
        sql = "SELECT customerID, sum(totalAmount) FROM Orders group by customerID"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)

        #문제 5 고객 이메일 업데이트
        sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
        cursor.execute(sql, ('update@update.com',1))
        connection.commit()

        #문제 6 주문 취소
        sql = "DELETE FROM Orders WHERE orderID=%s"
        cursor.execute(sql, (15))
        connection.commit()

        #문제 7 특정 제품 검색
        sql = "SELECT * FROM Products where productName like %s"
        cursor.execute(sql,('%book%'))
        result = cursor.fetchall()
        for data in datas:
            print(data['productName'])

        #문제 8 특정 고객의 모든 주문 조회
        sql = "SELECT * FROM Orders where customerID=%s"
        cursor.execute(sql,(1))
        result = cursor.fetchall()
        for data in data:
            print(data)

        #문제 9 가장 많이 주문한 고객 찾기
        sql = "SELECT customerID, count(*)as orderCount From order group bycustomerID order by ordercount desc limit 1"
        cursor.execute(sql)
        data - cursor.fetchone()
        print(data)
        
# 결과 받아오기
        #result = cursor.fetchall()
        #print(result)

finally:
    # 데이터베이스 연결 종료
    connection.close()