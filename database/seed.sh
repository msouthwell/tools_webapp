#!/bin/bash

source mysql.handyman.cfg

$(mysql -u${sys_user} -p ${db_name} <<EOF
# ### BEGIN SEED

# Clerks
INSERT INTO clerks (login, first_name, last_name, password)
VALUES ("arta", "Art", "Anderson", "arta");

INSERT INTO clerks (login, first_name, last_name, password)
VALUES ("bobb", "Bob", "Baker", "bobb");

INSERT INTO clerks (login, first_name, last_name, password)
VALUES ("cabc", "Cab", "Calloway", "cabc");

# Customers
#INSERT INTO customers (email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number)
#VALUES ("xavier@xmen.com", "Charles", "Xavier", "xavier", "Professor Xavier's School for the Gifted", "1", "1234567890", "1", "2345678901");
#
#INSERT INTO customers (email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number)
#VALUES ("yolandi@derantwood.com", "Yolandi", "Visser", "yolandi", "District 9", "27", "111234567", "27", "821234567");
#
#INSERT INTO customers (email, first_name, last_name, password, address, work_phone_cc, work_phone_number, home_phone_cc, home_phone_number)
#VALUES ("zorro@swords.com", "Zorro", "Zoroaster", "zorro", "Parts Unknown", "52", "12345678", "52", "23456789");
#
# Categories
#INSERT INTO categories (category, has_accessories)
#VALUES("Hand Tools", FALSE);
#
#INSERT INTO categories (category, has_accessories)
#VALUES("Construction Equipment", FALSE);
#
#INSERT INTO categories (category, has_accessories)
#VALUES("Power Tools", TRUE);
#
### Tools
#INSERT INTO tools (short_description, full_description, deposit, day_price, original_price, category_id)
#VALUES("Hammer", "Normal Hammer", 1.00, 1.00, 1.00, 1);
#
#INSERT INTO tools (short_description, full_description, deposit, day_price, original_price, category_id)
#VALUES("Claw Hammer", "A hammer with a claw", 1.00, 1.25, 1.25, 1);
#
#INSERT INTO tools (short_description, full_description, deposit, day_price, original_price, category_id)
#VALUES("Jackhammer", "Gas powered and big", 100.00, 100.00, 1000.00, 2);
#
#INSERT INTO tools (short_description, full_description, deposit, day_price, original_price, category_id)
#VALUES("Planer", "Planes wood", 5.00, 50.00, 500.00, 3);
#
#INSERT INTO tools (short_description, full_description, deposit, day_price, original_price, category_id)
#VALUES("Sawzall", "Sawzall and accessories", 5.00, 50.00, 250.00, 3);
#
## TOOL ACCESSORIES
#INSERT INTO tool_accessories (tool_id, description)
#VALUES(5, "Mitre box");
#
#INSERT INTO tool_accessories (tool_id, description)
#VALUES(5, "Extra blades");
#
# ### END SEED

EOF
);
