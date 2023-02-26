import sqlite3
from colorama import Fore, Style


def check_table():

    conn = sqlite3.connect('scan_results.db')
    # create a cursor
    cursor = conn.cursor()

    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='scan_results' ''')

    if cursor.fetchone()[0]==1 :
        gen_report()
    else:
        print(Fore.RED + "ERROR: Table not found" + Style.RESET_ALL)
        print('Please run the scanner to generate the table')

    conn.commit()

    conn.close()


def gen_report():
    # connect to the database
    conn = sqlite3.connect('scan_results.db')

    # create a cursor
    cursor = conn.cursor()

    # execute a SELECT statement
    cursor.execute('SELECT ip_address, port, state, alive, latency FROM scan_results')

    # get the results
    results = cursor.fetchall()

    # print the results
    print('IP Address, Port, state, alive, latency ')
    print(results)

    usr_input = str(input('Would you like to delete the results, Yes/No? : '))
    if usr_input.lower() == 'yes':
            # drop table to clean up
            cursor.execute('DROP TABLE scan_results')

    # close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    check_table()