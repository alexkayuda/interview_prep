# System Monitoring Script

#!/bin/bash # shebang, of course

# Default Variables
THRESHOLD_CPU=80
THRESHOLD_MEMORY=80
THRESHOLD_DISK=80
LOG_FILES="/var/log/system.health.log"
EMAIL="your_email@example.com"

# Send Alert of Threshold Breached
function send_alert(){
    local MESSAGE=$1
}
