%#template for creating a login screen

% rebase('layout.tpl', title="Main Menu")
<div class="container">
    <div class="row">
        <h1 class="text-center">Clerk's Menu</h1>
    </div>
    <form class="form-horizontal" role="form" action="/about" method="get">
        <div class="form-group">
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/pick_up" method="get">
                        <input class="form-control" type="submit" value="Pick Up" name="pickUp">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/drop_off" method="get">
                        <input class="form-control" type="submit" value="Drop Off" name="dropOff">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/generate_reports" method="get">
                        <input class="form-control" type="submit" value="Generate Reports" name="generateReports">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/hold_for_repair" method="get">
                        <input class="form-control" type="submit" value="Hold For Repair" name="holdForRepair">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/sell_tool" method="get">
                        <input class="form-control" type="submit" value="Sell Tool" name="sellTool">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/create_tool" method="get">
                        <input class="form-control" type="submit" value="Add Tool" name="addTool">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/generate_rental_contract" method="get">
                        <input class="form-control" type="submit" value="Generate Rental Contract" name="generateRentalContract">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/login" method="get">
                        <input class="form-control" type="submit" value="Logout" name="logout">
                    </form>
                </div>
            </div>
        </div>

</div>
</form>
</div>