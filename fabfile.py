from fabric.api import local

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
    min_css()
    local('s3cmd sync -c ~/.s3cmd-marc _build/ s3://marc.weistroff.net -P')
