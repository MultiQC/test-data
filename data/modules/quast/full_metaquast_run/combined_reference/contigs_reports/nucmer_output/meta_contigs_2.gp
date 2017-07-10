set terminal canvas jsdir ""
set output "/home/vsaveliev/quast/quast_test_output/combined_reference/contigs_reports/nucmer_output/meta_contigs_2.html"
set xtics rotate ( \
 "0" 0, \
 "20000" 20000, \
 "40000" 40000, \
 "60000" 60000, \
 "80000" 80000, \
 "100000" 100000, \
 "120000" 120000, \
 "140000" 140000, \
 "160000" 160000, \
 "" 179997 \
)
set ytics ( \
 "0" 0, \
 "20000" 20000, \
 "40000" 40000, \
 "60000" 60000, \
 "80000" 80000, \
 "100000" 100000, \
 "120000" 120000, \
 "140000" 140000, \
 "160000" 160000, \
 "" 172703 \
)
set size 1,1
set grid
set key outside bottom right
set border 0
set tics scale 0
set xlabel "Reference" noenhanced
set ylabel "Assembly" noenhanced
set format "%.0f"
set xrange [1:179997]
set yrange [1:172703]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/home/vsaveliev/quast/quast_test_output/combined_reference/contigs_reports/nucmer_output/meta_contigs_2.fplot" title "FWD" w lp ls 1, \
 "/home/vsaveliev/quast/quast_test_output/combined_reference/contigs_reports/nucmer_output/meta_contigs_2.rplot" title "REV" w lp ls 2
