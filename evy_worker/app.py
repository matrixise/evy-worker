# -*- coding: utf-8 -*-
import contextlib
import datetime
import functools
import logging
import os
import socket

from redis import Redis
from rq import Connection
from rq import Queue
from rq import Worker

import redis
import stevedore

import jinja2

import outbox

def main():
    with Connection():
        queues = [Queue('builds'), Queue('send_email')]
        Worker(queues).work()
