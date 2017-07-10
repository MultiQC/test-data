set terminal canvas jsdir ""
set output "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_3/contigs_reports/nucmer_output/meta_contigs_2.html"
set ytics ( \
 "0" 0, \
 "8000" 8000, \
 "16000" 16000, \
 "24000" 24000, \
 "32000" 32000, \
 "40000" 40000, \
 "48000" 48000, \
 "56000" 56000, \
 "" 63015 \
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
set yrange [1:63015]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_3/contigs_reports/nucmer_output/meta_contigs_2.fplot" title "FWD" w lp ls 1, \
 "/home/vsaveliev/quast/quast_test_output/runs_per_reference/meta_ref_3/contigs_reports/nucmer_output/meta_contigs_2.rplot" title "REV" w lp ls 2
