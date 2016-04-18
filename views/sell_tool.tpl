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
        <td>Price/Day:</td>
        <td>${{'{:.2f}'.format(day_price)}}</td>
      </tr>
      <tr>
        <td>Deposit:</td>
        <td>${{'{:.2f}'.format(deposit)}}</td>
      </tr>
      <tr>
        <td>Category:</td>
        <td>{{category}}</td>
      </tr>

      <tr>
        <td>Original Price:</td>
        <td>${{'{:.2f}'.format(original_price)}}</td>
      </tr>
      
      <tr>
        <td>Sell Price:</td>
        <td>${{'{:.2f}'.format(sell_price)}}</td>
      </tr>

      <tr>
        <form class="form-horizontal" role="form" action="/sell" value="{{tool_id}}" method="post">
        <td><input type="hidden" name="tool_id" value="{{tool_id}}"></td>
        <td><input class="form-control btn btn-primary" type="submit" name="Submit" value="submit"></td>
        </form>
      </tr>
    </table>
  </div>
</div>
