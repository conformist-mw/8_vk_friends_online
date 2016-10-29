import vk
from getpass import getpass


APP_ID = -1


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass(prompt='Password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    return [api.users.get(user_ids=x)[0] for x in api.friends.getOnline()]


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print('\t{} {}'.format(friend['first_name'], friend['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    if login and password:
        friends_online = get_online_friends(login, password)
        if friends_online:
            print('Друзья онлайн:')
            output_friends_to_console(friends_online)
        else:
            print('Друзей онлайн нет :(')
    else:
        print('Данные введены неверно')
