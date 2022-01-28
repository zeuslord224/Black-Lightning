import os

if ENV := bool(os.environ.get("ENV", False)):
    from heroku_config import Var as config
else:
    from localconfig import config


Var = config
