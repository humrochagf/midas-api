import os

from .dirs import CONF_DIR

# common settings
common_settings = os.path.join(CONF_DIR, 'common.py')
exec(open(common_settings).read())

# app settings
app_settings = os.path.join(CONF_DIR, 'app.py')
exec(open(app_settings).read())

# local settings
local_settings = os.path.join(CONF_DIR, 'local.py')
exec(open(local_settings).read())
