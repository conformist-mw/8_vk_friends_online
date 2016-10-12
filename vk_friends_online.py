import vk


APP_ID = -1


def get_user_login():
    return input('Введите логин: ')


def get_user_password():
    return input('Введите пароль: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    ids = api.friends.getOnline()
    users = []
    for user in ids:
        users.append(api.users.get(user_ids=user)[0])
    return users


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
