import vk
import time


APP_ID = 5648564


def get_vk_api(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    return vk.API(session)


def get_user_login():
    return input('Enter your login: ')


def get_user_password():
    return input('Enter your password: ')


def get_online_friends(login, password):
    api = get_vk_api(login, password)
    return api.friends.getOnline()


def output_friends_to_console(friends_online):
    api = get_vk_api(login, password)

    print('Friends online:')
    for friend_id in friends_online:
        friend = api.users.get(user_ids=friend_id)[0]
        print(friend['first_name'], friend['last_name'])
        # applications should not send more than three requests per second
        time.sleep(0.35)

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except vk.exceptions.VkAuthError as error:
        print('Invalid login or password.')
        exit()
    output_friends_to_console(friends_online)
