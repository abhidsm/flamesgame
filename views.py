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
    return shortcuts.render_to_response('index.html', {'allow_share' : 'on'})

def show(request):
    if len(request['security']) == 0 :
        your_name = request['your_name']
        partner_name = request['partner_name']
        result = flames.calculate(your_name, partner_name)
        final_result = get_result(result, partner_name)
        allow_share = request.POST.get('allow_share','')
    #    if allow_share == '' :
        SendEmail('Flames Result for ' + your_name + " and " + partner_name, final_result).start()
        share_message = "Do you want to know what type of relationship you are going to have with your dream partner? Check "
    #    return shortcuts.render_to_response('index.html',{'result' : final_result, 'status': result, 'your_name' : your_name, 'partner_name' : partner_name, 'share_message' : share_message, 'allow_share' : allow_share })
        data = {"flames": {"result": final_result, "status": result}}
        flames_data = flames.Flames(your_name = your_name, partner_name = partner_name, result = result)
        flames_data.put()
        return HttpResponse(simplejson.dumps(data))

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

