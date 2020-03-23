#!/bin/sh
while (( "$#" ));
do
    key=$1
    val=$2
    #shift by two
    shift 2
    case $key in
       -i)
       id=$val;;
       -o)
       output=$val;;
       -c)
       col=$val;;
       -h)
       html=$val;;
       *);;
    esac
done

python get_pdb.py --id $id --output $id.pdb
if (($col))
#if colorized parameter not empty
then java -jar C://Users//Maxim//Desktop//Jmol-14.30.2-binary//jmol-14.30.2//Jmol.jar  ${id}.pdb -n -s non_col_cartoon.txt -w JPG:./img/${output}.jpg -x
#then java -jar /mnt/biosoft/software/Jmol.jar $id.pdb -n -s non_col_cartoon.txt -w JPG:${output}.jpg -x

#if colorized parameter empty
else java -jar C://Users//Maxim//Desktop//Jmol-14.30.2-binary//jmol-14.30.2//Jmol.jar ${id}.pdb -n -s col_cartoon.txt -w JPG:./img/${output}.jpg -x
#else java -jar /mnt/biosoft/software/Jmol.jar/Jmol.jar $id.pdb -n -s col_cartoon.txt -w JPG:${output}.jpg -x
#rm $id.pdb
fi
