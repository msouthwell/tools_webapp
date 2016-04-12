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
          <th>Deposit</th>
          <th>Price/Day</th>
          <th>Links</th>
        </tr>
      </thead>
      <tbody>
      %for row in rows:
        <tr>
          <td>{{row['tool_id']}}</td>
          <td>{{row['short_description']}}</td>
          <td>{{row['deposit']}}</td>
          <td>{{row['day_price']}}</td>
          <td><a href="/view_tool/{{row['tool_id']}}">Detail</a></td>
        </tr>
      %end
      </tbody>
    </table>
  </div>
</div>
