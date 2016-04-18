%#template for creating a login screen
%from controllers import make_reservation
%import json

% rebase('layout.tpl', title="Make Reservation")
<div class="container">
  <h1>Make Reservation</h1>
  <h4>{{message}}</h4>
  <hr>
  <form class="form-horizontal reservation_form" role="form" action="/make_reservation" method="post">
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
    <hr>
    <div class="reservation_tools">
      <input type="hidden" name="reserved_tools" value="{{reserved_tools}}"/>
      <table class="table">
        <thead>
          <tr>
            <th>Tool ID</th>
            <th>Description</th>
            <th>Price/Day</th>
            <th>Deposit</th>
            <th>Links</th>
          </tr>
        </thead>
        <tbody>
        %for index, reserved_tool in enumerate(eval(reserved_tools)):
          <tr>
            <td>{{reserved_tool['tool_id']}}</td>
            <td><a href="/view_tool/{{reserved_tool['tool_id']}}">{{reserved_tool['short_description']}}</a></td>
            <td>${{'{:.2f}'.format(float(reserved_tool['day_price']))}}</td>
            <td>${{'{:.2f}'.format(float(reserved_tool['deposit']))}}</td>
            <td><a href="{{index}}" class="remove_tool">Remove</a></td>
          </tr>
        %end
        </tbody>
      </table>
      <hr>
      <div class="form-group">
        <label for="category" class="control-label col-sm-4">Type of Tool</label>
        <div class="col-sm-8">
          <select class="form-control" name="category">
          %for category in categories:
            <option value="{{category['category_id']}}" {{!'selected="selected"' if str(category['category_id']) == selected_category else ""}}>{{category['category']}}</option>
          %end
          </select>
        </div>
      </div>
      <div class="form-group">
        <label for="requested_tool" class="control-label col-sm-4">Tool</label>
        <div class="col-sm-8">
          <select class="form-control" name="requested_tool">
          %for tool in tools:
            <option value="{{json.dumps(tool, default=make_reservation.decimal_default)}}">{{tool['tool_id']}} {{tool['short_description']}} ${{'{:.2f}'.format(float(tool['day_price']))}}</option>
          %end
          </select>
        </div>
      </div>
      <div class="form-group">
        <div class="col-sm-offset-4 col-sm-8">
          <input class="form-control btn btn-primary" type="submit" name="Add Tool" value="Add Tool"/>
        </div>
      </div>
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
        startDate: "+0d",
        todayBtn: "linked",
        orientation: "bottom auto",
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
      $("a.remove_tool").click(function(e){
        e.preventDefault();
        var link = this;
        var removeIndex = $(link).attr('href');

        // remove the requested tool from the reserved tool list
        var reserved_tools_field = $("input[name=reserved_tools]");
        var reserved_tools = $.parseJSON(reserved_tools_field.val());
        reserved_tools.splice(removeIndex, 1);
        reserved_tools_field.val(JSON.stringify(reserved_tools));

        // submit the form to redraw the table
        $("form.reservation_form").submit();
      });

      $("form.reservation_form").submit(function(e){
        e.preventDefault();
        var form = this;
        var button = $(this).find("input[type=submit]:focus").attr("value");
        if (button == 'Add Tool') {
          // get requested tool; is JSON in the value
          var requested_tool = $.parseJSON($("select[name=requested_tool]").val());

          // add the requested tool to the reserved tool list
          var reserved_tools_field = $("input[name=reserved_tools]");
          var reserved_tools = $.parseJSON(reserved_tools_field.val());
          reserved_tools.push(requested_tool);
          reserved_tools_field.val(JSON.stringify(reserved_tools));

          // submit the form to redraw the table
          form.submit();
        } else {
          form.submit();
        }
      });

      function reservationDatesSpecified() {
        var start_date = $("input.date-control[name=start_date]").val();
        var end_date = $("input.date-control[name=end_date]").val();
        return start_date.length > 0 && end_date.length > 0;
      }
    });
  </script>
</div>
