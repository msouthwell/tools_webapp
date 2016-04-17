%#template for creating a login screen

% rebase('layout.tpl', title="Main Menu")
<div class="container">
    <div class="row">
        <h1 class="text-center">Clerk's Menu</h1>
    </div>

            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/pick_up" method="get">
                        <input class="form-control" type="submit" value="Pick Up Reservation" name="pickUp">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/drop_off" method="get">
                        <input class="form-control" type="submit" value="Drop Off Reservation" name="dropOff">
                    </form>
                </div>
            </div>

            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/service_order" method="get">
                        <input class="form-control" type="submit" value="Service Order" name="holdForRepair">
                    </form>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-offset-4 col-sm-4">
                    <form class="form-horizontal" role="form" action="/create_tool" method="get">
                        <input class="form-control" type="submit" value="Add New Tool" name="addTool">
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
                    <form class="form-horizontal" role="form" action="/generate_reports" method="get">
                        <input class="form-control" type="submit" value="Generate Reports" name="generateReports">
                    </form>
                </div>
            </div>
        </div>
</div>
