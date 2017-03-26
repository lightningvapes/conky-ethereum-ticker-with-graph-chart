#!/usr/bin/gnuplot
reset

set terminal png size 450,200
set term png transparent truecolor

set style rectangle fillstyle noborder
unset xtics
set autoscale y
set linetype 1 lc rgb 'green'
set ytics font 'Verdana,16'
set ytics textcolor rgb 'white'
set ytics 1
set title '12 hrs' offset 0,-10.7
set title font 'Verdana,16'
set title textcolor rgb 'white'
set ylabel '$'
set ylabel font 'Verdana,20' textcolor rgb 'white' offset 44,0
set ylabel rotate by 180
set output '~/eth-price-graph/download.png'

plot '< tail -n 144 ~/eth-price-graph/prices.txt' lw 3 with lines notitle