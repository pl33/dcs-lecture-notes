#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2023 Philipp Le
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.

import json
import os
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from typing import AnyStr, Dict


SCRIPT_DIR = os.path.dirname(__file__)
OUTDIR = os.path.join(SCRIPT_DIR, "build", "programming")


@dataclass
class Package:
    archive: AnyStr
    files: Dict[AnyStr, AnyStr] = field(default_factory=lambda: {})
    scripts: Dict[AnyStr, AnyStr] = field(default_factory=lambda: {})


PACKAGES = [
    Package(
        archive="Templates 1",
        files={
            "Ex 2.7": "exercise02/programming/template_2_7.py",
            "Ex 2.8": "exercise02/programming/template_2_8.py",
            "Ex 3.6": "exercise03/programming/template_3_6.py",
            "Ex 4.4": "exercise04/programming/template_4_4.py",
        },
        scripts={
            "Ex 3.6": "exercise03/programming/datagen_3_6.py",
        },
    ),
    Package(
        archive="Solutions 1",
        files={
            "Ex 2.7": "exercise02/programming/solution_2_7.py",
            "Ex 2.8": "exercise02/programming/solution_2_8.py",
            "Ex 3.6": "exercise03/programming/solution_3_6.py",
            "Ex 4.4": "exercise04/programming/solution_4_4.py",
        },
    ),
    Package(
        archive="Templates 2",
        files={
            "Ex 5.5": "exercise05/programming/template_5_5.py",
            "Ex 5.6": "exercise05/programming/template_5_6.py",
            "Ex 6.5": "exercise06/programming/template_6_5.py",
            "Ex 6.6": "exercise06/programming/template_6_6.py",
        },
        scripts={
            "Ex 5.5": "exercise05/programming/datagen_5_5.py",
            "Ex 6.5": "exercise06/programming/datagen_6_5.py",
            "Ex 6.6": "exercise06/programming/datagen_6_6.py",
        },
    ),
    Package(
        archive="Solutions 2",
        files={
            "Ex 5.5": "exercise05/programming/solution_5_5.py",
            "Ex 5.6": "exercise05/programming/solution_5_6.py",
            "Ex 6.5": "exercise06/programming/solution_6_5.py",
            "Ex 6.6": "exercise06/programming/solution_6_6.py",
        },
    ),
    Package(
        archive="Templates 3",
        files={
            "Ex 7.5": "exercise07/programming/template_7_5.py",
            "Ex 7.6": "exercise07/programming/template_7_6.py",
            "Ex 8.6": "exercise08/programming/template_8_6.py",
        },
        scripts={
            "Ex 7.5": "exercise07/programming/datagen_7_5.py",
            "Ex 7.6": "exercise07/programming/datagen_7_6.py",
        },
    ),
    Package(
        archive="Solutions 3",
        files={
            "Ex 7.5": "exercise07/programming/solution_7_5.py",
            "Ex 7.6": "exercise07/programming/solution_7_6.py",
            "Ex 8.6": "exercise08/programming/solution_8_6.py",
        },
    ),
]


def prepare_dir(tmpdir: AnyStr, files: Dict[AnyStr, AnyStr]):
    """
    Make source and destination paths and create the destination directory
    """
    for subdir, path in files.items():
        src_path = os.path.join(SCRIPT_DIR, path)
        fname = os.path.basename(path)
        dst_dir = os.path.join(tmpdir, subdir)
        dst_path = os.path.join(dst_dir, fname)
        
        os.makedirs(dst_dir, exist_ok=True)
        yield src_path, dst_dir, dst_path
    

def make_package(pkg: Package, git_meta):
    """
    Make a package
    """
    tmpdir = tempfile.mkdtemp()
    try:
        git_meta_str = json.dumps(git_meta, indent=4)
        git_meta_file = os.path.join(tmpdir, ".git_meta")
        with open(git_meta_file, "w") as fh:
            fh.write(git_meta_str)
        
        for src_path, _, dst_path in prepare_dir(tmpdir, pkg.files):
            shutil.copy2(src_path, dst_path)
            
        for src_path, dst_dir, _ in prepare_dir(tmpdir, pkg.scripts):
            subprocess.run(["python", src_path], cwd=dst_dir, check=True)
            
        archive_out = os.path.join(OUTDIR, pkg.archive)
        shutil.make_archive(archive_out, "zip", tmpdir)
    finally:
        shutil.rmtree(tmpdir)


def read_stdout(stdout: bytes):
    """
    Extract first line from stdout
    """
    s = str(stdout, "utf-8")
    lines = s.split("\n")
    return lines[0]


def get_metadata():
    """
    Get Git metadata
    """
    sha1 = subprocess.run(["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE, cwd=SCRIPT_DIR, check=True)
    timestamp = subprocess.run(["git", "log", "-1", "--format=%cd", "--date=iso8601"], stdout=subprocess.PIPE, cwd=SCRIPT_DIR, check=True)
    commit_no = subprocess.run(["git", "rev-list", "--count", "HEAD"], stdout=subprocess.PIPE, cwd=SCRIPT_DIR, check=True)
    dirty = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE, cwd=SCRIPT_DIR, check=True)
    
    metadata = {
        "git_commit": {
            "sha1": read_stdout(sha1.stdout),
            "timestamp": read_stdout(timestamp.stdout),
            "serial": int(read_stdout(commit_no.stdout)),
            "dirty": len(dirty.stdout) != 0,
        },
    }
        
    return metadata


def main():
    git_meta = get_metadata()
    
    os.makedirs(OUTDIR, exist_ok=True)
    
    for pkg in PACKAGES:
        make_package(pkg, git_meta)


if __name__ == "__main__":
    main()
