#!/bin/bash
set -e

cd "HOME/proyectosemma"STREAMINGJAR=(find "$HADOOP_HOME/share/hadoop/tools/lib" \
  -name 'hadoop-streaming-*.jar' | head -n 1)

if [ -z "STREAMINGJAR"];thenecho"NoseencontróelJARdeHadoopStreaming."exit1fiifhdfsdfs-test-e/semma/modelo;thenecho"Lasalidaanteriorexiste.Eliminando..."hdfsdfs-rm-r/semma/modelofihadoopjar"STREAMING_JAR" \
  -Dmapreduce.job.reduces=1 \
  -files "PWD/alquileresporhora.py,PWD/reducir_alquileres.py" \
  -input /semma/modificado/hour_limpio.csv \
  -output /semma/modelo \
  -mapper "python3 alquileres_por_hora.py" \
  -reducer "python3 reducir_alquileres.py"

echo "Resultados del modelo:"
hdfs dfs -cat /semma/modelo/part-00000
