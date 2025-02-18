#!/usr/bin/env python3

import	matplotlib.pyplot as plt
import	numpy as np
import	math
import	cmath
import	random

N					= 2048
measurement_points	= 50
base_frequency		= 1
noise_amplitude		= 0.1

x	= np.linspace( 0, N - 1, N )
rng	= np.random.default_rng()

def main():
	amplitude_freq_phase	= [ 
		(x / measurement_points, 
		x + base_frequency, 
		x * (360 / measurement_points)) 
			for x in range( measurement_points ) ]
	
	results	= []
	
	for afp in amplitude_freq_phase:
		freq			= afp[ 1 ] * (x / N) * 2 * np.pi
		phase_radian	= np.pi / (180 / afp[ 2 ] ) if afp[ 2 ] else 0

		y	= afp[ 0 ] * np.sin( freq + phase_radian )
		n	= rng.random( N )

		y	+= (n - 0.5) * noise_amplitude * 2

		results	+= [ singlepoint_ft( y, afp[ 1 ] ) ]

	
	for r in results:
		print( f"result= {r}  .. abs:{abs( r )}, phase[°]:{cmath.phase( r ) * 180 / np.pi}" )

	plot_cplane( results, f"graphout/cplane.png" )

def	singlepoint_ft( wave, freq ):
	f	= freq * (x / N) * 2 * np.pi
	
	s	= np.sin( f )
	c	= np.cos( f )

	r	= wave * s
	i	= wave * c

	plot_timedomain( wave, s, c, r, i, freq, f"graphout/timedomain_{freq:.2f}.png" )

	return	complex( sum( r ) / (N / 2), sum( i ) / (N / 2) )
	
	
def plot_timedomain( wave, s, c, r, i, freq, filename = None ):
	fig	= plt.figure( figsize=( 18, 6 ) )
	ax	= fig.add_subplot( 111 )
	yspan	= 1 + noise_amplitude
	ax.set_ylim( [ -yspan, yspan ] )

	plt.plot( x, wave, color = [ 0, 0, 0 ], alpha = 1.0, label = "wave" )
	plt.plot( x, s, color = [ 0, 0, 1 ], alpha = 0.1, label = "sin()" )
	plt.plot( x, c, color = [ 1, 0, 0 ], alpha = 0.1, label = "cos()" )
	plt.plot( x, r, color = [ 0, 0, 1 ], alpha = 0.7, label = "wave * sin()" )
	plt.plot( x, i, color = [ 1, 0, 0 ], alpha = 0.7, label = "wave * cos()" )

	plt.grid( which = "major", alpha=0.8 )
	plt.grid( which = "minor", alpha=0.3 )
	ax.text( 0, 1.0, f"f={freq:.2f}, noise_amplitude={noise_amplitude}, N={N}" )

	if filename:
		plt.savefig( filename )
	else:
		plt.show()

def plot_cplane( results, filename = None ):
	fig	= plt.figure( figsize=( 6, 6 ) )
	ax	= fig.add_subplot( 111 )
	ax.set_xlim( [ -1, 1 ] )
	ax.set_ylim( [ -1, 1 ] )

	for r in results:
		plt.plot( r.real, r.imag, marker = ".", color = [ 0, 0, 0 ], alpha = 1.0, label = "wave" )

	plt.grid( which = "major", alpha=0.8 )
	plt.grid( which = "minor", alpha=0.3 )

	if filename:
		plt.savefig( filename )
	else:
		plt.show()
	
if __name__ == "__main__":
	main()

