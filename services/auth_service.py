import dropbox


def auth_user(auth_token):
    try:
        dbx = dropbox.Dropbox(auth_token)
        return dbx.users_get_current_account()
    except:
        return 'Unable to auth user'
