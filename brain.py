#!/usr/bin/env python
#coding:utf-8

import os
import aiml

kernel = aiml.Kernel()


if os.path.isfile("rebot_brain.brn"):
    kernel.bootstrap(brainFile="rebot_brain.bin")
else:
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    kernel.saveBrain("rebot_brain.bin")



while True:
    message = raw_input("Enter your message to the bot: ")
    if message == "quit":
        exit()
    elif message == "save":
        kernel.saveBrain("rebot_brain.brn")
    else:
        bot_response = kernel.respond(message)
        print "rob say: %s" % bot_response
        # bot_response() 回复某些信息
