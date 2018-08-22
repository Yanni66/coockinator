runShellCommand("bash /mnt/data/root/page.sh -a 0");
runShellCommand("bash /mnt/data/root/serial.sh");

mac_arr.forEach(function(item, i, arr) {
    if (item != "") {
        runShellCommand("python3 /mnt/data/root/__main__.py -m " + item);
    }
});

defineRule("cron_timer_", {
    when: cron("@every 0h10m0s"),
    then: function() {
        runShellCommand("python3 /mnt/data/root/r.py");
    }
});