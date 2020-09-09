# Python Academy 2020 - Movie Dataset Exercise

## Project Structure

<img src="images/project_tree.png" width="200"/>

- **main:** File containing all the Exercises 
- **filters:** Package containing some filtering functions
- **impor_helper:**  Importing helper functions.

## Exercise 
Note: Some results presented errors importing the dataset as not all data had an ending quotechar in 'whiteSpace'. This is why some data  values may present different results.

-    list(csv.reader(csvfile, delimiter=',', quotechar='\n')
-    list(csv.reader(csvfile, delimiter=',', quotechar=' ')

I had doubts on how to proceed on this. Finally, I took the decision on skipping the data with no complete values and taking only data with quotechar ending in '\n'


#### - How many Black & White and color movies are in the list?
- 5024 Black and White and color movies are present - elapsed time : 6 ms
- 4815 Black and White and color movies are present - elapsed time : 3.9 ms 

#### -  How many movies were produced by director in the list?

Director per movie quantity [('', 104), ('Steven Spielberg', 26), ('Woody Allen', 22), ('Martin Scorsese', 20), ('Clint Eastwood', 20), ('Ridley Scott', 17), ('Tim Burton', 16), ('Steven Soderbergh', 16), ('Spike Lee', 16), ('Renny Harlin', 15), ('Oliver Stone', 14), ('Sam Raimi', 13), ('Michael Bay', 13), ('Robert Zemeckis', 13), ('Ron Howard', 13), ('Joel Schumacher', 13), ('Barry Levinson', 13), ('Robert Rodriguez', 13), ('John Carpenter', 13), ('Peter Jackson', 12), ('Shawn Levy', 12), ('Richard Donner', 12), ('Tony Scott', 12), ('Brian De Palma', 12), ('Wes Craven', 12), ('Kevin Smith', 12), ('Rob Cohen', 11), ('Chris Columbus', 11), ('Rob Reiner', 11), ('Francis Ford Coppola', 11), ('Stephen Frears', 11), ('Richard Linklater', 11), ('Brett Ratner', 10))

Elapsed time :  6.8 ms

What Can I say? Empty director, unknown, is also an answer xD

#### - Which are the 10 less criticized movies in the list?

 [('Godzilla Resurgence\xa0', '1'), ('Harry Potter and the Deathly Hallows: Part II\xa0', '1'), ('Godzilla Resurgence\xa0', '1'), ('Ben-Hur\xa0', '1'), ('Ben-Hur\xa0', '1'), ('The Border\xa0            ', '1'), ('10 Days in a Madhouse\xa0', '1'), ('The Bold and the Beautiful\xa0            ', '1'), ('Barfi\xa0', '1'), ('Ben-Hur\xa0', '1')] 
 
 Elapsed time 0.006 seconds
 
#### - Which are the 20 longest-running movies in the list?

20 longest movies are : '
' [('Trapped\xa0            ', '511'), ('Carlos\xa0            ', '334'), ('"Blood In', '330'), ("Heaven's Gate\xa0", '325'), ('The Legend of Suriyothai\xa0', '300'), ('Das Boot\xa0', '293'), ('Apocalypse Now\xa0', '289'), ('The Company\xa0            ', '286'), ('Gods and Generals\xa0', '280'), ('Gettysburg\xa0', '271'), ('Arn: The Knight Templar\xa0', '270'), ('Cleopatra\xa0', '251'), ('Once Upon a Time in America\xa0', '251'), ('The Wolf of Wall Street\xa0', '240'), ('Gandhi\xa0', '240'), ('Emma\xa0            ', '240'), ('Dances with Wolves\xa0', '236'), ('Lawrence of Arabia\xa0', '227'), ('Gone with the Wind\xa0', '226'), ('The Greatest Story Ever Told\xa0', '225')] 

Elapsed time 0.0059680938720703125 seconds 

#### Which are the top 5 movies that raised more money in the list?
5 more profitable movies are : '
' [('Avatar\xa0', '760505847'), ('Titanic\xa0', '658672302'), ('Jurassic World\xa0', '652177271'), ('The Avengers\xa0', '623279547'), ('The Avengers\xa0', '623279547')] 

Elapsed time 0.005738973617553711 seconds 

#### Which are the top 5 movies that made the least money in the list?
5 less profitable movies are : '
[('Skin Trade\xa0', '162'), ('The Jimmy Show\xa0', '703'), ('In Her Line of Fire\xa0', '721'), ('Out of the Blue\xa0', '728'), ("Perrier's Bounty\xa0", '828')] 

Elapsed time 0.004220724105834961 seconds 

#### Which are the top 3 movies that expend more money to be produced in the list?
Top 3 more expensive movies : '
' [('The Host\xa0', '12215500000'), ('Lady Vengeance\xa0', '4200000000'), ('Fateless\xa0', '2500000000')] 

Elapsed time 0.00641322135925293 seconds 

#### Which are the top 3 movies that expend less money to be produced in the list?
Top 3 low cost movies : '
' [('Tarnation\xa0', '218'), ('A Plague So Pleasant\xa0', '1400'), ('The Mongol King\xa0', '3250')] 

Elapsed time 0.0046918392181396484 seconds 

#### What year was the one who had more movies released ?

The year with more movies releases was : '
' ('2009', 255) 

Elapsed time 0.002627134323120117 seconds 

#### What year was the one who had less movies released ?
The year with less movies releases was 1927 with 1 movie(s)

Elapse time  0.002347707748413086 Seconds

#### Create a actor ranking ordered by number of performances by:
#### - Number of movies where the actor performed
#### - Social Media Influence
#### - Best Movie

Actor ranking : 
('Robert De Niro', 54, 1188000, 7.118836910088769)
('Morgan Freeman', 45, 495000, 7.8965078860196005)
('Johnny Depp', 41, 1640000, 6.568560059206175)
('Bruce Willis', 39, 507000, 6.231539757813152)
Elapsed time :  0.04546689987182617 secodns

#### Create a “tag cloud” using tags or keywords of the movie: To do this you can create an ordered ranking
#### of the number of word occurrences.

The 1123
of 481
the 455
and 138
A 101
in 100
to 99
a 84
2 79

Elapsed time :  1.029115915298462 Seconds

## What movie genre raised more money per year?
## What movie genre raised less money per year?

==
Raised more money in  2009 Action
Raised less money in  2009 Sci-Fi
==
==
Raised more money in  2007 Adventure
Raised less money in  2007 Western
==
==
Raised more money in  2015 Animation
Raised less money in  2015 Western
==
==
Raised more money in  2012 Action
Raised less money in  2012 War
==
==
Raised more money in  2004 Adventure
Raised less money in  2004 Drama
==
==
Raised more money in  1997 Action
Raised less money in  1997 Sci-Fi
==
==
Raised more money in  2011 Comedy
Raised less money in  2011 Horror
==
==
Raised more money in  1992 Action
Raised less money in  1992 Drama
==
==
Raised more money in  2013 Comedy
Raised less money in  2013 Thriller
==
==
Raised more money in  2010 Comedy
Raised less money in  2010 Sci-Fi
==
==
Raised more money in  2008 Action
Raised less money in  2008 Horror
==
==
Raised more money in  2003 Action
Raised less money in  2003 Horror
==
==
Raised more money in  1999 Comedy
Raised less money in  1999 Horror
==
==
Raised more money in  1998 Comedy
Raised less money in  1998 Drama

Elapse time in seconds :  0.021592140197753906

#### What movie genre does the public like most?
More Liked Movies by the Community 
Drama 55762519
Comedy 27172616
Adventure 24387570
Crime 20474813
Family 19189809
Mystery 15435951
Fantasy 12252970
Horror 11698541
Romance 10064550
Sci-Fi 9836726
Animation 7744928
History 6414301
Action 5800364
Music 4051801
Biography 3000926
Thriller 2216522
Musical 1768012
Documentary 1127952
Western 583027
War 143643
Film-Noir 113234
Reality-TV 60050
Sport 58643
Short 11700
Game-Show 4834
Elapse timme in seconds  0.029370784759521484

#### Which are the top five best reputation directors?
Steven Spielberg 6582
Ridley Scott 4930
Peter Jackson 4542
Martin Scorsese 4285
Clint Eastwood 4244
