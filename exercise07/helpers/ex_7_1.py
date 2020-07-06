#!/usr/bin/env python3

# SPDX-License-Identifier: BSD-3-Clause
#
# Copyright 2020 Philipp Le
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

import numpy
import scipy.signal

C1 = numpy.array([1,1,-1,-1])
C2 = numpy.array([1,-1,-1,1])
D = numpy.array([1,-1])

S = numpy.array([0,0,0,0,1,1,-1,-1,-1,-1,1,1,0,0,0,0])

def cross(d, dn, c, name):
    print("\\begin{equation*}")
    print("\\begin{split}")
    for n in range(len(d)-len(c)+1):
        res = 0
        syms = []
        vals = []
        for k in range(4):
            syms.append("%s[%d] \\cdot %s[%d]" % (dn, (n+k-4), name, (k)))
            vals.append("(%d) \\cdot (%d)" % (d[n+k], c[k]))
            res += d[n+k] * c[k]
        print("\\mathrm{R}_{%s%s}[%d] &= %s \\\\" % (dn, name, (n-4), " + ".join(syms)))
        print(" &= %s \\\\" % (" + ".join(vals)))
        print(" &= %d \\\\" % res)
        #print(" &= %s = \\underline{\\underline{%d}} \\\\" % (" + ".join(vals), res))
    print("\\end{split}")
    print("\\end{equation*}")

print("c) ================================")
cross(S, "S", C1, "C_{4,1}")

print("d) ================================")
cross(S, "S", C2, "C_{4,2}")

print("e) ================================")
C2ext = numpy.array([0,0,0,0,1,-1,-1,1,0,0,0,0])
cross(C2ext, "C_{4,2}", C2, "C_{4,2}")
