%#template for displaying reservation

% rebase('layout.tpl', title="Reservation")
<div class="container">
  <h1>Reservation Details</h1>
  <h4>{{message}}</h4>
  %for reservation in reservations:
  <div class="table-responsive">
    <table class="table">
      <tr>
        <td>Reservation</td>
        <td>{{reservation['reservation_id']}}</td>
      </tr>
      <tr>
        <td>Customer</td>
        <td>{{reservation['customer_name']}}</td>
      </tr>
      <tr>
        <td>Start Date</td>
        <td>{{reservation['start_date']}}</td>
      </tr>
      <tr>
        <td>End Date</td>
        <td>{{reservation['end_date']}}</td>
      </tr>
      <tr>
        <td>Total Rental Price</td>
        <td>${{'{:.2f}'.format(float(reservation['total_rental']))}}</td>
      </tr>
      <tr>
        <td>Total Deposit</td>
        <td>${{'{:.2f}'.format(float(reservation['total_deposit']))}}</td>
      </tr>
    </table>
  </div>
  <div class="table-responsive">
    <table class="table">
      <thead>
        <tr>
          <th>Tool ID</th>
          <th>Description</th>
          <th>Deposit</th>
          <th>Price/Day</th>
          <th>Links</th>
        </tr>
      </thead>
      <tbody>
      %for tool in reservation['tools']:
        <tr>
          <td>{{tool['tool_id']}}</td>
          <td>{{tool['short_description']}}</td>
          <td>${{'{:.2f}'.format(float(tool['deposit']))}}</td>
          <td>${{'{:.2f}'.format(float(tool['day_price']))}}</td>
          <td><a href="/view_tool/{{tool['tool_id']}}">Details</a></td>
        </tr>
      %end
      </tbody>
    </table>
  </div>
  %end
</div>
