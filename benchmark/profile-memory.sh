#!/bin/sh
set -e

mkdir -p memory-stats

# for sample_size in 50 100 200 500; do
# 	for variables in 500 1000; do
# 		echo $sample_size, $variables
# 		for _ in $(seq 1 10); do
# 			/usr/bin/time -f %M -o memory-stats/${sample_size}-${variables}.txt -a poetry run python run-dense-isn.py $sample_size $variables
# 		done
# 	done
# 	echo "500,1000" >memory-stats/memory-${sample_size}.csv
# 	paste -d',' memory-stats/${sample_size}-500.txt memory-stats/${sample_size}-1000.txt >>memory-stats/memory-${sample_size}.csv
# done

for sample_size in 50 100 200 500; do
	for variables in 500 1000; do
		echo $sample_size, $variables
		# for _ in $(seq 1 10); do
		# 	/usr/bin/time -f %M -o memory-stats/R-${sample_size}-${variables}.txt -a Rscript run-lioness.R $sample_size $variables
		# done
	done
	echo "500,1000" >memory-stats/R-memory-${sample_size}.csv
	paste -d',' memory-stats/R-${sample_size}-500.txt memory-stats/R-${sample_size}-1000.txt >>memory-stats/R-memory-${sample_size}.csv
done

poetry run python plot-memory.py
