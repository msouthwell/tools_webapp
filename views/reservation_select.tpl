%#template for entering a reservation number

% rebase('layout.tpl', title="Login")
<div class="container">
  <h1>Enter Reservation Number</h1>
  <h4>{{message}}</h4>
  <form class="form-horizontal" role="form" action="/pick_up" method="GET">
      <div class="form-group">
        <label for="id" class="control-label col-sm-4">Reservation ID</label>
        <div class="col-sm-8">
          <input class="form-control" maxlength="255" name="id" autofocus required>
        </div>
      </div>
      <div class="form-group">
          <div class="col-sm-offset-4 col-sm-8">
            <input class="form-control btn btn-primary" type="submit" name="Submit" value="Submit">
          </div>
      </div>
  </form>
</div>
