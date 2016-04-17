%#template for viewing a tool

% rebase('layout.tpl', title="View Tool")
<div class="container">
  <h2>Tool Details</h2>
  
  %for tool in tools:
  <div class="table">
    <table class="table">
      <tr>
        <td>Tool ID:</td>
        <td>{{tool['tool_id']}}</td>
      </tr>
      <tr>
        <td>Description:</td>
        <td>{{tool['short_description']}}</td>
      </tr>
      <tr>
        <td>Full Description:</td>
        <td>{{tool['full_description']}}</td>
      </tr>
      <tr>
        <td>Deposit:</td>
        <td>${{'{:.2f}'.format(tool['deposit'])}}</td>
      </tr>
      <tr>
        <td>Price/Day:</td>
        <td>${{'{:.2f}'.format(tool['day_price'])}}</td>
      </tr>
      <tr>
        <td>Category:</td>
        <td>{{tool['category_id']}}</td>
      </tr>
      
      %for accessory in tool['accessories']:
        <tr>
          <td>{{accessory['description']}}</td>
        </tr>
      %end

    </table>
  </div>
  %end
</div>
