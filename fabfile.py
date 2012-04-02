from boto.s3.connection import S3Connection
from boto.s3.key import Key
from fabric.api import *
from fabric.colors import *
from fabric.contrib import *
from time import gmtime, strftime
import os

def upload_s3():
    conn = S3Connection(os.getenv('AWS_ID'), os.getenv('AWS_SECRET'))
    bucket = conn.get_bucket('marcw-blog')
    key = Key(bucket)
    filename = 'static/all.css'
    key.key = filename
    fid = file(filename, 'r')
    key.set_contents_from_file(fid)
    key.set_acl('public-read')

    key = Key(bucket)
    filename = 'static/bootstrap.min.js'
    key.key = filename
    fid = file(filename, 'r')
    key.set_contents_from_file(fid)
    key.set_acl('public-read')

def min_css():
    local('lessc static/all.less | yuicompressor --type=css -o static/all.css')

def clean():
    local('rm static/all.css')
    local('rm -rf _build/*')

def serve():
    clean()
    min_css()
    local('run-rstblog serve')

def build():
    clean()
    min_css()
    local('run-rstblog build')

def deploy():
    build()
    upload_s3()
    local('rsync -a _build/ sheep01:/var/www/marc.weistroff.net')
