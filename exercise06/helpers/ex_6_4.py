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

x = numpy.array([-0.5, 1, -2, 2])

print("TEST ================================")

print(numpy.fft.fft(x))

print("a) ==================================")

for k in range(4):
    eq_str = "\\underline{X}[%d] = " % (k)
    elems = []
    res = 0
    for n in range(4):
        #elems.append("\\underline{x}[%d] \\cdot e^{-j \\frac{2\\pi}{N} %d \\cdot %d}" % (n, k, n))
        elems.append("\\underline{x}[%d] \\cdot e^{-j \\frac{\\pi}{2} %d \\cdot %d}" % (n, k, n))
        res += x[n] * numpy.exp(-1j*(numpy.pi/2)*n*k)
    eq_str += " + ".join(elems)
    eq_str += " = " + str(res)
    print (eq_str)

print("d) ==================================")

E = numpy.zeros(2)
O = numpy.zeros(2)
for k in range(2):
    eq_str = "\\underline{E}[%d] = \\underline{x}[0] + \\underline{w}_2^{%d} \\cdot \\underline{x}[2]" % (k, k)
    E[k] = x[0] + numpy.exp(-1j*(numpy.pi)*k) * x[2]
    eq_str += " = " + str(E[k])
    print (eq_str)
    
    eq_str = "\\underline{O}[%d] = \\underline{x}[1] + \\underline{w}_2^{%d} \\cdot \\underline{x}[3]" % (k, k)
    O[k] = x[1] + numpy.exp(-1j*(numpy.pi)*k) * x[3]
    eq_str += " = " + str(O[k])
    print (eq_str)

for k in range(4):
    eq_str = "\\underline{X}[%d] = \\underline{E}[%d] + \\underline{w}_2^{%d} \\cdot \\underline{O}[%d]" % (k, (k%2), k, (k%2))
    res = E[k%2] + numpy.exp(-1j*(numpy.pi/2)*k) * O[k%2]
    eq_str += " = " + str(res)
    print (eq_str)
