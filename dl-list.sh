
# sh dl-list.sh links.txt yt-dlp
for f in `cat $1`
do
    echo $2 "'"$f"'"
done

