%#template for viewing a customer profile
% rebase('layout.tpl', title="Customer Profile")
<div class="container">
    <h2>Customer Details</h2>
    <div class="table-responsive">
        <table class="table">
            <tr>
                <td>Name:</td>
                <td>{{customer['customer_name']}}</td>
            </tr>
            <tr>
                <td>Email:</td>
                <td>{{customer['email']}}</td>
            </tr>
            <tr>
                <td>Address:</td>
                <td>{{customer['address']}}</td>
            </tr>
            <tr>
                <td>Work Phone:</td>
                <td>{{customer['work_phone']}}</td>
            </tr>
            <tr>
                <td>Home Phone:</td>
                <td>{{customer['home_phone']}}</td>
            </tr>
        </table>
    </div>
    <h3>Reservations</h3>
    %if len(reservations) == 0:
    <h4>No reservations</h4>
    %else:
        <div class="table-responsive">
          <table class="table">
              <thead>
                  <tr>
                      <th>Reservation Number</th>
                      <th>Tools</th>
                      <th>Start Date</th>
                      <th>End Date</th>
                      <th>Total Rental Price</th>
                      <th>Total Deposit</th>
                      <th>Pick Up Clerk</th>
                      <th>Drop Off Clerk</th>
                  </tr>
              </thead>
              %for reservation in reservations:
              <tr>
                  <td><a href="/view_reservation/{{reservation['reservation_id']}}">{{reservation['reservation_id']}}</a></td>
                  <td>
                  %for tool in reservation['tools']:
                    <a href="/view_tool/{{tool['tool_id']}}">{{tool['short_description']}}</a><br/>
                  %end
                  </td>
                  <td>{{reservation['start_date']}}</td>
                  <td>{{reservation['end_date']}}</td>
                  <td>${{'{:.2f}'.format(float(reservation['total_rental']))}}</td>
                  <td>${{'{:.2f}'.format(float(reservation['total_deposit']))}}</td>
                  <td>{{!reservation['pickup_clerk'] if reservation['pickup_clerk'] is not None else ""}}</td>
                  <td>{{!reservation['dropoff_clerk'] if reservation['dropoff_clerk'] is not None else ""}}</td>
              </tr>
              %end
          </table>
        </div>
    %end
</div>
