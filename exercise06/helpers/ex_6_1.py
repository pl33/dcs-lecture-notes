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
import matplotlib.pyplot as plt

b = [2, -1]
a = [1, -0.5]

w, h = scipy.signal.freqz(b, a, 8)

print(scipy.signal.tf2zpk(b,a))

w = numpy.round(w*100)/100
h = numpy.round(h*100)/100

print("$\\phi$ in \\si{rad} & $\\left|\\underline{H}\\left(e^{j\\phi}\\right)\\right|$ & $\\arg\\left(\\underline{H}\\left(e^{j\\phi}\\right)\\right)$ in \\si{rad} \\\\")
for n in range(len(w)):
    print("$%g$ & $%g$ & $%g$ \\\\" % (w[n], abs(h[n]), (numpy.angle(h[n]))))
    
print()

elems = []
for n in range(len(w)):
    elems.append("(%g, %g)" % (w[n], abs(h[n])))
print("coordinates {%s}" % " ".join(elems))

elems = []
for n in range(len(w)):
    elems.append("(%g, %g)" % (w[n], (numpy.angle(h[n]))))
print("coordinates {%s}" % " ".join(elems))

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(w, abs(h), 'b')
ax2 = ax1.twinx()
ax2.plot(w, (numpy.angle(h)), 'g')
plt.show()
