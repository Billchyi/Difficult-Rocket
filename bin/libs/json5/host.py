# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil
import sys
import tempfile

if sys.version_info[0] < 3:
    # pylint: disable=redefined-builtin, invalid-name
    str = unicode


class Host(object):
    def __init__(self):
        self.stdin = sys.stdin
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def chdir(self, *comps):
        return os.chdir(self.join(*comps))

    def getcwd(self):
        return os.getcwd()

    def join(self, *comps):
        return os.path.join(*comps)

    def mkdtemp(self, **kwargs):
        return tempfile.mkdtemp(**kwargs)

    def print_(self, msg=u'', end=u'\n', stream=None):
        stream = stream or self.stdout
        stream.write(str(msg) + end)
        stream.flush()

    def rmtree(self, path):
        shutil.rmtree(path, ignore_errors=True)

    def read_text_file(self, path):
        with open(path, 'rb') as fp:
            return fp.read().decode('utf8')

    def write_text_file(self, path, contents):
        with open(path, 'wb') as f:
            f.write(contents.encode('utf8'))
