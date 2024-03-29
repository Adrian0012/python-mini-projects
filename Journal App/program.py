import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-----------------------')
    print('     Journal APP       ')
    print('-----------------------')


def run_event_loop():
    print('What do you want to do with your journal? ')
    cmd = 'EMPTY!!'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd entries, E[x]it ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("{} is an Invalid Command".format(cmd))

    print('Done!!')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entries(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


print('__file__ ' + __file__)
print('__name__ ' + __name__)

if __name__ == '__main__':
    main()
