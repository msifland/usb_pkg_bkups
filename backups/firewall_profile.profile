[fwBasic]
status = enabled
incoming = deny
outgoing = allow
routed = disabled

[Rule0]
ufw_rule = 22/tcp ALLOW IN Anywhere
description = SSH
command = /usr/sbin/ufw allow in proto tcp from any to any port 22
policy = allow
direction = in
protocol = 
from_ip = 
from_port = 
to_ip = 
to_port = 22/tcp
iface = 
routed = 
logging = 

[Rule1]
ufw_rule = 22/tcp (v6) ALLOW IN Anywhere (v6)
description = SSH
command = /usr/sbin/ufw allow in proto tcp from any to any port 22
policy = allow
direction = in
protocol = 
from_ip = 
from_port = 
to_ip = 
to_port = 22/tcp
iface = 
routed = 
logging = 

[Rule2]
ufw_rule = 882 ALLOW IN Anywhere
description = SSH
command = /usr/sbin/ufw allow in proto tcp from any to any port 882
policy = allow
direction = in
protocol = 
from_ip = 
from_port = 
to_ip = 
to_port = 882
iface = 
routed = 
logging = 

[Rule3]
ufw_rule = 882 (v6) ALLOW IN Anywhere (v6)
description = SSH
command = /usr/sbin/ufw allow in proto tcp from any to any port 882
policy = allow
direction = in
protocol = 
from_ip = 
from_port = 
to_ip = 
to_port = 882
iface = 
routed = 
logging = 
