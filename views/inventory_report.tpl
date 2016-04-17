    %#template for inventory Report


% rebase('layout.tpl', title="Inventory Report")
<div class="container">
    <div class="row">
    <h3>Inventory Report</h3>
    <div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <th>Tool ID</th>
                    <th>Short Description</th>
                    <th>Rental Profit</th>
                    <th>Cost of Tool</th>
                    <th>Total Profit</th>
                </tr>
            </thead>
            %for row in rows:

            <tr>
                <td>{{row['tool_id']}}</td>
                <td>{{row['short_description']}}</td>
                <td>{{row['rental_profit']}}</td>
                <td>{{row['cost_of_tool']}}</td>
                <td>{{row['total_profit']}}</td>
            </tr>
            %end
        </table>
    </div>
</div>