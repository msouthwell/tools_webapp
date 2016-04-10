%#template for creating a new clerk

% rebase('layout.tpl', title="New Clerk")
<div class="container">
    <h2>Clerk Details</h2>
    <h4>{{message}}</h4>
    <hr/>
    <form class="form-horizontal" role="form" action="/create_clerk" method="post">
        <div class="form-group">
            <label for="login" class="control-label col-sm-4">Login<em>*</em></label>
            <div class="col-sm-8">
                <input type="login" class="form-control" maxlength="16" name="login" autofocus required>
            </div>
        </div>
        <div class="form-group">
            <label for="first_name" class="control-label col-sm-4">First Name<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="45" name="first_name" required>
            </div>
        </div>
        <div class="form-group">
            <label for="last_name" class="control-label col-sm-4">Last Name<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="45" name="last_name" required>
            </div>
        </div>
        <div class="form-group">
            <label for="password" class="control-label col-sm-4">Password<em>*</em></label>
            <div class="col-sm-8">
                <input type="password" class="form-control" maxlength="32" name="password" required>
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
            <input class="form-control" type="submit" name="Submit" value="submit">
            </div>
        </div>
    </form>
</div>
