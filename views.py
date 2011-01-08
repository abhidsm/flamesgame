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
    male_name = request['male_name']
    female_name = request['female_name']
    result = flames.calculate(male_name, female_name)
    return shortcuts.render_to_response('index.html',{'result' : result, 'male_name' : male_name, 'female_name' : female_name})
