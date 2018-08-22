function sold_done() {
    if (dev[user_active + "/Score"] >= score_price) {
        dev[user_active + "/Score"] = parseInt(dev[user_active + "/Score"]) - score_price
        dev["worm_move"]["enabled"] = 1;
    }
	sold_cancel()
}

function sold_cancel() {
    user_active = null;
    pin_cur = null;
    pin_activ = false;
    near = 0;
    runShellCommand("bash /mnt/data/root/page.sh -a 1");
}

function page_swap() {
    if (_page == 1) {
        _page = 2;
        user_chose(_page);
    } else if (_page == 2) {
        _page = 1;
        user_chose(_page);
    }
}

function pin_correct() {
    if (pin_activ) {
        pin_activ = false;
        pin_cur = null;
        user_chose_entered(user_active);
    } else {
        pin_cur = null;
        runShellCommand("bash /mnt/data/root/page.sh -a 1");
    }
}

function check_ble() {
    near = 0;
    var pruf = ble_is_near();
    if (pruf) {
        user_active = pruf;
        user_chose_entered(user_active)
    } else {
        runShellCommand("bash /mnt/data/root/page.sh -a 5");
    }
}

function user_chose(page) {
    runShellCommand("bash /mnt/data/root/page.sh -a 6");
    if (timer_user_id) {
        clearTimeout(timer_user_id);
    }
    timer_user_id = setTimeout(function() {
        if (page == 1) {
            for (var i = 1; i < 9; i++) {
                runShellCommand("bash /mnt/data/root/text.sh -a b" + butt_arr[i] + " -b '" + dev[users_arr[i] + "/name"] + "'");
            }
        } else if (page == 2) {
            for (var i = 9; i < 17; i++) {
                runShellCommand("bash /mnt/data/root/text.sh -a b" + butt_arr[i] + " -b '" + dev[users_arr[i] + "/name"] + "'");
            }
        }
        timer_user_id = null;
    }, timer_user_ms);
}

function user_chose_entered(user) {
    runShellCommand("bash /mnt/data/root/page.sh -a 8");
    if (timer2_user_id) {
        clearTimeout(timer2_user_id);
    }
    timer2_user_id = setTimeout(function() {
        if (user_active) {
            runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + dev[user_active + "/name"] + "'");
            runShellCommand("bash /mnt/data/root/text.sh -a t1 -b '" + dev[user_active + "/Score"] + "'");
            runShellCommand("bash /mnt/data/root/text.sh -a t2 -b '" + score_price + "'");
        }
        timer2_user_id = null;
    }, timer2_user_ms);
}

function user_chose_select(id) {
    runShellCommand("bash /mnt/data/root/page.sh -a 7");
    pin_cur = pin_arr[id];
    user_active = users_arr[id];
    pin_activ = true;
}