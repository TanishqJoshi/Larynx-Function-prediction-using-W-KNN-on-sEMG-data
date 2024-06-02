import numpy as np

def tunable_q_filter_s3(sig):
    j = 0
    spec = {}
    q_array = np.zeros(34)
    band = np.zeros(34)
    re = np.zeros(34)
    Jl = np.zeros(34)
    rt = np.zeros(34)

    for Q, J in [(1, 19), (1.45, 22), (1.87, 24), (2.33, 26), (2.72, 27), (3.14, 28), (3.58, 29), (4.06, 30), 
                 (4.56, 31), (5.1, 32), (5.68, 33), (6.1, 33), (6.56, 33), (7.04, 33), (7.56, 33), (7.87, 32), 
                 (8.2, 31), (8.56, 30), (8.93, 29), (9.63, 29), (10.37, 29), (10.8, 28), (11.28, 27), (11.4, 25), 
                 (11.93, 24), (12.5, 23), (13.1, 22), (13.8, 21), (13.94, 19), (14.1, 17), (14.98, 16), (15.17, 14), 
                 (15.4, 12), (15.6, 10), (15.9, 8), (16.2, 6), (16.5, 4), (19.5, 3), (23.7, 2), (24.5, 1)]:
        r = 9
        deco1 = tqwt_radix2(sig, Q, r, J)
        spec[j] = deco1[J]
        q_array[j] = Q
        band[j] = J
        re[j] = r
        Jl[j] = J
        rt[j] = np.sum(deco1[J]**2) / (np.sum(sig**2) - np.sum(deco1[J]**2))
        j += 1

    return spec, q_array, band, re, Jl, rt

import numpy as np

def tqwt_radix2(sig, Q, r, J):
    N = len(sig)
    p = int(np.log2(N))
    dec = np.zeros((N, p+1), dtype=np.complex128)

    sig = sig * 2**r

    for L in range(1, p+1):
        # Splitting
        for k in range(0, N, 2**L):
            # Weighting
            dec[k:k+2**L, L] = sig[k:k+2**L] * np.exp(-1j * np.pi * (k + 2**(L-1)) / Q)

        # Quad Merging
        for k in range(0, N, 2**(L+1)):
            for l in range(0, 2**L):
                e = dec[k+l, L]
                o = dec[k+l+2**(L-1), L]
                dec[k+l, L] = e + o
                dec[k+l+2**(L-1), L] = e - o

    dec[:, p] = dec[:, p] / N

    return dec
