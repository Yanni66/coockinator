defineRule("worm_move_control", {
    whenChanged: "worm_move/enabled",
    then: function(newValue, devName, cellName) {
        if (newValue) {
            if (worm_timer_id) {
                clearTimeout(worm_timer_id);
            }
            worm_timer_id = setTimeout(function() {
                dev["worm_move"]["enabled"] = 0;
                worm_timer_id = null;
            }, worm_timer);
        }
        dev["wb-gpio"]["MOD2_OUT1"] = dev["worm_move"]["enabled"];
    }
});