#!/bin/bash

# MySQL root/admin username and password
sys_user="root"

# The handyman database name, user, and password to use
db_name="handyman"
db_user="handy_user"
db_pass="handy_pass"

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
