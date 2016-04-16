%#template for viewing a customer profile % rebase('layout.tpl', title="Customer Profile")
<div class="container">
    <h2>Customer Details</h2>
    <hr/> % base = rows[0]
    <div class="table-responsive">
        <table class="table">
            <tr>
                <td>First Name:</td>
                <td>{{base['first_name']}}</td>
            </tr>
            <tr>
                <td>Last Name:</td>
                <td>{{base['last_name']}}</td>
            </tr>
            <tr>
                <td>Email:</td>
                <td>{{base['email']}}</td>
            </tr>
            <tr>
                <td>Address:</td>
                <td>{{base['address']}}</td>
            </tr>
            <tr>
                <td>Work Phone Country Code:</td>
                <td>{{base['work_phone_cc']}}</td>
            </tr>
            <tr>
                <td>Work Phone:</td>
                <td>{{base['work_phone_number']}}</td>
            </tr>
            <tr>
                <td>Home Phone Country Code:</td>
                <td>{{base['home_phone_cc']}}</td>
            </tr>
            <tr>
                <td>Home Phone Country Code:</td>
                <td>{{base['home_phone_number']}}</td>
            </tr>
        </table>
    </div>
    <!-- TODO iterate over this list -->
    <h3>Reservations</h3>
    <div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <th>Reservation Number</th>
                    <th>Tools</th>
                    <th>Start Date</th>
                    <th>End Date</th>
                    <th>Rental Price</th>
                    <th>Deposit</th>
                    <th>Pick Up Clerk</th>
                    <th>Drop Off Clerk</th>
                </tr>
            </thead>
            %for row in rows:

            <tr>
                <td>{{row['reservation_id']}}</td>
                <td>{{row['short_description']}}</td>
                <td>{{row['start_date']}}</td>
                <td>{{row['end_date']}}</td>
                <!-- What is the price? Day Price or a calculation? -->
                <td>${{row['day_price']}}</td>
                <td>${{row['deposit']}}</td>
                <td>{{row['p_name']}}</td>
                <td>{{row['d_name']}}</td>
            </tr>
            %end
        </table>
    </div>
</div>