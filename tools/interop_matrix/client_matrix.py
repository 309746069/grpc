#!/usr/bin/env python2.7
# Copyright 2017 gRPC authors.
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

# Defines languages, runtimes and releases for backward compatibility testing

from collections import OrderedDict


def get_github_repo(lang):
    return {
        'dart': 'https://github.com/grpc/grpc-dart.git',
        'go': 'https://github.com/grpc/grpc-go.git',
        'java': 'https://github.com/grpc/grpc-java.git',
        'node': 'https://github.com/grpc/grpc-node.git',
        # all other languages use the grpc.git repo.
    }.get(lang, 'https://github.com/grpc/grpc.git')


def get_release_tags(lang):
    """Returns list of known releases for given language."""
    return list(LANG_RELEASE_MATRIX[lang].keys())


def get_runtimes_for_lang_release(lang, release):
    """Get list of valid runtimes for given release of lang."""
    runtimes_to_skip = []
    release_info = LANG_RELEASE_MATRIX[lang][release]
    if release_info:
        runtimes_to_skip = release_info.skip_runtime
    return [
        runtime for runtime in LANG_RUNTIME_MATRIX[lang]
        if runtime not in runtimes_to_skip
    ]


def should_build_docker_interop_image_from_release_tag(lang):
    # All dockerfile definitions live in grpc/grpc repository.
    # For language that have a separate repo, we need to use
    # dockerfile definitions from head of grpc/grpc.
    if lang in ['go', 'java', 'node']:
        return False
    return True


# Dictionary of runtimes per language
LANG_RUNTIME_MATRIX = {
    'cxx': ['cxx'],  # This is actually debian8.
    'go': ['go1.8', 'go1.11'],
    'java': ['java_oracle8'],
    'python': ['python'],
    'node': ['node'],
    'ruby': ['ruby'],
    'php': ['php', 'php7'],
    'csharp': ['csharp', 'csharpcoreclr'],
}


class ReleaseInfo:
    """Info about a single release of a language"""

    def __init__(self, patch=[], skip_runtime=[], testcases_file=None):
        self.patch = patch
        self.skip_runtime = skip_runtime
        self.testcases_file = None


