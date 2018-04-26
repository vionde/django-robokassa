# coding: utf-8
from __future__ import unicode_literals

from django.dispatch import Signal


result_received = Signal(providing_args=["InvId", "OutSum"])
success_page_visited = Signal(providing_args=["InvId", "OutSum"])
fail_page_visited = Signal(providing_args=["InvId", "OutSum"])
