import vk
from getpass import getpass


APP_ID = 5648564


def get_user_login():
    return input('Enter your login: ')


def get_user_password():
    return getpass('Enter your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    return api.users.get(user_ids=friends_online_ids)


def output_friends_to_console(friends_online):
    print('Friends online:')
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError as error:
        print('Invalid login or password.')
        exit()
    else:
        output_friends_to_console(friends_online)
