%#template for creating a new customer profile

<p>Add a new customer</p>
<form action="/create_profile" method="GET">
<p>Email</p>
<input type="text" size="100" maxlength="100" name="email">
<p>first_name</p>
<input type="text" size="100" maxlength="100" name="first_name">
<p>last_name</p>
<input type="text" size="100" maxlength="100" name="last_name">
<p>password</p>
<input type="text" size="100" maxlength="100" name="password">
<p>address</p>
<input type="text" size="100" maxlength="100" name="address">
<p>work_phone_cc</p>
<input type="text" size="100" maxlength="100" name="work_phone_cc">
<p>work_phone_number</p>
<input type="text" size="100" maxlength="100" name="work_phone_number">
<p>home_phone_cc</p>
<input type="text" size="100" maxlength="100" name="home_phone_cc">
<p>home_phone_number</p>
<input type="text" size="100" maxlength="100" name="home_phone_number">

<input type="submit" name="Submit" value="submit">
</form>