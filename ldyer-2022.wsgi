import sys
import os

sys.path.extend([
    "/var/student-webapps/src/ldyer-2022/",
    "/var/www/.local/lib/python3.8/site-packages"])

os.chdir("/var/student-webapps/src/ldyer-2022/")
import app
application = app.app
