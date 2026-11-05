import setup_variables as setvar

def log_in_admin(username_log_in, password_log_in):
    if username_log_in == setvar.admin_username and password_log_in == setvar.admin_password:
        return True
    return False

def log_in_pengguna(username_log_in, password_log_in):
    for data_test in setvar.data_akun:
        if username_log_in == data_test and password_log_in == setvar.data_akun[data_test]:
            return True
    return False