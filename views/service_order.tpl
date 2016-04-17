%#template for creating a new customer profile

% rebase('layout.tpl', title="Service Order")
<div class="container">
  <h2>Service Order Request</h2>
  <h4>{{message}}</h4>
  <hr/>
  <form class="form-horizontal" role="form" action="/service_order" method="post">
    <div class="form-group">
      <label for="email" class="control-label col-sm-4">Took ID<em>*</em></label>
      <div class="col-sm-8">
        <input type="text" class="form-control" maxlength="255" name="tool_id" value="{{tool_id}}" autofocus required/>
      </div>
    </div>
    <div class="form-group">
      <label for="start_date" class="control-label col-sm-4">Start Date<em>*</em></label>
      <div class="col-sm-8">
        <input class="form-control date-control" maxlength="10" name="start_date" value="{{start_date}}" required/>
      </div>
    </div>
    <div class="form-group">
      <label for="end_date" class="control-label col-sm-4">End Date<em>*</em></label>
      <div class="col-sm-8">
        <input class="form-control date-control" maxlength="10" name="end_date" value="{{end_date}}" required/>
      </div>
    </div>
    <div class="form-group">
      <label for="cost" class="control-label col-sm-4">Estimated Cost Of Repair<em>*</em></label>
      <div class="col-sm-8">
        <input type="text" class="form-control" maxlength="255" name="cost" value="{{cost}}" required/>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-4 col-sm-8">
        <input class="form-control btn btn-primary" type="submit" name="Submit" value="submit">
      </div>
    </div>
  </form>
  <script>
    $(document).ready(function(){
      $("input.date-control").datepicker({
        startDate: "+0d",
        todayBtn: "linked",
        orientation: "bottom auto",
        autoclose: true,
        todayHighlight: true
      });
    });
  </script>
</div>
