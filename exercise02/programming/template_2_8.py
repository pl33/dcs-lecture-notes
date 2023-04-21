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

import numpy as np
import matplotlib.pyplot as plt


AMPLITUDE = 2
BASE_FREQUENCY_HZ = 0.5
T_START = -3
T_END = 3
SAMPLE_PERIOD = 10e-3
N_MAX = 10
DC_BIAS = 0.3


def get_a_n(n):
    """
    Generate data and plot it
    """
    if n == 0:
        a_n = # TODO: How much?
    else:
        a_n = # TODO: How much?
    return a_n


def make_sinusoidal(t, n):
    a_n = get_a_n(n)
    y = # TODO: Implement function
    return y


def main():
    """
    Entry point
    """
    t = np.arange(T_START, T_END, SAMPLE_PERIOD)
    
    superimposition = np.zeros(t.shape)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    
    for n in range(N_MAX):
        y = make_sinusoidal(t, n)
        ax1.plot(t, y)
        
        superimposition += y
    
    ax2.plot(t, superimposition)
    
    plt.show()
    
    

if __name__ == "__main__":
    main()


