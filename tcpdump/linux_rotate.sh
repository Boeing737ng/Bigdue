#!/bin/bash

SRCDIR="$(dirname ${BASH_SOURCE[0]})"
cd ${SRCDIR}

trap ctrl_c INT

function ctrl_c() {
    chmod -R 777 data
}

mkdir -p data
tcpdump -i any -C 1024 -w data/`date -u +%s_%N`.pcap ip
