function ble_is_near() {
    mac_arr.forEach(function(item, i, arr) {
        if (item != "") {
            if (dev["BLE/" + item] > -65 && dev["BLE/" + item] < -10) {
                log(users_arr[i]);
                near = users_arr[i];
            }
        }
    });
    return near;
}

defineRule("cron_timer_2", {
    when: cron("@every 0h0m20s"),
    then: function() {
        runShellCommand("mqtt-delete-retained '/devices/BLE/#'");
    }
});