%#template for creating a report selection screen

% rebase('layout.tpl', title="Generate Reports")
<div class="container">
  <h1>Generate Reports</h1>
  <h4>{{message}}</h4>
  <form class="form-horizontal" role="form" action="/generate_reports" method="post">

      <div class="form-group">
        <label class="radio-inline"><input type="radio" name="report_type" value="inventory" checked>Inventory Report</label>
        <label class="radio-inline"><input type="radio" name="report_type" value="customer">Customer Report</label>
        <label class="radio-inline"><input type="radio" name="report_type" value="clerk">Clerk Report</label>
      </div>
      <div class="form-group">
          <div class="col-sm-offset-4 col-sm-8">
            <input class="form-control btn btn-primary" type="submit" name="generate" value="Generate Report">
          </div>
      </div>
  </form>
</div>