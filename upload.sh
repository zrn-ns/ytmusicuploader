#! /bin/sh

DIR=$(cd $(dirname $0); pwd)
MEDIA_FILE_NAME=$1

${DIR}/venv/bin/python ${DIR}/upload.py $MEDIA_FILE_NAME
