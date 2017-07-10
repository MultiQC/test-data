set terminal canvas jsdir ""
set output "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_2/contigs_reports/nucmer_output/meta_contigs_1.html"
set ytics ( \
 "0" 0, \
 "7000" 7000, \
 "14000" 14000, \
 "21000" 21000, \
 "28000" 28000, \
 "35000" 35000, \
 "42000" 42000, \
 "49000" 49000, \
 "56000" 56000, \
 "" 59158 \
)
set size 1,1
set grid
set key outside bottom right
set border 0
set tics scale 0
set xlabel "Reference" noenhanced
set ylabel "Assembly" noenhanced
set format "%.0f"
set xrange [1:*]
set yrange [1:59158]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_2/contigs_reports/nucmer_output/meta_contigs_1.fplot" title "FWD" w lp ls 1, \
 "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_2/contigs_reports/nucmer_output/meta_contigs_1.rplot" title "REV" w lp ls 2
