set terminal canvas jsdir ""
set output "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_1/contigs_reports/nucmer_output/meta_contigs_1.html"
set ytics ( \
 "0" 0, \
 "6000" 6000, \
 "12000" 12000, \
 "18000" 18000, \
 "24000" 24000, \
 "30000" 30000, \
 "36000" 36000, \
 "42000" 42000, \
 "48000" 48000, \
 "" 50304 \
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
set yrange [1:50304]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_1/contigs_reports/nucmer_output/meta_contigs_1.fplot" title "FWD" w lp ls 1, \
 "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_1/contigs_reports/nucmer_output/meta_contigs_1.rplot" title "REV" w lp ls 2
