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


def fft(x):
    """
    FIR filter implementation
    
    :param x: Input vector
    :return: Output vector
    """
    N = len(x)
    if N == 1:
        return x
    else:
        # Divide into even and odd index vectors and calculate their FFTs
        even = fft(x[0::2])
        odd = fft(x[1::2])
        
        # primitive roots of unity
        prim_roots = np.exp(-2j * np.pi * np.arange(int(N / 2)) / N)

        # Butterfly operation
        out = np.concatenate(
            [
                even + (prim_roots * odd),
                even - (prim_roots * odd),
            ],
            axis=None
        )

        return out


def main():
    """
    Entry point
    """
    # Load ADC data from file
    with open("data_6_6.dat", "rb") as fh:
        signal = np.frombuffer(fh.read(), dtype=np.int16)
    # signal = np.array([-0.5, 1, -2, 2])  # Data from exercise 6.4
    
    # Calculate FFT with reference implementation from NumPy
    ref = np.fft.fft(signal)
    
    # Calculate FFT with your implementation
    freq_dom = fft(signal)
    
    # Plot carthesian
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
    ax1.set_title("Input Signal")
    ax1.plot(signal)
    ax2.set_title("Own FFT Implementation")
    ax2.plot(np.real(freq_dom), label="Real")
    ax2.plot(np.imag(freq_dom), label="Imag")
    ax3.set_title("np.fft.fft (Reference Implementation)")
    ax3.plot(np.real(ref), label="Real")
    ax3.plot(np.imag(ref), label="Imag")
    
    # Plot polar
    # ATTENTION: It is 20 dB * log10 because it is a magnitude and not a power spectrum
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    ax1.set_title("Magnitude Own Implementation")
    ax1.plot(20 * np.log10(np.abs(freq_dom)))
    ax2.set_title("Magnitude Reference Implementation")
    ax2.plot(20 * np.log10(np.abs(ref)))
    ax3.set_title("Phase Own Implementation")
    ax3.plot(np.angle(freq_dom))
    ax4.set_title("Phase Reference Implementation")
    ax4.plot(np.angle(ref))

    plt.show()
    
    # Check if your implementation works.
    # It checks if the total error between your and the NumPy implementation is smaller than 1.
    # Due to rounding errors, both results might not be identical. This check should be sufficient.
    if np.linalg.norm(ref - freq_dom) < 1:
        print("Your implementation is correct")
    else:
        raise AssertionError("Your implementation is incorrect")
    

if __name__ == "__main__":
    main()


