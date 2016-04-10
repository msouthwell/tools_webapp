%#template for viewing a clerk profile

% rebase('layout.tpl', title="Clerk Profile")
<div class="container">
    <h2>Clerk Details</h2>
    <h4>{{message}}</h4>
    <hr/>
    <div class="table-responsive">
        <table class="table">
            <tr>
                <td>First Name:</td>
                <td>{{first_name}}</td>
            </tr>
            <tr>
                <td>Last Name:</td>
                <td>{{last_name}}</td>
            </tr>
        </table>
    </div>
</div>
