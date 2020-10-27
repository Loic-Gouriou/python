from datetime import datetime

def test(text):



    f = open ('phonebook.log', 'a')

    date = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
    f.write(f'{date} {text} \n')

    f.close()

def dump_log():

    f = open ('phonebook.log', 'r')

    line = f.readline()

    while line :
        print(line)
        line = f.readline()
    f.close()