# Dictionary of known releases for given language.
LANG_RELEASE_MATRIX = {
    'cxx':
    OrderedDict([
        ('v1.0.1', ReleaseInfo()),
        ('v1.1.4', ReleaseInfo()),
        ('v1.2.5', ReleaseInfo()),
        ('v1.3.9', ReleaseInfo()),
        ('v1.4.2', ReleaseInfo()),
        ('v1.6.6', ReleaseInfo()),
        ('v1.7.2', ReleaseInfo()),
        ('v1.8.0', ReleaseInfo()),
        ('v1.9.1', ReleaseInfo()),
        ('v1.10.1', ReleaseInfo()),
        ('v1.11.1', ReleaseInfo()),
        ('v1.12.0', ReleaseInfo()),
        ('v1.13.0', ReleaseInfo()),
        ('v1.14.1', ReleaseInfo()),
        ('v1.15.0', ReleaseInfo()),
        ('v1.16.0', ReleaseInfo()),
        ('v1.17.1', ReleaseInfo()),
    ]),
    'go':
    OrderedDict([
        ('v1.0.5', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.2.1', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.3.0', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.4.2', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.5.2', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.6.0', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.7.4', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.8.2', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.9.2', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.10.1', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.11.3', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.12.2', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.13.0', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.14.0', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.15.0', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.16.0', ReleaseInfo(skip_runtime=['go1.11'])),
        ('v1.17.0', ReleaseInfo(skip_runtime=['go1.8'])),
    ]),
    'java':
    OrderedDict([
        ('v1.0.3', ReleaseInfo()),
        ('v1.1.2', ReleaseInfo()),
        ('v1.2.0', ReleaseInfo()),
        ('v1.3.1', ReleaseInfo()),
        ('v1.4.0', ReleaseInfo()),
        ('v1.5.0', ReleaseInfo()),
        ('v1.6.1', ReleaseInfo()),
        ('v1.7.0', ReleaseInfo()),
        ('v1.8.0', ReleaseInfo()),
        ('v1.9.1', ReleaseInfo()),
        ('v1.10.1', ReleaseInfo()),
        ('v1.11.0', ReleaseInfo()),
        ('v1.12.0', ReleaseInfo()),
        ('v1.13.1', ReleaseInfo()),
        ('v1.14.0', ReleaseInfo()),
        ('v1.15.0', ReleaseInfo()),
        ('v1.16.1', ReleaseInfo()),
        ('v1.17.1', ReleaseInfo()),
    ]),
    'python':
    OrderedDict([
        ('v1.0.x', ReleaseInfo()),
        ('v1.1.4', ReleaseInfo()),
        ('v1.2.5', ReleaseInfo()),
        ('v1.3.9', ReleaseInfo()),
        ('v1.4.2', ReleaseInfo()),
        ('v1.6.6', ReleaseInfo()),
        ('v1.7.2', ReleaseInfo()),
        ('v1.8.1', ReleaseInfo()),
        ('v1.9.1', ReleaseInfo()),
        ('v1.10.1', ReleaseInfo()),
        ('v1.11.1', ReleaseInfo()),
        ('v1.12.0', ReleaseInfo()),
        ('v1.13.0', ReleaseInfo()),
        ('v1.14.1', ReleaseInfo()),
        ('v1.15.0', ReleaseInfo()),
        ('v1.16.0', ReleaseInfo()),
        ('v1.17.1', ReleaseInfo()),
    ]),
    'node':
    OrderedDict([
        ('v1.0.1', ReleaseInfo()),
        ('v1.1.4', ReleaseInfo()),
        ('v1.2.5', ReleaseInfo()),
        ('v1.3.9', ReleaseInfo()),
        ('v1.4.2', ReleaseInfo()),
        ('v1.6.6', ReleaseInfo()),
        # TODO: https://github.com/grpc/grpc-node/issues/235.
        # ('v1.7.2', ReleaseInfo()),
        ('v1.8.4', ReleaseInfo()),
        ('v1.9.1', ReleaseInfo()),
        ('v1.10.0', ReleaseInfo()),
        ('v1.11.3', ReleaseInfo()),
        ('v1.12.4', ReleaseInfo()),
    ]),
    'ruby':
    OrderedDict([
        ('v1.0.1',
         ReleaseInfo(patch=[
             'tools/dockerfile/interoptest/grpc_interop_ruby/Dockerfile',
             'tools/dockerfile/interoptest/grpc_interop_ruby/build_interop.sh',
         ])),
        ('v1.1.4', ReleaseInfo()),
        ('v1.2.5', ReleaseInfo()),
        ('v1.3.9', ReleaseInfo()),
        ('v1.4.2', ReleaseInfo()),
        ('v1.6.6', ReleaseInfo()),
        ('v1.7.2', ReleaseInfo()),
        ('v1.8.0', ReleaseInfo()),
        ('v1.9.1', ReleaseInfo()),
        ('v1.10.1', ReleaseInfo()),
        ('v1.11.1', ReleaseInfo()),
        ('v1.12.0', ReleaseInfo()),
        ('v1.13.0', ReleaseInfo()),
        ('v1.14.1', ReleaseInfo()),
        ('v1.15.0', ReleaseInfo()),
        ('v1.16.0', ReleaseInfo()),
        ('v1.17.1', ReleaseInfo()),
    ]),
    'php':
    OrderedDict([
        ('v1.0.1', ReleaseInfo()),
        ('v1.1.4', ReleaseInfo()),
        ('v1.2.5', ReleaseInfo()),
        ('v1.3.9', ReleaseInfo()),
        ('v1.4.2', ReleaseInfo()),
        ('v1.6.6', ReleaseInfo()),
        ('v1.7.2', ReleaseInfo()),
        ('v1.8.0', ReleaseInfo()),
        ('v1.9.1', ReleaseInfo()),
        ('v1.10.1', ReleaseInfo()),
        ('v1.11.1', ReleaseInfo()),
        ('v1.12.0', ReleaseInfo()),
        ('v1.13.0', ReleaseInfo()),
        ('v1.14.1', ReleaseInfo()),
        ('v1.15.0', ReleaseInfo()),
        ('v1.16.0', ReleaseInfo()),
        ('v1.17.1', ReleaseInfo()),
    ]),
    'csharp':
    OrderedDict([
        ('v1.0.1',
         ReleaseInfo(patch=[
             'tools/dockerfile/interoptest/grpc_interop_csharp/Dockerfile',
             'tools/dockerfile/interoptest/grpc_interop_csharpcoreclr/Dockerfile',
         ])),
        ('v1.1.4', ReleaseInfo()),
        ('v1.2.5', ReleaseInfo()),
        ('v1.3.9', ReleaseInfo()),
        ('v1.4.2', ReleaseInfo()),
        ('v1.6.6', ReleaseInfo()),
        ('v1.7.2', ReleaseInfo()),
        ('v1.8.0', ReleaseInfo()),
        ('v1.9.1', ReleaseInfo()),
        ('v1.10.1', ReleaseInfo()),
        ('v1.11.1', ReleaseInfo()),
        ('v1.12.0', ReleaseInfo()),
        ('v1.13.0', ReleaseInfo()),
        ('v1.14.1', ReleaseInfo()),
        ('v1.15.0', ReleaseInfo()),
        ('v1.16.0', ReleaseInfo()),
        ('v1.17.1', ReleaseInfo()),
    ]),
}

# This matrix lists the version of testcases to use for a release. As new
# releases come out, some older docker commands for running tests need to be
# changed, hence the need for specifying which commands to use for a
# particular version in some cases. If not specified, xxx__master file will be
# used. For example, all java versions will run the commands in java__master.
# The testcases files exist under the testcases directory.
# TODO(jtattermusch): make this data part of LANG_RELEASE_MATRIX,
# there is no reason for this to be a separate data structure.
TESTCASES_VERSION_MATRIX = {
    'node_v1.0.1': 'node__v1.0.1',
    'node_v1.1.4': 'node__v1.1.4',
    'node_v1.2.5': 'node__v1.1.4',
    'node_v1.3.9': 'node__v1.1.4',
    'node_v1.4.2': 'node__v1.1.4',
    'node_v1.6.6': 'node__v1.1.4',
    'ruby_v1.0.1': 'ruby__v1.0.1',
    'csharp_v1.0.1': 'csharp__v1.1.4',
    'csharp_v1.1.4': 'csharp__v1.1.4',
    'csharp_v1.2.5': 'csharp__v1.1.4',
    'python_v1.0.x': 'python__v1.0.x',
    'python_v1.1.4': 'python__v1.0.x',
    'python_v1.2.5': 'python__v1.0.x',
    'python_v1.3.9': 'python__v1.0.x',
    'python_v1.4.2': 'python__v1.0.x',
    'python_v1.6.6': 'python__v1.0.x',
    'python_v1.7.2': 'python__v1.0.x',
    'python_v1.8.1': 'python__v1.0.x',
    'python_v1.9.1': 'python__v1.0.x',
    'python_v1.10.1': 'python__v1.0.x',
}
