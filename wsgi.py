import sys

# Expand Python classes path with your app's path
sys.path.append('F:\ezzhiwa_git\learn_web_front\personal_com_project')

from web import app

# put logging code (and imports) here ...

# Initialize WSGI app object
application = app

# import sys
# # from web import app as application
#
# # Expand Python classes path with your app's path
# sys.path.index(0, "F:\ezzhiwa_git\learn_web_front\personal_com_project")
#
# from web import app
#
# # put logging code (and imports) here ...
#
# # Initialize WSGI app object
# application = app
