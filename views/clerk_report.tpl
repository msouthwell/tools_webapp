    %#template for clerk Report


% rebase('layout.tpl', title="Clerk Report")
<div class="container">
    <div class="row">
    <h3>Clerk Report</h3>
    <div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <th>Clerk Name</th>
                    <th>Pick-Ups</th>
                    <th>Drop-Offs</th>
                    <th>Total</th>
                </tr>
            </thead>
            %for row in rows:

            <tr>
                <td>{{row['clerk_name']}}</td>
                <td>{{row['pickup_count']}}</td>
                <td>{{row['dropoff_count']}}</td>
                <td>{{row['total_count']}}</td>
            </tr>
            %end
        </table>
    </div>
</div>