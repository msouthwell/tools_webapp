%#template for Drop Off


% rebase('layout.tpl', title="Drop Off")
<div class="container">
    <div class="row">
    <h2>Handyman Tools Rental Receipt</h2>
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
                    <td>{{clerk_dropoff_name}}</td>
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
    <hr>
    <div class="row">
        <div class="table">
            <table class="table">
                <tr>
                    <td>Rental Cost:</td>
                    <td>${{'{:.2f}'.format(rental_cost)}}</td>
                </tr>
                <tr>
                    <td>Deposit Held:</td>
                    <td>- ${{'{:.2f}'.format(deposit_held)}}</td>
                </tr>
                <tr>
                    <td>Total:</td>
                    <td>${{'{:.2f}'.format(remaining_cost)}}</td>
                </tr>
            </table>
        </div>
    </div>
</div>
</div>