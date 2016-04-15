%#template for selling a tool

% rebase('layout.tpl', title="Sell Tool")
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

      <tr>
        <td>Original Price:</td>
        <td>{{original_price}}</td>
      </tr>
      
      <tr>
        <td>Sell Price:</td>
        <td>{{sell_price}}</td>
      </tr>

    </table>
    <div>
        <input class="form-control" type="submit" name="Submit" value="Submit">
    </div>
  </div>
</div>
