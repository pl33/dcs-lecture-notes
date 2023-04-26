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


# FIR filter coefficients
FIR_COEFFS = np.array([0, 0, -0.021, 0, 0.271, 0.501, 0.271, 0, -0.021, 0, 0])

# Down-sampling decimation factor
DECIMATION = 2


def fir_filter(signal):
    """
    FIR filter implementation
    
    :param signal: Input signal
    :return: Output signal
    """
    # Allocate memory for the feed-forward delay taps
    forward_taps = np.zeros((len(FIR_COEFFS), ))
    
    # Allocate memory for the output vector
    output = np.zeros((len(signal), ))
    
    # Do the FIR filtering
    for index, value in enumerate(signal):
        # Shift all delay taps, the last tap rolls over to the first one (which is incorrect) but will get overwritten soon
        forward_taps = np.roll(forward_taps, 1)
        # Insert the new input value into the first tap
        forward_taps[0] = value
        # Scalar product of the taps with the coefficients (multiply-accumulate operations for each tap)
        output[index] = np.dot(forward_taps, FIR_COEFFS)
        
    return output

def decimation(signal):
    """
    Down-sampler
    
    :param signal: Input signal
    :return: Output signal
    """
    # Calculate the number of output samples
    len_out = int(len(signal) / DECIMATION)

    # Allocate memory for the output vector
    output = np.zeros((len_out, ))
    
    # Decimate by taking out every DECIMATION-th sample
    for index in range(len_out):
        output[index] = signal[DECIMATION * index]
        
    return output


def main():
    """
    Entry point
    """
    # Load ADC data
    with open("data_6_5.dat", "rb") as fh:
        signal = np.frombuffer(fh.read(), dtype=np.int16)
    
    # Filter the signal
    filtered = fir_filter(signal)
    # Decimate the signal
    decimated = decimation(filtered)
    
    # Plot everything
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.set_title("Input Signal")
    ax1.plot(signal)
    ax2.set_title("After Filtering")
    ax2.plot(filtered)
    ax3.set_title("After Decimation")
    ax3.plot(decimated)
    
    plt.show()
    

if __name__ == "__main__":
    main()


