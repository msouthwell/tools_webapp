%#template for creating a login screen

% rebase('layout.tpl', title="Main Menu")
<div class="container">
  <h1>Clerk's Menu</h1>
  <form class="form-horizontal" role="form" action="/about" method="get">
      <div class="form-group">
          <div class="col-sm-offset-2 col-sm-10">
          <input class="form-control" type="submit" name="Submit" value="submit">
          </div>
      </div>
  </form>
</div>
