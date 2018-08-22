function cur(ruble) {
    MoneyTotal = MoneyTotal + ruble;
    bank = bank + ruble;
    dev["cur_money"]["curent"] = ruble;
    dev["cur_money"]["total"] = MoneyTotal;
    dev["cur_money"]["bank"] = bank;
    if (!sale && !sale1) {
        runShellCommand("bash /mnt/data/root/page.sh -a 2");
        buy_cookie();
    } else if (sale) {
        buy_cookie();
    } else if (sale1) {
        buy_game();
    }
}
function buy_cookie() {
    sale = true;
    if (MoneyTotal >= price) {
        MoneyTotal = (MoneyTotal - price);
        runShellCommand("bash /mnt/data/root/page.sh -a 1");
        dev["worm_move"]["enabled"] = 1;
        sale = false;
    } else {
        if (timer1_id) {
            clearTimeout(timer1_id);
        }
        timer1_id = setTimeout(function() {
            runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + price + "'");
            runShellCommand("bash /mnt/data/root/text.sh -a t1 -b '" + MoneyTotal + "'");
            timer1_id = null;
        }, timeout1_ms);
    }
}

function buy_game() {
    runShellCommand("bash /mnt/data/root/page.sh -a 2");
    sale1 = true;
    if (timer2_id) {
        clearTimeout(timer2_id);
    }
    timer2_id = setTimeout(function() {
        if (MoneyTotal >= gamePrice) {
            MoneyTotal = (MoneyTotal - gamePrice);
            play_game();
            sale1 = false;
        }
        timer2_id = null;
    }, timeout2_ms);

    if (timer_id_b_game) {
        clearTimeout(timer_id_b_game);
    }
    timer_id_b_game = setTimeout(function() {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + gamePrice + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a t1 -b '" + MoneyTotal + "'");
        timer_id_b_game = null;
    }, timeout_ms_b_game);
}