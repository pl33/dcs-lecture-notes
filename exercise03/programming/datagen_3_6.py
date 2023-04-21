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


N_SAMPLES = 512
AMPLITUDE = 5.0
WIDTH = 0.1 * N_SAMPLES
SHIFT = 0.3 * N_SAMPLES
STD_DEV = 1.0


def save(x, filename):
    """
    Save array to file
    """
    data = x.astype(np.int16).tobytes()
    with open(filename, "wb") as fh:
        fh.write(data)


def main():
    """
    Entry point
    """
    np.random.seed(10000)
    
    t = np.arange(0, N_SAMPLES)
    
    gauss = AMPLITUDE * np.exp(-1 * np.power((t - SHIFT), 2) / (2 * np.power(WIDTH, 2)))
    noise = []
    for _ in range(3):
        noise.append(np.random.normal(0, STD_DEV, len(t)))
        
    save(noise[0], "signal_1.dat")
    save(gauss + noise[1], "signal_2.dat")
    save(noise[2], "signal_3.dat")
    
    

if __name__ == "__main__":
    main()


