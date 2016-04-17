%#template for creating a new customer profile

% rebase('layout.tpl', title="New Customer")
<div class="container">
    <h2>Customer Details</h2>
    <h4>{{message}}</h4>
    <hr/>

    </script>
    <form class="form-horizontal" role="form" action="/create_profile" method="post">
        <div class="form-group">
            <label for="email" class="control-label col-sm-4">Email<em>*</em></label>
            <div class="col-sm-8">
                <input type="email" class="form-control" maxlength="255" name="email" autofocus required>
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
            <label for="password1" class="control-label col-sm-4">Password<em>*</em></label>
            <div class="col-sm-8">
                <input type="password" class="form-control" maxlength="32" name="password" id="password" required>
            </div>
        </div>
        <div class="form-group">
            <label for="password2" class="control-label col-sm-4">Confirm Password<em>*</em></label>
            <div class="col-sm-8">
                <input type="password" class="form-control" maxlength="32" name="password2" id="password2" required>
            </div>
        </div>
        <div class="form-group">
            <label for="address" class="control-label col-sm-4">Address<em>*</em></label>
            <div class="col-sm-8">
                <TEXTAREA type="text" class="form-control" maxlength="500" name="address" required></TEXTAREA>
            </div>
        </div>
        <div class="form-group">
            <label for="work_phone_cc" class="control-label col-sm-4">Work Phone Country Code<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" size="5" maxlength="4" name="work_phone_cc" required>
            </div>
        </div>
        <div class="form-group">
            <label for="work_phone_number"class="control-label col-sm-4">Work Phone Number<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="20" name="work_phone_number" required>
            </div>
        </div>
        <div class="form-group">
            <label for="home_phone_cc" class="control-label col-sm-4">Home Phone Country Code<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="4" name="home_phone_cc" required>
            </div>
        </div>
        <div class="form-group">
            <label for="home_phone_number" class="control-label col-sm-4">Home Phone Number<em>*</em> </label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="20" name="home_phone_number" required>
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
            <input class="form-control" type="submit" name="Submit" value="submit">
            </div>
        </div>
    </form>
</div>
<script type="text/javascript">
    window.onload = function() {
        document.getElementById("password1").onchange = validatePassword;
        document.getElementById("password2").onchange = validatePassword;
    }

    function validatePassword() {
        var pass2 = document.getElementById("password2").value;
        var pass1 = document.getElementById("password1").value;
        if (pass1 != pass2)
            document.getElementById("password2").setCustomValidity("Passwords Don't Match");
        else
            document.getElementById("password2").setCustomValidity('');
        //empty string means no validation error
    }
</script>
