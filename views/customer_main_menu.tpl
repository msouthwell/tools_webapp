%#template for creating a login screen

% rebase('layout.tpl', title="Main Menu")
<div class="container">
  <h1>Main Menu</h1>

  <div class="col-sm-offset-4 col-sm-8">
    <form class="form-horizontal" role="form" action="/view_profile" method="get">
      <input class="form-control btn btn-primary" type="submit" name="View Profile" value="View Profile"/>
    </form>
  </div>

  <div class="col-sm-offset-4 col-sm-8">
    <form class="form-horizontal" role="form" action="/check_available_tools" method="get">
      <input class="form-control btn btn-primary" type="submit" name="Check Tool Availability" value="Check Tool Availability"/>
    </form>
  </div>

  <div class="col-sm-offset-4 col-sm-8">
    <form class="form-horizontal" role="form" action="/make_reservation" method="get">
      <input class="form-control btn btn-primary" type="submit" name="Make Reservation" value="Make Reservation"/>
    </form>
  </div>

  <div class="col-sm-offset-4 col-sm-8">
    <form class="form-horizontal" role="form" action="/login" method="get">
      <input class="form-control btn btn-primary" type="submit" name="Exit" value="Exit"/>
    </form>
  </div>
</div>
