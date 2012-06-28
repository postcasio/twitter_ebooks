# twitter_ebooks

twitter_ebooks is a COBE markov-chain tweetbot. It takes a training file of flat text and generates tweets each time twert.py is run.

Based on thom_ebooks by CelestialBeard, available at https://github.com/CelestialBeard/thom_ebooks/

## DEPENDENCIES
* Python 2.7
* [COBE](https://github.com/pteichman/cobe)
* [python-twitter](http://code.google.com/p/python-twitter/)

## SETUP

Create a new cobe brain:

<pre>cobe init</pre>

Prime it with your data:

<pre>cobe learn [file]</pre>

Create a twitter account and use it to register an application on dev.twitter.com. Set access to read/write and generate an access token. Enter the necessary information into config-example.py and rename it to config.py

Run `twert.py --stdout` to test. If the result is to your liking, you can schedule updates with cron.

For regular COBE use, including console and irc use, read the COBE README.

## TODO

Allow bot to "respond" to tweets by feeding the reply text into a b.reply.

## MAINTAINER

Dominic Adelaar <dom@casiotone.org> (twitter: @casiotone)

## LARGE ASCII ART IMAGE OF THOM

<pre>
                                                                                
                         MN8DDNMND87                                            
                           ZMN88888888DDNDZ                                     
                               ?NMN8888888888DNN8?                              
                                  $8MMM8888888888888MN                          
                           ?NNN88888888888888888888888DDM7                      
                        NN8OZZO888888888888888888888D88DDDDNNN7                 
                     MN88888OZZO888888888888888888D88DDDDDDD8D8DM7              
                  8D8888888888ZZO888888888888DDD888DDDDDDDDDDDDDD8N$            
                ON8888888888888ZZO888888888888DDDD8DDDDDDDDD8888D88DN           
               M88888N8888888888ZZO8888888DD88DDDDDDDDDDDDD8888888888N          
             D88DMN?ZD88888888888ZZO8888888DDDDDDDDDDDDDD8DD8888888888NI        
           OMD?    D88888D88888888ZZO8888DMO88DDDDDDDD88D88D888888888N8D8       
          D       ZD8DDDD8888888888ZZO8NO===MDDDDDD88D8888888888888888MM88      
                  NDDDD888DD8888DM888D+====+NDDD8DD88D8888888888888888D?DN8     
                 MDDDDDDDDD888NZN8NO~======ID8DD88D88888888888888888888N  M$    
                N8DDDDDDDD8NO7NDN==========$888D8888888888D8888D88D8888D        
                NDDDDDNDDD8?NDD============O88888888888888D8888D88D888888       
               M8DDDMNDDN+NDN==============D88888888888888DD888DD8DD88D8N       
              $DDDDMN8MIDDN===+OZODO=======M8888D8888D8888DD888DD88D88D8M       
              MNNDDNNZ7NN=============DI===M88M8DD888DD888DDD88DDDDDD8DDN       
             MZ$DNMN~MNZZ=~:::::::======I8=M88M8DDD88DD888DDDDDDDDDDDDDDN       
             8 ZDM$MM8+~=~::::::~+=========M88M8DDD8DDDD88DDDDDDDDDDDDDDN       
            Z  ?ND8NNID~=::::::~I7I+=======M88MDDDDDDDDD8DDDDDDDDDDDDDDDM       
                D::~+77MMDND88O7:...?I?M$==M88NNDDDDDDDDDDDDDDDDDDDDDDDDD       
                MDO   .D$:=+8:: ..,::~=7NMZM8D$MDDDDDDDDDDDD8DDDDDMDDDDDZ       
                MMM,  ,D?=:~8::      .?NNNNM8D8D8DDDNDDDDDDMDDDDDDDM8DDN        
                IZZ+D8=DI=:~8:::       +D:=M8N=7DDDDMDDDDDNNDDDDDDDMNDDN        
                 D7====88::~8::::+$OOI::D:=M8N~+MDDNMDDDDDNDDDDDDDDND8DO        
                  =7ODD$7::~8~~::::::::+8:=N8N~=MDDNMDDDDDZ8DDDDDDDM MD7        
                 O~====8:::::,:+7$O8887,::=D8D~=M8DMNDDDM~MDDDDDDDDM MD         
                 N~===8:::::::::::::::::::=Z8D==N8DMDDDM$IDDDDDDDDDM  M         
                 O==8=:::::::::::::::::::~=7DO==N8DM8NDD~MDDDDDDNDDM  MI        
                 7=I:::::::::::::::::::::~=?N$==N8MDN?+=N8DDDDDMODDD  ZZ        
                 Z+O,:::7::::::::::::::::~++MI==MN+====N8DDDDDDO7DD8   8        
                 D~=+$I::::::::::::::::::~+=M+==MZ==~ZNDDDDDDDN M8N             
                  D===~::::::::::::::::::~+=M==IO=?M8DDDDDDDDN  NDD             
                   Z7I~:::::::::::::::::::+=D~=N~=DMDDNDDDDDM  M8N              
                    I=8NNNM$+:::::::::::::==?====O~MZMMN  MN  $DDZ              
                    8=DMN$ONNNI:::::::::::==:==:8~=7 8Z  M$   MNZ               
                     N~=~:~=+78D::::::::::::::8?====N                           
                      8==~:::::::::::::::::+D+======?$                          
                       ?==::::::::::::::IDI==========8                          
                       D~=:::::::::I8D7+==============8                         
                         OOOOZ?    N~=====~:::::+=====+MDM                      
                                   8I===::::::::=======8NNNN                    
                               MNNM=7=~:::::::::~======ONNNNNN                  
                              ZNNM~===::::::::::=======DNNNNNNNM                
                            OMNNND~===::::::::::=======MNNNNNNNNNM?             
</pre>
