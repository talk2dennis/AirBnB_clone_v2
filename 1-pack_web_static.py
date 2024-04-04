#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
    web_static
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
        a fabfile task to pack the contents of folder into .tgz
    """

    # get the current time
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    
    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/web_static_{time}.tgz web_static/",
                   capture = True)
    if result.succeeded:
        return f"versions/web_static_{time}.tgz"
    else:
        return None
