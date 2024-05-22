import sqlite3 as sl
baseInfo = sl.connect('base_info.db')
cursor = baseInfo.cursor()
# with baseInfo:
#     baseInfo.execute("DROP TABLE IF EXISTS financialAccounting")

with baseInfo:
    baseInfo.execute("""
        CREATE TABLE IF NOT EXISTS financialAccounting (
                     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     product TEXT,
                     spended FLOAT,
                     income FLOAT,
                     overall FLOAT
        );
""")


table = True
while table:
        deleteInput = input("Если хочешь удалить таблицу напиши delete Or ignote to continue: ")
        if deleteInput.lower() == "delete":
            with baseInfo:
                baseInfo.execute("DROP TABLE IF EXISTS financialAccounting")
                exit()

        warning = input("If you wanna leave write 'quite' Or  ignore to continue: ")
        
        if warning.lower() == 'quite':
            table = False
        else:
            userProduct = input("product: ")
            try:
                userSpended = float(input("spended: "))
            except ValueError:
                 print("Введите только сумму в виде сумма.сумма")
                 continue
            try: 
                userIncome = float(input("income: "))
            except ValueError:
                 print("Введите только сумму в виде сумма.сумма")
                 continue
            userOverall = userIncome - userSpended
            print(f'У тебя имеется {userOverall} денег')
            sql = 'INSERT INTO financialAccounting(product,spended,income,overall)  VALUES(?,?,?,?)'
            data = [
                (userProduct,userSpended,userIncome,userOverall)
            ]
            with baseInfo:
                baseInfo.executemany(sql,data)
            with baseInfo:
                result = baseInfo.execute("SELECT * FROM financialAccounting")
                for row in result:
                    print(row)
            warning2 = input("Write 'open' to open table file: ")
            if warning2.lower() == "open":
                with open("troll.text","w",encoding="utf-8") as file:
                    content = file.write("Скачай спец приложение чтобы открыть таблицу")
                    print("Был создай файл troll.text,поищи его")
baseInfo.commit()
baseInfo.close()

