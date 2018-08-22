users_arr.forEach(function(item, i, arr) {
  if(item != 0){
    defineRule("score_" + item, {
        whenChanged: item + "/orders_finished",
        then: function(newValue, devName, cellName) {
          order_done(item);
        }
    });
  }
});

function order_done(user_id) {
    if (dev[user_id + "/orders_finished"] > dev[user_id + "/orders_finished_was"]) {
      var donet_1 = (parseInt(dev[user_id + "/orders_finished"]) - parseInt(dev[user_id + "/orders_finished_was"]))*order_price
        dev[user_id + "/Score"] = parseInt(dev[user_id + "/Score"]) + donet_1;
      log(dev[user_id + "/Score"]);
    }
    dev[user_id + "/orders_finished_was"] = dev[user_id + "/orders_finished"];
}