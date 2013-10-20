This is a script that will help set up your Mac OS X system to automatically
connect to your SSH SOCKS proxy when you switch to a SOCKS-enabled Network
Location.

When you are traveling/on insecure wifi networks, using this will help make
sure your traffic is secure.

INSTALL
---
Run the `install` script


HOW IT WORKS
---
We add a LaunchAgent to run the `autotunnel` script to detect when your active
Network Location profile has changed.  If set to a SOCKS-enabled profile, it 
enables another LaunchAgent to start an autossh session.  If changed to a 
non-SOCKS profile, we disable that LaunchAgent, stopping autossh.


SEE ALSO
---
* http://randomfoo.net/blog/id/3908
* http://richardkmiller.com/925/script-to-enabledisable-socks-proxy-on-mac-os-x
* http://chetansurpur.com/projects/sidestep/
  https://github.com/chetan51/sidestep
  this looks like the easiest/most developed solution? however, like sheepsafe
  it switches locations automatically (based on whether wifi is secure or not).
  that means it switches only after you're connected, so may also suffer the
  problem of auto-reconnecting apps like Adium? also not sure how compatible it
  is with captive portals...
* http://codesorcery.net/meerkat 
  commercial alternative for non-technical users
* https://github.com/nicksieger/sheepsafe
  this looks similar to what I wrote; uses ssh vs autossh; switches locations 
  based on known wifi; runs as daemon; if this switches only after you jump on
  unknown wireless, doesn't it close the barn doors a bit late for 
  auto-reconnecting apps like Adium?
* https://github.com/apenwarr/sshuttle
  http://apenwarr.ca/log/?m=201102#04
  requires root access (mucks w/ your iptables) but looks like it does some
  neat stuff?
