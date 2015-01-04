for i in MS*xml; do j=`echo $i | sed s/MS/ms/`; cp $i $j; done
