#!/usr/bin/python3
""" This is a fabfile script pushes the webstatic archive to the webserver
    and decompresses it.
"""

from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['18.212.210.50', '54.89.116.191']


def do_deploy(archive_path):
    """ This function uploads the archive file and decompresses it to right
     folders in the server."""
    fil = archive_path[8:]
    filename = archive_path[8:-4]
    upload = put(archive_path, "/tmp/")
    if upload.failed:
        return False
    run("mkdir -p /data/web_static/releases/{}/".format(filename))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
        fil, filename))
    run("mv /data/web_static/releases/{0}/web_static/* /data/\
web_static/releases/{0}/".format(filename))
    run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
    run("rm /tmp/{}".format(fil))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
        filename))
    print("New version deployed!")
    return True
