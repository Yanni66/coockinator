function play_game() {
    runShellCommand("bash /mnt/data/root/page.sh -a 3");
    if (timer3_id) {
        clearTimeout(timer3_id);
    }
    timer3_id = setTimeout(function() {
        game_lvl_qw(game_lvl);
    }, timeout3_ms);

}

function check_game(but) {
    if (but == _answer) {
        if (game_lvl == 3 || game_lvl == 6 || game_lvl == 9) {
            if (game_lvl == 9) {
                game_lvl = 1;
            } else {
                game_lvl++;
            }
            total_game(true, true);
        } else {
            game_lvl++;
            game_lvl_qw(game_lvl);
        }
    } else {
        total_game(false, true);
    }
}


function game_lvl_qw(question) {
    if (question == 1) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "1/3): 212+13*8=" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "1800" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "1709" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "560" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "316" + "'");
        _answer = 4;
    } else if (question == 2) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "2/3): 6/2*(2+1)=" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "9" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "3" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "1" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "6" + "'");
        _answer = 3;
    } else if (question == 3) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "3/3): 34*(87-46)=" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "481" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "1394" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "2605" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "1285" + "'");
        _answer = 2;
    } else if (question == 4) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "1/3): (59+84)*3/3=" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "143" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "2" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "3" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "429" + "'");
        _answer = 1;
    } else if (question == 5) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "2/3): 1712-2*10=" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "17100" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "1606" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "1692" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "17190" + "'");
        _answer = 3;
    } else if (question == 6) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "3/3): 414-14*7" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "316" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "2800" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "856" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "1920" + "'");
        _answer = 1;
    } else if (question == 7) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "1/3): (186-128)/2=" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "58" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "26" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "116" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "29" + "'");
        _answer = 4;
    } else if (question == 8) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "2/3): 1282+63*21=" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "1323" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "28245" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "1345" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "2605" + "'");
        _answer = 4;
    } else if (question == 9) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "3/3): 812+252/2=" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "1064" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "938" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "532" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "450" + "'");
        _answer = 1;
    }
}

function total_game(_result, _exit) {
    if (!_result) {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "Looser!!!" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "" + "'");
        _answer = 0;
    } else {
        runShellCommand("bash /mnt/data/root/text.sh -a t0 -b '" + "Winner!!!" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b0 -b '" + "" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b1 -b '" + "" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b2 -b '" + "" + "'");
        runShellCommand("bash /mnt/data/root/text.sh -a b3 -b '" + "" + "'");
        _answer = 0;
        dev["worm_move"]["enabled"] = 1;
    }
    if (_exit) {
        if (fin_timer_id) {
            clearTimeout(fin_timer_id);
        }
        fin_timer_id = setTimeout(function() {
            runShellCommand("bash /mnt/data/root/page.sh -a 1");
        }, fin_timeout_ms);

    }
}