%#template for creating a login screen

% rebase('layout.tpl', title="Check Available Tools")
<div class="container">
  <h1>Check Available Tools</h1>
  <form class="form-vertical" role="form" action="/check_available_tools" method="post">
    <hr>
    <div class="radio">
      <label><input type="radio" name="category" value="1" checked autofocus /> Hand Tools</label>
    </div>
    <div class="radio">
      <label><input type="radio" name="category" value="2"/> Construction Equipment</label>
    </div>
    <div class="radio">
      <label><input type="radio" name="category" value="3"/> Power Tools</label>
    </div>
    <hr>
    <div class="form-group">
      <label for="start_date" class="control-label">Start Date<em>*</em></label>
      <input class="form-control date-control" maxlength="10" name="start_date" required/>
    </div>
    <div class="form-group">
      <label for="end_date" class="control-label">End Date<em>*</em></label>
      <input class="form-control date-control" maxlength="10" name="end_date" required/>
    </div>
    <hr>
    <input class="form-control btn btn-primary" type="submit" name="Search" value="Search"/>
  </form>
  <script>
    $(document).ready(function(){
      $("input.date-control").datepicker({
        startDate: '+0d'
      });
    });
  </script>
</div>
