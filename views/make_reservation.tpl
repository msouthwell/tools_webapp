%#template for creating a login screen

% rebase('layout.tpl', title="Make Reservation")
<div class="container">
  <h1>Make Reservation</h1>
  <form class="form-vertical reservation_form" role="form" action="/make_reservation" method="post">
    <hr>
    <div class="form-group">
      <label for="start_date" class="control-label">Start Date<em>*</em></label>
      <input class="form-control date-control" maxlength="10" name="start_date" value="{{start_date}}" required/>
    </div>
    <div class="form-group">
      <label for="end_date" class="control-label">End Date<em>*</em></label>
      <input class="form-control date-control" maxlength="10" name="end_date" value="{{end_date}}" required/>
    </div>
    <hr>
    <div class="container reservation_tools">
      <input type="hidden" name="reserved_tools" value="{{reserved_tools}}"/>
      <table class="table">
        <thead>
          <tr>
            <th>Tool ID</th>
            <th>Description</th>
            <th>Deposit</th>
            <th>Price/Day</th>
            <th>Links</th>
          </tr>
        </thead>
        <tbody>
        </tbody>
      </table>
      <hr>
      <div class="form-group">
        <label for="category" class="control-label">Type of Tool:<em>*</em></label>
        <select class="form-control" name="category" required>
        %for category in categories:
          <option value="{{category['category_id']}}">{{category['category']}}</option>
        %end
        </select>
      </div>
      <div class="form-group">
        <label for="tool" class="control-label">Tool:<em>*</em></label>
        <select class="form-control" name="tool" required>
        %for tool in tools:
          <option value="{{tool['tool_id']}}">{{tool['tool_id']}} {{tool['short_description']}} ${{tool['day_price']}}</option>
        %end
        </select>
      </div>
      <input class="form-control btn btn-primary" type="submit" name="Add Tool" value="Add Tool"/>
      <hr>
      <input class="form-control btn btn-primary" type="submit" name="Calculate Total" value="Calculate Total"/>
    </div>
  </form>
  <script>
    $(document).ready(function(){
      if (reservationDatesSpecified()) {
        $("div.reservation_tools").show();
      } else {
        $("div.reservation_tools").hide();
      }
      $("input.date-control").datepicker({
        startDate: '+0d',
        todayBtn: true,
        autoclose: true,
        todayHighlight: true
      }).on('changeDate', function(e) {
        if (reservationDatesSpecified()) {
      	  $("div.reservation_add").show();
      	  $("form.reservation_form").submit();
        }
      });
      $("select[name=category]").on('change', function(e) {
        $("form.reservation_form").submit();
      });
      
      function reservationDatesSpecified() {
      	var start_date = $("input.date-control[name=start_date]").val();
      	var end_date = $("input.date-control[name=end_date]").val();
      	return start_date.length > 0 && end_date.length > 0;
      }
    });
  </script>
</div>
