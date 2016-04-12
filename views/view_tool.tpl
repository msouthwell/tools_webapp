%#template for viewing a clerk profile

% rebase('layout.tpl', title="Clerk Profile")
<div class="container">
  <h2>Tool Details</h2>
  <div class="table">
    <table class="table">
      <tr>
        <td>Tool ID:</td>
        <td>{{tool_id}}</td>
      </tr>
      <tr>
        <td>Description:</td>
        <td>{{short_description}}</td>
      </tr>
      <tr>
        <td>Full Description:</td>
        <td>{{full_description}}</td>
      </tr>
      <tr>
        <td>Deposit:</td>
        <td>{{deposit}}</td>
      </tr>
      <tr>
        <td>Price/Day:</td>
        <td>{{day_price}}</td>
      </tr>
      <tr>
        <td>Category:</td>
        <td>{{category}}</td>
      </tr>
    </table>
  </div>
</div>
