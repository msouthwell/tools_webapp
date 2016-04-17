%#template for getting tool_id to sell

% rebase('layout.tpl', title="Sell Tool")
<div class="container">
  <h2>Sell Tool</h2>
  <form class="form-horizontal" role="form" action="/sell_tool" method="post">
    <div class="form-group">
      <label for="tool_id" class="control-label col-sm-4">Tool ID<em>*</em></label>
      <div class="col-sm-8">
        <input type="text" class="form-control" maxlength="255" name="tool_id" value="{{tool_id}}" autofocus required/>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-offset-4 col-sm-8">
        <input class="form-control btn btn-primary" type="submit" name="Submit" value="submit">
      </div>
    </div>
  </form>
</div>
