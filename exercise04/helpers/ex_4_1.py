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

print("$n$ & "+latex_table([int(num) for num in numpy.linspace(0,8,9)]))

t=numpy.linspace(0,1e-6,9)
print("$t$ in \\si{\\micro\\second} & "+latex_table(t*1e6))

x=2*numpy.cos(2*numpy.pi*2e6*t+(numpy.pi/3))
print("$u[n]$ in \\si{V} & "+latex_table(numpy.round(x*100)/100))

print("")

phi=2*numpy.pi*numpy.array([0,1,2,3])/4
omega=phi/125e-9
f=omega/(2*numpy.pi)
print("$\\phi[k]$ & "+latex_table(numpy.round(phi*100)/100))
print("$\\omega[k]$ & "+latex_table(numpy.round(omega*100)/100))
print("$f[k]$ & "+latex_table(f))


Xft = numpy.fft.fft(x[0:4])
Xft_abs = numpy.abs(Xft)
Xft_phase = numpy.angle(Xft)
print("$\\underline{U}[k]$ & "+latex_table(numpy.round(Xft*100)/100))
print("$|\\underline{U}[k]|$ & "+latex_table(numpy.round(Xft_abs*100)/100))
print("$\\arg\\left(\\underline{U}[k]\\right)$ & "+latex_table(numpy.round(Xft_phase*100)/100))
