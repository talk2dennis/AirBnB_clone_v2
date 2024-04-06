#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the contents of the
    web_static
"""


from fabric.api import *
from datetime import datetime
import os


env.user = "ubuntu"
env.hosts = ["54.197.44.251", "34.207.121.185"]


def do_pack():
    """
        a fabfile to pack the contents of folder into .tgz
    """

    # get the current time
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    result = local(f"tar -cvzf versions/web_static_{time}.tgz web_static/",
                   capture=True)
    if result.succeeded:
        return f"versions/web_static_{time}.tgz"
    else:
        return None


def do_deploy(archive_path):
    """
        a fabfile to unpack .tgz file and upload to the remote server
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except:
        return False

def deploy():
    """
        creates and distributes an archive to your web servers,
            using the function deploy
    """
    try:
        archive_path = do_pack()
        return do_deploy(archive_path)
    except:
        return False
