%#template for creating a login screen

% rebase('layout.tpl', title="Check Available Tools")
<div class="container">
  <h1>Check Available Tools</h1>
  <hr>
  <form class="form-horizontal" role="form" action="/check_available_tools" method="post">
    <div class="form-group">
      <label class="col-sm-4 control-label">Tool Type<em>*</em></label>
      <div class="col-sm-8">
      %for category in categories:
        <div class="radio">
          <label><input type="radio" name="category" value="{{category['category_id']}}"/> {{category['category']}}</label>
        </div>
      %end
      </div>
    </div>
    <hr>
    <div class="form-group">
      <label for="start_date" class="control-label col-sm-4">Start Date<em>*</em></label>
      <div class="col-sm-8">
        <input class="form-control date-control" maxlength="10" name="start_date" required/>
      </div>
    </div>
    <div class="form-group">
      <label for="end_date" class="control-label col-sm-4">End Date<em>*</em></label>
      <div class="col-sm-8">
        <input class="form-control date-control" maxlength="10" name="end_date" required/>
      </div>
    </div>
    <hr>
    <div class="form-group">
      <div class="col-sm-offset-4 col-sm-8">
        <input class="form-control btn btn-primary" type="submit" name="Search" value="Search"/>
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
      $("input[type=radio]:first").attr('checked', true);
    });
  </script>
</div>
