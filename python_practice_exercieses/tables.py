"""Make a time table acript that ask user the following things:
    1- how many tables you want to print
    2- what should be user starting point
    3 = ending point point of table

    NOTE: tables should be print horizentally """

if __name__ == "__main__":
    table_no = int(input('Enter table no: '))
    start = int(input('starting point of table: '))
    end = int(input('Ending point of table: '))

    for i in range(start, end + 1):
        for table in range(1, table_no + 1):
            print(f"{table} x {i} = {table_no * i} ", end='\t')
        print()
