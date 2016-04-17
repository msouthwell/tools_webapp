# Final Testing

In preparation for the final TA presentation on Saturday 04/23/2016 from 9:00AM - 9:30AM EDT via Webex.

While testing, make sure to modify your database.json file accordingly and watch MySQL workbench to make sure the queries will be readable by the TA grader.

When testing, fill in if the test passed or failed, and the steps you took. If the test failed, file an issue on Github.

Also, before testing, drop and re-seed `handyman` db so that we are all working with the same dataset.

| Test                     | Pass | Fail | Steps                                                                                                                                                                                                 |
|--------------------------|------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Customer Login           | x    |      | Started server, visited `/login`, username 'xavier@xmen.com', password 'xavier'. Was then taken to `/customer_main_menu`                                                                              |
| Clerk Login              | x    |      | Started server, visited `/login`, selected clerk, username 'cabc', password 'cabc'. Was then taken to `clerk_main_menu`                                                                               |
| Pickup                   | x    |      | Logged in as clerk, uses reservation id 1, checked tool details 1, enter cc # '123456', exp date: '05/12/2016', saw rental contract successfully                                                      |
| Drop off                 | x    |      | Logged in as clerk, used reservation id 1, was presented with handyman tools rental receipt                                                                                                           |
| Inventory Report         | x    |      | Logged in as clerk, selected generate report, Inventory report, saw Inventory table                                                                                                                   |
| Customer Report          |      |      |                                                                                                                                                                                                       |
| Clerk Report             | x    |      | Logged in as clerk, selected generate report, clerk report, saw clerk table with pick up and drop off information. Currently all that data is zero. We should see the database with some information. |
| Hold for Repair          |      |      |                                                                                                                                                                                                       |
| Sell Tool                |      |      |                                                                                                                                                                                                       |
| Add Tool                 |      |      |                                                                                                                                                                                                       |
| Generate Rental Contract |      |      |                                                                                                                                                                                                       |
| Customer Main Menu       |      |      |                                                                                                                                                                                                       |
| New Profile              |      |      |                                                                                                                                                                                                       |
| View Profile             |      |      |                                                                                                                                                                                                       |
| Check Available Tools    |      |      |                                                                                                                                                                                                       |
| Make Reservation         |      |      |                                                                                                                                                                                                       |
| Final Reservation        |      |      |                                                                                                                                                                                                       |
| View Reservation         |      |      |                                                                                                                                                                                                       |
| View Tool Details        |      |      |                                                                                                                                                                                                       |
