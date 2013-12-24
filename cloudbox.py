#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import getpass
import easywebdav

class RemoteDir(object):
    """docstring for RemoteDir"""
    def __init__(self, dav_host, username, password, protocol):
        super(RemoteDir, self).__init__()
        #self.arg = arg
        self.webdav = easywebdav.connect(dav_host, username=username, password=password, protocol=protocol)


    def walk(self, dav_path):
        """docstring for walk"""
        self.webdav.cd(dav_path)

        for f in self.webdav.ls():
            if f.contenttype.split('+')[0] == 'httpd/unix-directory' and f.name != dav_path:
                self.walk(f.name)
            else:
                print f.name


#class LocalDir(object):
#    """docstring for LocalDir"""
#    def __init__(self, directory):
#        super(Local, self).__init__()
#        self.directory = directory



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Sync a directory with WebDAV')

    parser.add_argument('-U', '--url', metavar='URL',
                        help='WebDAV URL to sync', required=True)
    parser.add_argument('-D', '--dir', metavar='DIRECTORY',
                        help='Directory to sync', required=True)

    parser.add_argument('-u', '--user', metavar='user', default=getpass.getuser(),
                        help='Username to login to WebDAV', required=False)
    parser.add_argument('-p', '--password', metavar='password', default=False,
                        help='Password to login to WebDAV', required=False)


    args = parser.parse_args()


    (protocol, full_path) = args.url.split('://')
    try:
        (dav_host, dav_path ) = full_path.split('/',1)
    except ValueError:
        (dav_host, dav_path ) = (full_path, '/')

    webdav = RemoteDir(dav_host, username=args.user, password=(args.password or getpass.getpass()), protocol=protocol)

    webdav.walk(dav_path)



# vim:fdm=marker:ts=4:sw=4:sts=4:ai:sta:et
