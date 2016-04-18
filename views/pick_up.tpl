%#template for picking up a reservation

% rebase('layout.tpl', title="Pick Up Reservation")
<div class="container">
    <div class="row">
        <h2>Reservation Details</h2>
        <div class="table">
            <table class="table">
                <tr>
                    <td>Reservation Number:</td>
                    <td>{{reservation['reservation_id']}}</td>
                </tr>
                <tr>
                    <td>Customer ID:</td>
                    <td>{{reservation['customer_id']}}</td>
                </tr>
                <tr>
                    <td>Start Date:</td>
                    <td>{{reservation['start_date']}}</td>
                </tr>
                <tr>
                    <td>End Date:</td>
                    <td>{{reservation['end_date']}}</td>
                </tr>
            </table>
        </div>
    </div>
    <div class="row">
        <h2>Tool Details</h2>
        <div class="table-responsive">
            <table class="table">
                <thead>
                    <tr>
                        <th>Tool ID</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                %for tool in reservation['tools']:
                    <tr>
                        <td>{{tool['tool_id']}}</td>
                        <td><a href="/view_tool/{{tool['tool_id']}}">{{tool['short_description']}}</a></td>
                    </tr>
                %end
                </tbody>
            </table>
        </div>
    </div>
    <div class="row">
        <div class="table">
            <table class="table">
                <tr>
                    <td>Estimated Cost:</td>
                    <td>${{'{:.2f}'.format(reservation['total_rental'])}}</td>
                </tr>
                <tr>
                    <td>Deposit Required:</td>
                    <td>${{'{:.2f}'.format(reservation['total_deposit'])}}</td>
                </tr>
            </table>
        </div>
    </div>
    <hr>
    <form class="form-horizontal" role="form" action="/view_tool" method="post">
        <div class="form-group">
            <label for="tool_id" class="control-label col-sm-4">Tool #</label>
            <div class="col-sm-8">
                <input class="form-control" maxlength="255" name="tool_id" required>
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-4 col-sm-8">
                <input class="form-control btn btn-primary" type="submit" name="View Tool Details" value="View Details" />
            </div>
        </div>
    </form>
    <hr>
    <form class="form-horizontal" role="form" action="/reservation_receipt/{{reservation['reservation_id']}}" method="post">
        <div class="form-group">
            <label for="credit_card" class="control-label col-sm-4">Credit Card #<em>*</em></label>
            <div class="col-sm-8">
                <input class="form-control" maxlength="255" name="credit_card" required>
            </div>
        </div>
        <div class="form-group">
            <label for="expiration_date" class="control-label col-sm-4">Expiration Date<em>*</em></label>
            <div class="col-sm-8">
                <input class="form-control date-control" maxlength="10" name="expiration_date" required>
            </div>
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