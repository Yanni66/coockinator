defineRule("money", {
    whenChanged: "wb-gpio/MOD1_IN2",
    then: function(newValue, devName, cellName) {
        if (newValue) {
            timerLast = Date.now()
            if ((timerLast - timerTime) >= 500) {
                timerTime = Date.now();
                countMoney = 1;
            } else {
                timerTime = Date.now();
                countMoney++;
            }
            if (timer_id) {
                clearTimeout(timer_id);
            }
            timer_id = setTimeout(function() {
                if (countMoney == 5) {
                    cur(10);
                  log("Чирик")
                } else if (countMoney == 4) {
                    cur(5);
                } else if (countMoney == 3) {
                    cur(2);
                } else if (countMoney == 2) {
                    cur(1);
                }
                timer_id = null;
            }, timeout_ms);
        }
    }
});