%#template for creating a new tool

% rebase('layout.tpl', title="New Tool")
<div class="container">
    <h2>Tool Details</h2>
    <h4>{{message}}</h4>
    <hr/>
    <form class="form-horizontal" role="form" action="/create_tool" method="post">
        <div class="form-group">
            <label for="short_description" class="control-label col-sm-4">Short Description<em>*</em></label>
            <div class="col-sm-8">
                <input type="login" class="form-control" maxlength="255" name="short_description" autofocus required>
            </div>
        </div>
        <div class="form-group">
            <label for="full_description" class="control-label col-sm-4">Full Description<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="1000" name="full_description" required>
            </div>
        </div>
        <div class="form-group">
            <label for="deposit" class="control-label col-sm-4">Deposit<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="8" name="deposit" required>
            </div>
        </div>
        <div class="form-group">
            <label for="day_price" class="control-label col-sm-4">Day Price<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="8" name="day_price" required>
            </div>
        </div>
        <div class="form-group">
            <label for="original_price" class="control-label col-sm-4">Original Price<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="8" name="original_price" required>
            </div>
        </div>
        <div class="form-group">
            <label for="category_id" class="control-label col-sm-4">Category<em>*</em></label>
            <div class="col-sm-8">
                <select type="password" class="form-control" maxlength="32" name="category_id" required>
                %for category in categories:
                    <option value="{{category['category_id']}}">{{category['category']}}</option>
                %end
                </select>
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
            <input class="form-control" type="submit" name="Submit" value="submit">
            </div>
        </div>
    </form>
</div>
