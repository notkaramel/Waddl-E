#!/usr/bin/evn bash

host=192.168.50.5
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub | ssh $host 'cat >> ~/.ssh/authorized_keys'
ssh $host 'chmod g-w,o-w ~; chmod 700 ~/.ssh; chmod 600 ~/.ssh/authorized_keys'
