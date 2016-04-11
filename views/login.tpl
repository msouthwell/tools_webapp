%#template for creating a login screen

% rebase('layout.tpl', title="Login")
<div class="container">
  <h1>Login</h1>
  <h4>{{message}}</h4>
  <form class="form-horizontal" role="form" action="/login" method="post">
      <div class="form-group">
        <label for="email" class="control-label">Login<em>*</em></label>
        <input class="form-control" maxlength="255" name="login" autofocus required>
      </div>
      <div class="form-group">
          <label for="password" class="control-label">Password<em>*</em></label>
          <input type="password" class="form-control" maxlength="255" name="password" required>
      </div>
      <div class="form-group">
        <label class="radio-inline"><input type="radio" name="usertype" value="customers" checked>Customer</label>
        <label class="radio-inline"><input type="radio" name="usertype" value="clerks">Clerk</label>
      </div>
      <div class="form-group">
          <div class="col-sm-offset-4 col-sm-8">
            <input class="form-control btn btn-primary" type="submit" name="Submit" value="submit">
          </div>
      </div>
  </form>
</div>
