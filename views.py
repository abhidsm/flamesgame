# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import flames
import django
from django.utils import simplejson
from django import http
from django.http import HttpResponse
from django import shortcuts
from google.appengine.api import mail
from google.appengine.ext import db
import threading
import datetime

def index(request):
    return shortcuts.render_to_response('index.html', {'page' : 'flames'})

def show(request):
    if len(request['security']) == 0 :
        your_name = request['your_name']
        partner_name = request['partner_name']
        result = flames.calculate(your_name, partner_name)
        final_result = get_result(result, partner_name)
        allow_share = request.POST.get('allow_share','')
    #    if allow_share == '' :
    #    SendEmail('Flames Result for ' + your_name + " and " + partner_name, final_result).start()
        share_message = "Do you want to know what type of relationship you are going to have with your dream partner? Check "
    #    return shortcuts.render_to_response('index.html',{'result' : final_result, 'status': result, 'your_name' : your_name, 'partner_name' : partner_name, 'share_message' : share_message, 'allow_share' : allow_share })
        data = {"flames": {"result": final_result, "status": result}}
        flames_data = flames.Flames(your_name = your_name, partner_name = partner_name, result = result, source = request['source'])
        flames_data.put()
        return HttpResponse(simplejson.dumps(data))

def algorithm(request):
    return shortcuts.render_to_response('algorithm.html', {'page' : 'algorithm'})

def analytics(request):
    friends_count = flames.get_analytics_for_flames('F')
    lovers_count = flames.get_analytics_for_flames('L')
    affections_count = flames.get_analytics_for_flames('A')
    marriages_count = flames.get_analytics_for_flames('M')
    enemies_count = flames.get_analytics_for_flames('E')
    sisters_count = flames.get_analytics_for_flames('S')
    total = friends_count + lovers_count + affections_count + marriages_count + enemies_count + sisters_count
    return shortcuts.render_to_response('analytics.html', {'page' : 'analytics', 'friends_count' : friends_count, 'lovers_count' : lovers_count, 'affections_count' : affections_count, 'marriages_count' : marriages_count, 'enemies_count' : enemies_count, 'sisters_count' : sisters_count, 'total' : total})

def get_result(result, partner_name):
    if result == 'F':
        return "'" + partner_name + "' is your Friend"
    elif result == 'L':
        return "'" + partner_name + "' loves you"
    elif result == 'A':
        return "'" + partner_name + "' is attracted towards you"
    elif result == 'M':
        return "You will get Married to '" + partner_name + "'"
    elif result == 'E':
        return "'" + partner_name + "' is your sworn Enemy"
    elif result == 'S':
        return "'" + partner_name + "' is your Sibling"

class SendEmail(threading.Thread): 
    def __init__(self, subject, body):
        self.user_address = "flames.game.app@gmail.com"
        self.sender_address = "abhidsm@gmail.com"
        self.subject = subject
        self.body = body
        threading.Thread.__init__(self)
    
    def run(self):
        mail.send_mail(self.sender_address, self.user_address, self.subject, self.body)

