%#template for displaying available tools

% rebase('layout.tpl', title="Available Tools")
<div class="container">
  <h1>Available Tools</h1>
  <hr>
  <div class="container">
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
      %for tool in tools:
        <tr>
          <td>{{tool['tool_id']}}</td>
          <td><a href="/view_tool/{{tool['tool_id']}}">{{tool['short_description']}}</a></td>
          <td>${{'{:.2f}'.format(float(tool['day_price']))}}</td>
          <td>${{'{:.2f}'.format(float(tool['deposit']))}}</td>
          <td><a href="/view_tool/{{tool['tool_id']}}">Details</a></td>
        </tr>
      %end
      </tbody>
    </table>
  </div>
  <hr>
  <form class="form-horizontal" role="form" action="/view_tool" method="post">
    <div class="form-group">
      <label for="tool_id" class="control-label col-sm-4">Part #<em>*</em></label>
      <div class="col-sm-8">
        <input class="form-control" maxlength="255" name="tool_id" required>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-4 col-sm-8">
        <input class="form-control btn btn-primary" type="submit" name="View Details" value="View Details"/>
      </div>
    </div>
  </form>
</div>
