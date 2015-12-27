#!/bin/env python

from __future__ import print_function

from nimrod_vim import execNimCmd


proj = "/foo"


while True:
    line = raw_input("enter command: ")
    async_ = False

    if line == 'quit':
        async_ = True

    print(execNimCmd(proj, line, async_))

    if line == 'quit':
        break
