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
from django import http
from django import shortcuts

def index(request):
    return shortcuts.render_to_response('index.html')

def show(request):
    your_name = request['your_name']
    partner_name = request['partner_name']
    result = flames.calculate(your_name, partner_name)
    final_result = get_result(result, partner_name)
    return shortcuts.render_to_response('index.html',{'result' : final_result, 'your_name' : your_name, 'partner_name' : partner_name})

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
        return "'" + partner_name + "' is your loving Sister"

