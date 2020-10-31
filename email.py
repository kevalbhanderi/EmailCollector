# email collector

import re

str = """Dative Preposition  Sentences:-
Ich komme  aus dem BUro um sieben Uhr.
Ich komme um 7 Uhr  aus dem BUro.
Ich gebe antwort nach die Frage.
Ich schlafe mit meinem Alteren Bruder.
Der Tempel  ist bei  meinem/dienem/seinem  Haus.
Ich nehme hilfe von  meinem vater. / MEIN VATER HILFT MIR.
Ich arbeite in das BUro seit vier Jahren.
Die studenten spielen das Kricket gegenUber dem Klassenzimmer.

kaival965@gmail.com
school.collage@edu.in
nike@brand.com
Ml.DS@edu.com

Akk.. Preposition  Sentences:-
Mein vater nehme Mittagessen um zwei Uhr in den mittag.
Ich gehe fUr dich.
Ich lesse das Buch bis zwei Uhr.
Mein  Bruder kommt durch das Auto. 
Ich gehe entlang den FuBweg. / Ich gehe auf den Fussweg.
Der dieb Offnet die TUr ohne  SchlUssel.  (open – Offnen)
Ich spreche nicht wider meinen vater.

Two  way  sentences :-

A.	Ich stehe vor den Spiegel.
D. Der Spiegel ist vor meinem bett.

A.	Ich gehe neben den lakeview Garten.
D. Mein Haus ist neben dem lakeview garten.

A.	Meine schwester zeichnet an die wand.
D. Die lampe hAngt an der wand.

A.	Ich fahre das Auto hinter mein Haus.
D. Die schule hinter meinem Haus.

A.	Ich lade mein Handy auf den Tisch.
D. Der laptop liegt auf dem Tisch.

A.	Ich stelle meiner schlAger unter den Tisch.
D. Meiner schlAger ist unter dem Tisch.
"""

# email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][0-9a-zA-Z.]+",str)
email = re.findall(r"\w+@\S+\w",str)
print(email)
