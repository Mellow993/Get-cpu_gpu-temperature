#!/bin/bash
# Funktionen
function balken
{
    echo "#################################"
}

# filenames
pythonfile=main_temperatur.py
filename_gpu=val_gpu
filename_cpu1=Core1
filename_cpu2=Core2
filename_cpu3=Core3
filename_cpu4=Core4

# Variablen
sekunden=0

balken
echo "Get temperature of all Cores and the GPU"
echo "Check if $filename_gpu is available"
balken

if [ -f $pythonfile ] # Check if python file is available
then
    echo "$pythonfile available"
else
    echo "pythonfile not available"
    exit 1
fi

if [ -f $filename_gpu ] # Check if val_gpu is available
then
    echo "$filename_gpu available"
    rm $filename_gpu
    echo "$filename_gpu has been deleted"

else
    echo "$filename_gpu does not exists"
    echo "$filename_gpu will be created"
fi

if [ -f $filename_cpu1 ] # Check if Core1 is available
then
    echo "$filename_cpu1 available"
    rm $filename_cpu1
    echo "$filename_cpu1 has been deleted"
else
    echo "$filename_cpu1 will be created"
fi

if [ -f $filename_cpu2 ] # And so on...
then
    echo "$filename_cpu2 available"
    rm $filename_cpu2

    echo "$filename_cpu2 has been deleted"

else
    echo "$filename_cpu2 will be created"
fi

if [ -f $filename_cpu3 ] # And so on...
then
    echo "$filename_cpu3 available"
    rm $filename_cpu3
    echo "$filename_cpu3 has been deleted"

else
    echo "$filename_cpu3 will be created"
fi

if [ -f $filename_cpu4 ] # And so on...
then
    echo "$filename_cpu4 available"
    rm $filename_cpu4
    echo "$filename_cpu4 has been deleted"

else
    echo "$filename_cpu4 will be created"
fi

read -p  "Enter a title name: " titelname
echo "$titelname will be your titlename"
echo "How long should the measurement take?"
read -p "Enter 0 when you want to interrupt the measurement by yourself: " dauer_messung
if [ $dauer_messung == 0 ]
then
    echo "To quit the measurement press Strg+C"
    dauer_messung=86400 
else
    echo "It will be measured for $dauer_messung seconds"
fi
balken
echo "Start in 3 seconds"
balken
for (( i=2; i>=0; i-- ))
do
    echo "Start in $i seconds"
    sleep 1
done

balken
echo "Start measurement"

while [ 0 ]
do
    sleep 1
    sensors -u coretemp-isa-0000  >> Core_ges       # Core temperature
    nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader >> val_gpu # GPU temperature
    echo "$sekunden seconds"
    sekunden=$(( sekunden+1 ))

    if [ $dauer_messung == $sekunden ]
    then
        break
    fi

    trap "break; exit " 2
done

echo "While has been left"

# Processor temperature
cat Core_ges | grep temp2_input  >> Core11
cat Core_ges | grep temp3_input  >> Core22
cat Core_ges | grep temp4_input  >> Core33
cat Core_ges | grep temp5_input  >> Core44

# Prepare for the python script
awk ' {print $2} ' Core11 >> $filename_cpu1
awk ' {print $2} ' Core22 >> $filename_cpu2
awk ' {print $2} ' Core33 >> $filename_cpu3
awk ' {print $2} ' Core44 >> $filename_cpu4

# Delete help files
rm Core11
rm Core22
rm Core33
rm Core44
rm Core_ges

python3 $pythonfile $titelname
