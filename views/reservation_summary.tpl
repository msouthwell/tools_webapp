%#template for creating a login screen
%from controllers import make_reservation
%import json

% rebase('layout.tpl', title="Reservation Summary")
<div class="container">
  <h1>Reservation Summary</h1>
  <form class="form-vertical reservation_form" role="form" action="/make_reservation" method="post">
    <h4>Tools Desired</h4>
    <input type="hidden" name="reserved_tools" value="{{reserved_tools}}"/>
    <div class="table-responsive">
      <table class="table">
        <thead>
          <tr>
            <th>Tool ID</th>
            <th>Description</th>
            <th>Deposit</th>
            <th>Price/Day</th>
          </tr>
        </thead>
        <tbody>
        %for reserved_tool in eval(reserved_tools):
          <tr>
            <td>{{reserved_tool['tool_id']}}</td>
            <td>{{reserved_tool['short_description']}}</td>
            <td>${{'{:.2f}'.format(float(reserved_tool['deposit']))}}</td>
            <td>${{'{:.2f}'.format(float(reserved_tool['day_price']))}}</td>
          </tr>
        %end
        </tbody>
      </table>
    </div>
    <h4>Rental Information</h4>
    <div class="table-responsive">
      <input type="hidden" name="start_date" value="{{start_date}}"/>
      <input type="hidden" name="end_date" value="{{end_date}}"/>
      <table class="table">
        <tr>
          <td>Start Date</td>
          <td>{{start_date}}</td>
        </tr>
        <tr>
          <td>End Date</td>
          <td>{{end_date}}</td>
        </tr>
        <tr>
          <td>Total Rental Price</td>
          <td>${{'{:.2f}'.format(rental_price)}}</td>
        </tr>
        <tr>
          <td>Total Deposit Required</td>
          <td>${{'{:.2f}'.format(deposit)}}</td>
        </tr>
      </table>
    </div>
    <hr>
    <input class="form-control btn btn-primary" type="submit" name="Reserve Tools" value="Reserve Tools"/>
  </form>
</div>
