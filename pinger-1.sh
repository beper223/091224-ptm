#!/bin/bash
#

if [ -z "$1" ]; then
    echo "Ошибка: необходимо передать адрес для пинга."
    exit 1
fi

address=$1
counter=0

while true; do
    ping_output=$(ping -c 1 "$address" 2>&1)

    if echo "$ping_output" | grep -q "time="; then
	counter=0
        ping_time=$(echo "$ping_output" | grep -oP 'time=\K[0-9.]+')
        if (( $(echo "$ping_time > 1" | bc -l) )); then
            echo "Время пинга превышает 100 мс: $ping_time ms"
        fi
        
    else
        ((counter++))
        if (( counter >= 3 )); then
            echo "Не удается выполнить пинг в течение 3 последовательных попыток."
            exit 1
        fi
    fi
    sleep 1
done
