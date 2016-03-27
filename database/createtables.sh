#!/bin/bash

source mysql.handyman.cfg

$(mysql -u${sys_user} -p ${db_name} < schema.sql)

if [ $? -eq 0 ]; then
    echo "${db_name} schema created"
else
    echo "Failed to create schema is ${db_name}"
fi
