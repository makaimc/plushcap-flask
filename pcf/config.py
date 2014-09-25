import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        var_set = environ[setting]
        if var_set == 'true' or var_set == 'True':
            return True
        elif var_set == 'false' or var_set == 'False':
            return False
        return var_set
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise Exception(error_msg)


# general Flask app settings
DEBUG = get_env_setting('DEBUG')
SECRET_KEY = get_env_setting('SECRET_KEY')
