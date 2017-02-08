
from datetime import datetime
import platform
from flask import render_template
from example import APP

@APP.route('/')
def home():
    """
    The home page
    """
    return render_template(
        'index.html',
        thetime=datetime.now(),
        container_info=platform.node())
