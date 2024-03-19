#!/bin/bash
echo $(date)
if ping -c 1 www.baidu.com > /dev/null 2>&1 ; then
    echo "可以访问互联网"
else
    echo "无法访问互联网"
    echo "linshuijin123" | sudo -S nmcli device wifi connect "XJTU_WLAN"    
    echo "linshuijin123" | sudo -S nmcli device wifi connect "XJTU_STU"
    echo "已恢复"
fi
