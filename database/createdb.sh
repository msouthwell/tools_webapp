#!/bin/bash

source mysql.handyman.cfg

# Check for existence, create if it does not exist
echo "Checking if $db_name exists..."

if [ "`mysql -u${sys_user} -p -e "SHOW DATABASES;" | grep ${db_name}`" ==  "${db_name}" ]; then
    echo "${db_name} exists"
else
    echo "${db_name} does not exist"

    $(mysql -u${sys_user} -p -e "CREATE DATABASE ${db_name};")
    
    if [ $? -eq 0 ]; then
        echo "${db_name} created"
    else
        echo "Failed to create ${db_name}"
    fi
fi
