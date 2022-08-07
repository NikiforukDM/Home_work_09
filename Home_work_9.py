phone_numbers_dict = {}


def input_error(func):

    def inner(command):

        try:
            func(command)
            return func

        except KeyError:
            print(f'Name is not in phonebook. Try another one.')

        except ValueError:
            print('Phone number must be digit')

        except IndexError:
            print("After command 'add' give me name and phone number please")
            print("After command write name and phone number please")

    return inner


def greeting():

    print('How can I help you?')


@input_error
def adder(command: str) -> dict[int]:
    edit_command = command.split(' ')

    if len(edit_command) == 3 and edit_command[-1].isdigit():
        phone_numbers_dict.update({edit_command[-2]: edit_command[-1]})
        print(phone_numbers_dict)
        print(f'{edit_command[-2]} was added to phonebook')
        return phone_numbers_dict

    elif len(edit_command) != 3:
        raise IndexError

    elif not edit_command[-1].isdigit():
        raise ValueError


@input_error
def changer(command):
    edit_command = command.split(' ')

    if edit_command[-2] in phone_numbers_dict and edit_command[-1].isdigit():
        phone_numbers_dict[edit_command[-2]] = edit_command[-1]
        print(phone_numbers_dict)
        print(
            f"{edit_command[-2]}'s phone number was changed on {edit_command[-1]}")
        return phone_numbers_dict

    elif len(edit_command) <= 2:
        raise IndexError

    else:
        raise ValueError

        raise KeyError


@input_error
def phoner(command):
    edit_command = command.split(' ')

    if edit_command[-1] in phone_numbers_dict:
        print(phone_numbers_dict[edit_command[-1]])

    else:
        raise KeyError


def show_all(command):
    print(phone_numbers_dict)


def goodbyer(command):
    if "goodbye" in command.lower() or 'close' in command.lower() or 'exit' in command.lower():
        print('Good bye!')

    print('Good bye!')


def main():
    while True:

        command = input('Enter your command:')

        if 'hello' in command.lower():
            greeting()

        elif 'add' in command.lower():
            adder(command)

        elif 'change' in command.lower():
            changer(command)

        elif 'phone' in command.lower():
            phoner(command)

        elif 'show all' in command.lower():
            show_all(command)

        elif "goodbye" in command.lower() or 'close' in command.lower() or 'exit' in command.lower():
            goodbyer(command)
            break

        else:
            print('The command is not correct. Try again.')


if __name__ == '__main__':
    main()
