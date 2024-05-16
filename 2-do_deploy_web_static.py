#!/usr/bin/python3
""" Packs webstatic into an archive """
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['54.196.38.185', '35.153.232.27']


def do_pack():
    """ Generates a .tgz archive from web_static """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    full_path = "web_static_" + date

    if not os.path.exists('./versions'):
        os.mkdir('./versions')

    local(f"tar -cvzf versions/{full_path}.tgz web_static")
    print(f"Packing web_static to versions/{full_path}.tgz")
    if os.path.getsize(f"versions/{full_path}.tgz"):
        size = os.path.getsize(f"versions/{full_path}.tgz")
        print(f"web_static packed: versions/{full_path} -> {size}Bytes")
        return f"{full_path}.tgz"
    return None


def do_deploy(archive_path):
    """ Distributes an archive to the webservers """
    if not os.path.exists(archive_path):
        return False
    try:
        file_n = archive_path.split("/")[-1]
        put(archive_path, f"/tmp/")
        name = file_n.split('.')
        path = "/data/web_static/releases/"
        run(f"mkdir -p /data/web_static/releases/{name[0]}")
        run(f"tar -xzf /tmp/{file_n} -C {path}{name[0]}")
        run(f"rm /tmp/{file_n}")
        run(f"mv /data/web_static/releases/{name[0]}/web_static/* \
    /data/web_static/releases/{name[0]}")
        run(f"rm -rf /data/web_static/releases/{name[0]}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {path}{name[0]}/ /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        return False
