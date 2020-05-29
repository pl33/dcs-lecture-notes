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

def latex_table(ar):
    return " & ".join(["$"+str(it)+"$" for it in ar])

x = numpy.array([0.25, 1, -0.5, 0.5, -0.5, -1, -0.5, -0.75])
print("$x[n]$ & "+latex_table(x))

w = 0.54 - 0.46 * numpy.cos(2*numpy.pi*numpy.array([0,1,2])/2)
w = numpy.concatenate([w, numpy.zeros(1)])
print("$w[n]$ & "+latex_table(w))

x_w = x[0:4]*w
print("$x_w[n]$ & "+latex_table(x_w))

Xft = numpy.fft.fft(x_w)
Xft_abs = numpy.abs(Xft)
Xft_phase = numpy.angle(Xft)
print("$\\underline{X}_w[k]$ & "+latex_table(Xft))
print("$|\\underline{X}_w[k]|$ & "+latex_table(Xft_abs))
print("$\\arg\\left(\\underline{X}_w[k]\\right)$ & "+latex_table(Xft_phase))

phi=2*numpy.pi*numpy.array([0,1,2,3])/4
omega=phi/1e-3
f=omega/(2*numpy.pi)
print("$\\phi[k]$ & "+latex_table(phi))
print("$\\omega[k]$ & "+latex_table(omega))
print("$f[k]$ & "+latex_table(f))

