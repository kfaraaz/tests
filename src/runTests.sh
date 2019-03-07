#!/bin/sh

for i in {1..100}
do
/opt/mapr/drill/drill-1.13.0/bin/sqlline -u "jdbc:drill:schema=dfs.tmp;drillbit=a.b.c.d" -n test -p test -f /root/query.sql
done
