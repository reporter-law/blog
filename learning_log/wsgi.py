import os,sys
path = '/home/caowang123/blog' # 在这里使用你自己的用户名和GitHub项目的名字。
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'learning_log.settings' # 在这里mysite请用settings所在文件夹名，我用的是和GitHub仓库名一样的名字
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
