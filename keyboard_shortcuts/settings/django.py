import environ

root = environ.Path(__file__) - 3  # root of project
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(root() + "/.env")  # reading .env file

# Build paths inside the project like this: BASE_DIR / ...
BASE_DIR = root()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")
SITE_ID = env.int("SITE_ID")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
