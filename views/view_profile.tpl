%#template for viewing a customer profile

% rebase('layout.tpl', title="Customer Profile")
<div class="container">
    <h2>Customer Details</h2>
    <h4>{{message}}</h4>
    <hr/>
    <div class="table-responsive">
        <table class="table">
            <tr>
                <td>First Name:</td>
                <td>{{first_name}}</td>
            </tr>
            <tr>
                <td>Last Name:</td>
                <td>{{last_name}}</td>
            </tr>
            <tr>
                <td>Email:</td>
                <td>{{email}}</td>
            </tr>
            <tr>
                <td>Address:</td>
                <td>{{address}}</td>
            </tr>
            <tr>
                <td>Work Phone Country Code:</td>
                <td>{{work_phone_cc}}</td>
            </tr>
            <tr>
                <td>Work Phone:</td>
                <td>{{work_phone_number}}</td>
            </tr>
            <tr>
                <td>Home Phone Country Code:</td>
                <td>{{home_phone_cc}}</td>
            </tr>
            <tr>
                <td>Home Phone Country Code:</td>
                <td>{{home_phone_number}}</td>
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
                <th>Pick Up Clerk</th>
                <th>Drop Off Clerk</th>
              </tr>
            </thead>
            <tr>
                <td>{{reservation_id}}</td>
            </tr>
            <tr>
                <td>{{short_description}}</td>
            </tr>
            <tr>
                <td>{{start_date}}</td>
            </tr>
            <tr>
                <td>{{end_date}}</td>
            </tr>
            <tr>
              <!-- What is the price? Day Price or a calculation? -->
                <td>Rental Price:</td>

            </tr>
            <tr>
                <td>{{p_name}}</td>
            </tr>
            <tr>
                <td>{{d_name}}</td>
            </tr>
        </table>
    </div>
</div>
