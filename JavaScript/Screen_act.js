defineRule("screen_cont", {
    whenChanged: "screen/raw",
    then: function(newValue, devName, cellName) {
        if (newValue != "") {
            if (newValue == "100") {
                runShellCommand("bash /mnt/data/root/page.sh -a 1")
            } else if (newValue == "200") {
                runShellCommand("bash /mnt/data/root/page.sh -a 4");
            } else if (newValue == "201") {
                buy_game();
            } else if (newValue == "202") {
                sale = false;
                sale1 = false;
                runShellCommand("bash /mnt/data/root/page.sh -a 1")
            } else if (newValue == "103") {
                runShellCommand("bash /mnt/data/root/page.sh -a 1")
            } else if (newValue == "301") {
                check_game("1");
            } else if (newValue == "302") {
                check_game("4");
            } else if (newValue == "303") {
                check_game("2");
            } else if (newValue == "304") {
                check_game("3");
            } else if (newValue == "403") {
                runShellCommand("bash /mnt/data/root/page.sh -a 1");
            } else if (newValue == "501") {
                runShellCommand("bash /mnt/data/root/page.sh -a 1");
            } else if (newValue == "401") {
                runShellCommand("bash /mnt/data/root/page.sh -a 2");
                buy_cookie();
            } else if (newValue == "402") {
                check_ble();
            } else if (newValue == "502") {
                user_chose(_page);
            } else if (newValue == "700") {
                sold_cancel();
            } else if (newValue == "801") {
                sold_cancel();
            } else if (newValue == "802") {
                sold_done();
            } else if (newValue == "601") {
                page_swap();
            } else if (newValue == "602") {
                page_swap();
            } else if (newValue == "pin_" + pin_cur) {
                pin_correct();
            } else {
                if (newValue != "") {
                    users_arr.forEach(function(item, i, arr) {
                        if (newValue == dev[item + "/name"]) {
                            user_chose_select(i);
                        }
                    });
                }
            }
            dev["screen"]["raw"] = "";
        }
    }
});