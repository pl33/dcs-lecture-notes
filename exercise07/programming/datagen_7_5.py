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

# DSSS code and spreading factor
DSSS_CODE = np.array([+1, +1, +1, -1, -1, -1, +1, -1, -1, +1, -1])
SPREADING_FACTOR = len(DSSS_CODE)

AMPLITUDE = 128
DATA = np.array([+1, +1, -1, -1, +1, -1, +1, -1])



def main():
    """
    Entry point
    """
    np.random.seed(10000)
    
    exteneded = np.repeat(np.array([DATA]), SPREADING_FACTOR, axis=0).transpose()
    dsss = np.concatenate(exteneded * DSSS_CODE) * AMPLITUDE
    noise = np.random.normal(0, 128.0, len(dsss))
    
    signal = dsss + noise
    
    with open("data_7_5_dsss.dat", "wb") as fh:
        data = signal.astype(np.int16).tobytes()
        fh.write(data)
    

if __name__ == "__main__":
    main()
