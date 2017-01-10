#!/bin/bash

host="delatech-web00"
project_path="/var/www/marc.weistroff.net"
user="web"
key_filename="/Users/marc/.ssh/web-deploy"
dry_run="--dry-run"
assets_differ=""

if [ "$1" == "force" ]
then
    dry_run=""
fi

function say {
    echo -e ""
}

function say_red {
    echo -e "\033[31m>>> $@\033[0m"
}

function say_green {
    echo -e "\033[32m>>> $@\033[0m"
}

function say_yellow {
    echo -e "\033[33m>>> $@\033[0m"
}

function rsync_files {
    say_yellow "Rsyncing to remote"
    exclude="--exclude-from=rsync-exclude.txt"
    options="--no-owner --no-group --progress -crDpLt --force --delete --verbose"
    cd _site/
    rsync ${dry_run} ${exclude} ${options} ./ ${user}@${host}:${project_path}
    cd -
}
bundle exec jekyll build
rsync_files
