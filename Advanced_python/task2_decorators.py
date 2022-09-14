has_login = True
def check_login(func):
    def wrapper():
        if has_login:
            return func()
        else:
            raise Exception('user not logged in')
    return wrapper

@check_login
# this is a decorator that returns a function
def show_dashboard():
    print('This is dashboard')

# check_login(show_dashboard)
# wrapper function
@check_login
def show_friend_list():
    return['abcd', 'dfgj']
print(show_friend_list())

