%#template for customer Report


% rebase('layout.tpl', title="Customer Report")
<div class="container">
    <div class="row">
    <h3>Customer Report</h3>
    <div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <th>Last Name</th>
                    <th>First Name</th>
                    <th>Email</th>
                    <th>Total Rentals</th>
                </tr>
            </thead>
            %for row in rows:
            <tr>
                <td>{{row['last_name']}}</td>
                <td>{{row['first_name']}}</td>
                <td>{{row['email']}}</td>
                <td>{{row['rentals']}}</td>
            </tr>
            %end
        </table>
    </div>
</div>