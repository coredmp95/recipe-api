#!/bin/sh

set -e

envsubst < /etc/nginx/devault.conf.tpl > /etc/nginx/conf.d/default.conf
nginx -g 'deamon off;'
