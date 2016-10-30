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
# Что не так

# Код стал короче, читать его проще, и сразу всплыла вот эта интересная строка:
# [api.users.get(user_ids=x)[0] for x in api.friends.getOnline()]
# замечал что скрипт работает как-то не шустро? название user_id*s* тебя,
# случаем, не смущает ?

# Ну в общем эта строка замена переменной, которая по сути получается лишней:
# users = api.friends.getOnline()
# и дальше проходим по полученному списку. Разницу в скорости
# не заметил. Почему изменил:
#  — в прошлом замечании был совет использовать map — но он тут не совсем
# удобен, ведь чтобы его использовать, лучше бы завести отдельную функцию для
#  api.users.get(id), но в эту функцию тогда нужно ещё
# как-то передать и объект api.
# По поводу user_ids — это не мной придуманная опция метода users.get
# (https://vk.com/dev/users.get) и тут я полностью согласен с замечанием,
# название выбрано так себе. Но не мне его изменять :(


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
