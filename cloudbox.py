#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import getpass
import easywebdav



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Sync a directory with WebDAV')

    parser.add_argument('-U', '--url', metavar='URL',
                        help='WebDAV URL to sync', required=True)
    parser.add_argument('-u', '--user', metavar='user', default=getpass.getuser(),
                        help='Username to login to WebDAV', required=False)
    parser.add_argument('-p', '--password', metavar='password', default=False,
                        help='Password to login to WebDAV', required=False)


    args = parser.parse_args()


    webdav = easywebdav.connect(args.url, username=args.user, password=(args.password or getpass.getpass()))

    webdav.ls()


# vim:fdm=marker:ts=4:sw=4:sts=4:ai:sta:et
