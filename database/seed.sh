#!/bin/bash

mysql -uroot test <<EOF
INSERT INTO clerks (id,
                    login,
                    first_name,
                    last_name,
                    password)
  VALUES (22,
          'bob22',
          'bob',
          'winter',
          'mypassword3');
EOF
