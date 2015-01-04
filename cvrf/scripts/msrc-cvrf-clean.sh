for i in `ls *.xml`; do sed 's/<vuln:BaseScore\/>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:TemporalScore\/>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:EnvironmentalScore\/>//g' $i > tmp.xml; mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:Vector\/>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:ProductID\/>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:GroupID\/>//g' $i > tmp.xml;	mv tmp.xml $i; done;

for i in `ls *.xml`; do sed 's/<vuln:BaseScore><\/vuln:BaseScore>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:TemporalScore><\/vuln:TemporalScore>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:EnvironmentalScore><\/vuln:EnvironmentalScore>//g' $i > tmp.xml; mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:Vector><\/vuln:Vector>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:ProductID><\/vuln:ProductID>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<vuln:GroupID><\/vuln:GroupID>//g' $i > tmp.xml;	mv tmp.xml $i; done;

for i in `ls *.xml`; do sed 's/<cvrf:CurrentReleaseDate><\/cvrf:CurrentReleaseDate>//g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/<cvrf:CurrentReleaseDate\/>//g' $i > tmp.xml;	mv tmp.xml $i; done;

for i in `ls *.xml`; do sed 's/<cvrf:Version\/>//g' $i > tmp.xml;	mv tmp.xml $i; done;

for i in `ls *.xml`; do sed 's/Ordinal=\"\"/Ordinal=\"1\"/g' $i > tmp.xml;	mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/Date=\"\"//g' $i > tmp.xml;	mv tmp.xml $i; done;

#20141231 this is a poor fix for a problem that MSRC is likley to fix soon
for i in `ls *.xml`; do sed 's/xmlns:xd=\"http:\/\/schemas.microsoft.com\/office\/infopath\/2003\"/xmlns:xd=\"http:\/\/schemas.microsoft.com\/office\/infopath\/2003\">/' $i > tmp.xml; mv tmp.xml $i; done;
for i in `ls *.xml`; do sed 's/>>/>/' $i > tmp.xml; mv tmp.xml $i; done;

