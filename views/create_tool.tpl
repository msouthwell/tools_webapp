%#template for creating a new tool

% rebase('layout.tpl', title="New Tool")
<div class="container">
    <h2>Tool Details</h2>
    <h4>{{message}}</h4>
    <hr/>
    <form class="form-horizontal new_tool_form" role="form" action="/create_tool" method="post">
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
            <label for="day_price" class="control-label col-sm-4">Day Price<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="8" name="day_price" required>
            </div>
        </div>
        <div class="form-group">
            <label for="deposit" class="control-label col-sm-4">Deposit<em>*</em></label>
            <div class="col-sm-8">
                <input type="text" class="form-control" maxlength="8" name="deposit" required>
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
                <select class="form-control" name="category_id" required>
                %for category in categories:
                    <option value="{{category['category_id']}} {{!'true' if category['has_accessories'] == 1 else ""}}">{{category['category']}}</option>
                %end
                </select>
            </div>
        </div>
        <div class="form-group accessories">
            <label class="control-label col-sm-4">Accessories</label>
            <div class="col-sm-8">
                <div class="table-responsive">
                    <input type="hidden" name="accessories" value=""/>
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Accessory</th>
                                <th>Links</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                </div>
                <div class="form-group">
                    <label for="new_accessory" class="control-label col-sm-4">New Accessory</label>
                    <div class="col-sm-8">
                        <input type="text" class="form-control" maxlength="255" name="new_accessory">
                    </div>
                </div>
                <div class="form-group">
                    <div class="col-sm-offset-4 col-sm-8">
                        <input class="form-control btn btn-primary add-accessory" type="button" name="Add Accessory" value="Add Accessory">
                    </div>
                </div>
            </div>
        </div>
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-10">
                <input class="form-control btn btn-primary" type="submit" name="Submit" value="submit">
            </div>
        </div>
    </form>
    <script>
        $(document).ready(function(){
            var accessories_field = $("input[name=accessories]");

            $("select[name=category_id]").on('change', function(e) {
                var optionSelected = $("option:selected", this)[0];
                showAccessories(optionSelected);
            });
            $("input.add-accessory").click(function(e) {
                e.preventDefault();
                var new_accessory_field = $("input[name=new_accessory]");
                var new_accessory = new_accessory_field.val();
                if (new_accessory.length > 0) {
                    var accessories = [];
                    if (accessories_field.val().length > 0) {
                        accessories = $.parseJSON(accessories_field.val());
                    }
                    accessories.push(new_accessory);
                    setAccessories(JSON.stringify(accessories))
                    new_accessory_field.val("");
                }
            });
            $(document).on('click', "a.remove_accessory", function(e){
                e.preventDefault();
                var link = this;
                var removeIndex = $(link).attr('href');

                // remove the requested accessory from the accessories list
                var accessories = $.parseJSON(accessories_field.val());
                accessories.splice(removeIndex, 1);
                setAccessories(JSON.stringify(accessories))
            });

            // show accessories according to first option
            showAccessories($("select[name=category_id] option:selected")[0]);

            function showAccessories(optionSelected) {
                if (optionSelected.value.indexOf('true') > 0) {
                    buildAccessoryTable();
                    $("div.accessories").show();
                } else {
                    // clear accessories and hide form
                    $("div.accessories").hide();

                    setAccessories('[]');
                }
            }

            function setAccessories(accessories) {
                accessories_field.val(accessories);
                buildAccessoryTable();
            }

            function buildAccessoryTable() {
                var newHtml = $("<tbody></tbody>");
                var accessories = $.parseJSON(accessories_field.val());
                if (accessories.length > 0) {
                    $.each(accessories, function(index, accessory) {
                        row = newHtml.append($("<tr></tr>"));
                        row.append($("<td>" + accessory + "</td>"));
                        row.append($('<td><a href="' + index + '" class="remove_accessory">Remove</a></td>'));
                    });
                }

                $("table.table tbody").replaceWith(newHtml);
            }
        });
    </script>
</div>
