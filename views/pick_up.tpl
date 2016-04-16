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
    <hr>
    <form class="form-vertical" role="form" action="/view_tool" method="post">
        <div class="form-group">
            <label for="tool_id" class="control-label">Tool #</label>
            <input class="form-control" maxlength="255" name="tool_id" required>
        </div>
        <input class="form-control btn btn-primary" type="submit" name="View Tool Details" value="View Details" />
    </form>
    <hr>
    <form class="form-vertical" role="form" action="/reservation_receipt/{{reservation_id}}" method="post">
        <div class="form-group">
            <label for="credit_card" class="control-label">Credit Card #<em>*</em></label>
            <input class="form-control" maxlength="255" name="credit_card" required>
        </div>
        <div class="form-group">
            <label for="expiration_date" class="control-label">Expiration Date<em>*</em></label>
            <input class="form-control date-control" maxlength="10" name="expiration_date" required>
        </div>
        <input class="form-control btn btn-primary" type="submit" name="complete" value="complete" />
    </form>
    <script>
        $(document).ready(function() {
            $("input.date-control").datepicker({
                startDate: "+0d",
                todayBtn: "linked",
                orientation: "bottom auto",
                autoclose: true,
                todayHighlight: true
            });
            $("input[type=radio]:first").attr('checked', true);
        });
    </script>
</div>
</div>