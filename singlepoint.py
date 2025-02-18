#!/usr/bin/env python3

import	matplotlib.pyplot as plt
import	numpy as np
import	math
import	cmath

amplitude_ratio	= 0.8
phase_degree	= 330
frequency		= 1
N				= 2048

x	= np.linspace( 0, N - 1, N )

def main():
	phase_radian	= np.pi / (180 / phase_degree)

	#x	= np.linspace( 0, 2 * np.pi, N ) * frequency
	f	= frequency * (x / N) * 2 * np.pi

	y	= amplitude_ratio * np.sin( f + phase_radian )

	s	= np.sin( f )
	c	= np.cos( f )

	r	= y * s
	i	= y * c

	result	= complex( sum( r ) / (N / 2), sum( i ) / (N / 2) )

	print( f"result= {result}  .. abs:{abs( result )}, phase[°]:{cmath.phase( result ) * 180 / np.pi}" )

	plot_timedomain( y, s, c, r, i, "result_timedomain.png" )
	plot_cplane( result, "result_cplane.png" )
	

def plot_timedomain( wave, s, c, r, i, filename = None ):
	fig	= plt.figure( figsize=( 9, 6 ) )
	ax	= fig.add_subplot( 111 )
	ax.set_ylim( [ -1, 1 ] )

	plt.plot( x, wave, color = [ 0, 0, 0 ], alpha = 1.0, label = "wave" )
	plt.plot( x, s, color = [ 0, 0, 1 ], alpha = 0.1, label = "sin()" )
	plt.plot( x, c, color = [ 1, 0, 0 ], alpha = 0.1, label = "cos()" )
	plt.plot( x, r, color = [ 0, 0, 1 ], alpha = 0.7, label = "wave * sin()" )
	plt.plot( x, i, color = [ 1, 0, 0 ], alpha = 0.7, label = "wave * cos()" )

	plt.grid( which = "major", alpha=0.8 )
	plt.grid( which = "minor", alpha=0.3 )
	plt.legend()
	
	if filename:
		plt.savefig( filename )
	else:
		plt.show()

def plot_cplane( r, filename = None ):
	fig	= plt.figure( figsize=( 6, 6 ) )
	ax	= fig.add_subplot( 111 )
	ax.set_xlim( [ -1, 1 ] )
	ax.set_ylim( [ -1, 1 ] )

	plt.plot( r.real, r.imag, marker = ".", color = [ 0, 0, 0 ], alpha = 1.0, label = "wave" )

	plt.grid( which = "major", alpha=0.8 )
	plt.grid( which = "minor", alpha=0.3 )

	if filename:
		plt.savefig( filename )
	else:
		plt.show()
	
if __name__ == "__main__":
	main()

