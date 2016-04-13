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
            <tr>
                <td>Reservation Number:</td>
                <td>{{reservation_id}}</td>
            </tr>
            <tr>
                <td>Tool:</td>
                <td>{{category}}</td>
            </tr>
            <tr>
                <td>Start Date:</td>
                <td>{{start_date}}</td>
            </tr>
            <tr>
                <td>End Date:</td>
                <td>{{end_date}}</td>
            </tr>
            <tr>
              <!-- What is the price? Day Price or a calculation? -->
                <td>Rental Price:</td>
                <td>{{day_price}}</td>
            </tr>
            <tr>
                <td>Pickup Clerk:</td>
                <td>{{pickup_clerk}}</td>
            </tr>
            <tr>
                <td>Dropoff Clerk:</td>
                <td>{{dropoff_clerk}}</td>
            </tr>
        </table>
    </div>
</div>
