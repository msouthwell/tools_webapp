%#template for picking up a reservation

% rebase('layout.tpl', title="Pick Up Reservation")
<div class="container">
    <div class="row">
        <h2>Reservation Details</h2>
        <div class="table">
            <table class="table">
                <tr>
                    <td>Reservation Number:</td>
                    <td>{{reservation_id}}</td>
                </tr>
                <tr>
                    <td>Customer ID:</td>
                    <td>{{customer_id}}</td>
                </tr>
                <tr>
                    <td>Start Date:</td>
                    <td>{{start_date}}</td>
                </tr>
                <tr>
                    <td>End Date:</td>
                    <td>{{end_date}}</td>
                </tr>
            </table>
        </div>
    </div>
    <div class="row">
        <h2>Tool Details</h2>
        <div class="table">
            <table class="table">
                {{!tool_table}}
            </table>
        </div>
    </div>
    <div class="row">
        <div class="table">
            <table class="table">
                <tr>
                    <td>Deposit Required:</td>
                    <td>{{deposit_required}}</td>
                </tr>
                <tr>
                    <td>Estimated Cost:</td>
                    <td>{{estimated_cost}}</td>
                </tr>
            </table>
        </div>
    </div>
</div>
</div>