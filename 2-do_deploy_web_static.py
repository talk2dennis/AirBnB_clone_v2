#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
    web_static
"""


from fabric.api import *
from datetime import datetime
import time
import os


env.hosts = ["54.197.44.251", "34.207.121.185"]


def do_pack():
    """
        a fabfile to pack the contents of folder into .tgz
    """

    # get the current time
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/web_static_{time}.tgz web_static/")
    if result.succeeded:
        return f"versions/web_static_{time}.tgz"
    else:
        return None


def do_deploy(archive_path):
    """
        a fabfile to unpack .tgz file and upload to the remote server
    """
    f_name = archive_path.split('/')[-1]
    p_name = f_name.split('.')[0]
    dest = f"/data/web_static/releases/{p_name}"
    if os.path.exists(archive_path):
        put(archive_path, "/tmp/")
        run(f"sudo mkdir -p {dest}")
        run(f"sudo mkdir -p /data/web_static/current")
        run(f"sudo tar -xzf /tmp/{f_name} -C {dest}")
        run(f"sudo rm /tmp/{f_name}")
        run(f"sudo mv {dest}/web_static/* {dest}")
        run(f"sudo rm -rf {dest}/web_static")
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -sf {dest}/ /data/web_static/current")
        print("New version deployed!")
        return True
    else:
        return False
