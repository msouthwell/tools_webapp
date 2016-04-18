%#template for pick up receipt


% rebase('layout.tpl', title="Pick Up Receipt")
<div class="container">
    <div class="row">
    <h2>Handyman Tools Rental Contract</h2>
        <h4>Reservation Details</h4>
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
                    <td>Customer Name:</td>
                    <td>{{customer_name}}</td>
                </tr>
                <tr>
                    <td>Clerk On Duty:</td>
                    <td>{{clerk_pickup_name}}</td>
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
        <h4>Tools Rented</h4>
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
                    <td>Rental Cost:</td>
                    <td>${{'{:.2f}'.format(float(estimated_cost))}}</td>
                </tr>
                <tr>
                    <td>Deposit Held:</td>
                    <td>${{'{:.2f}'.format(float(deposit_required))}}</td>
                </tr>
            </table>
        </div>
    </div>
    <hr>
    <div class="row">
        <div class="table">
            <table class="table">
                <tr>
                    <td>Credit Card:</td>
                    <td>{{credit_card}}</td>
                </tr>
                <tr>
                    <td>Expiration Date:</td>
                    <td>{{expiration_date}}</td>
                </tr>
            </table>
        </div>
    </div>
    <p>______________________________________________________</p>
    <h6>Customer Signature</h6>

</div>
</div>